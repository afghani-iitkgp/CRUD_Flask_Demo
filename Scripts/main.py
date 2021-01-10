# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

import os
import json
import random
from flask import Flask, render_template
from flask import Blueprint
from flask import request
import pickle

import sys
import re
from collections import defaultdict
from Constants import const
import mysql.connector
from mysql.connector import errorcode

from Utility import utility_file





app = Blueprint("app", __name__)

exception_message = '{"status": False, "message": "Server Error, Please contact your Admin"}'
method_error_message = '{"status": False, "message": "Method not supported!!"}'


cnx = mysql.connector.connect(user=utility_file.config["mysql_credentials"]["user"],
                              password=utility_file.config["mysql_credentials"]["password"],
                              host=utility_file.config["mysql_credentials"]["host"]
                              )

cursor = cnx.cursor()

mydb_conn = mysql.connector.connect(user=utility_file.config["mysql_credentials"]["user"],
                                      password=utility_file.config["mysql_credentials"]["password"],
                                      host=utility_file.config["mysql_credentials"]["host"],
                                      database=utility_file.config["mysql_credentials"]["database"]
                                      )

mydb_cursor = mydb_conn.cursor()



#--------------------------------- Create Database and Tables-----------------------------------------------------------

@app.route("/create_database", methods=['GET'])
def create_database():
    DB_NAME = const.DB_NAME


    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        cursor.execute("USE {}".format(DB_NAME))

        db_list = []
        for db in cursor:
            print(db)
            db_list.append(db)

        return {"status": "Database is created successfully", "db_list": db_list}


    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        utility_file.logger.exception("Failed creating database" + str(err))

        try:
            cursor.execute("USE {}".format(DB_NAME))
            if err.errno == 1007:
                return {"status": "Database is present"}

        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            utility_file.logger.exception("Database does not exist" + str(err))

            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME

                return {"data": "Database created successfully"}
            else:
                print(err)
                exit(1)

        exit(1)


@app.route("/delete_database", methods=['POST'])
def delete_database():
    if request.method == "POST":

        DB_NAME = request.form["database_name"]

        try:
            cursor.execute("DROP DATABASE {} ".format(DB_NAME))
            db_list = []
            for db in cursor:
                print(db)
                db_list.append(db)

            return {"status": "Database is deleted successfully", "db_list": db_list}


        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            try:
                cursor.execute("USE {}".format(DB_NAME))
                return {"status": "Database is present"}

            except mysql.connector.Error as err:
                print("Database {} does not exists.".format(DB_NAME))
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    create_database(cursor)
                    print("Database {} created successfully.".format(DB_NAME))
                    cnx.database = DB_NAME

                    return {"data": "Database created successfully"}
                else:
                    print(err)
                    exit(1)

            exit(1)



@app.route("/delete_table", methods=['POST'])
def delete_table():
    if request.method == "POST":

        TABLE = request.form["table_name"]
        DB_NAME = const.DB_NAME


        try:
            cursor.execute("DROP TABLE {} ".format(TABLE))
            db_list = []
            for db in cursor:
                print(db)
                db_list.append(db)

            return {"status": "Table is deleted successfully", "db_list": db_list}


        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            try:
                cursor.execute("USE {}".format(DB_NAME))
                cursor.execute("DROP TABLE {} ".format(TABLE))
                return {"status": "Table is deleted successfully"}

                # return {"status": "Database is present"}

            except mysql.connector.Error as err:
                print("Database {} does not exists.".format(DB_NAME))
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    create_database(cursor)
                    print("Database {} created successfully.".format(DB_NAME))
                    cnx.database = DB_NAME

                    return {"data": "Database created successfully"}
                elif err.errno == 3730:
                    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                    cursor.execute("DROP TABLE {} ".format(TABLE))
                    return {"status": "Table is deleted successfully"}
                elif err.errno == 1051:
                    return {"status": "Table is not found, might be deleted in past."}






@app.route("/create_table", methods=['GET'])
def create_tables():


    if request.method == "GET":
        try:
            TABLES = const.TABLES
            DB_NAME = const.DB_NAME

            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    print("Creating table {}: ".format(table_name), end='')
                    mydb_cursor.execute(table_description)
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("table already exists.")
                        utility_file.logger.exception("table already exists" + str(err))
                        continue
                        # return {"data": "the '{}' table already exist".format(table_name)}
                    elif err.errno == errorcode.ER_NO_DB_ERROR:
                        mydb_cursor.execute("USE {}".format(DB_NAME))
                        print(err.msg)
                        utility_file.logger.exception("Exception occurs at :" + str(err.msg))
                        continue
                    elif err.errno == 1824:
                        continue

                else:
                    print("OK")
                    continue


            return {"status": "tables are created in the Database"}
            # cnx.close()

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))


@app.route("/populate_table", methods=['GET'])
def create():
    if request.method == "GET":
        try:
            DB_NAME = const.DB_NAME

            for filename in const.sql_crud_filepath:
                fd = open(filename, 'r')
                sqlFile = fd.read()
                fd.close()
                sqlCommands = sqlFile.split(';')

                for command in sqlCommands:
                    try:
                        if command.strip() != '':
                            mydb_cursor.execute(command)
                    except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                            print("table already exists.")
                            utility_file.logger.exception("Table already exist :" + str(err.msg))
                            return {"status": "table already exists."}
                        elif err.errno == errorcode.ER_NO_DB_ERROR:
                            mydb_cursor.execute("USE {}".format(DB_NAME))
                            print(err.msg)
                            utility_file.logger.exception("Exception occurs at :" + str(err.msg))
                            continue

                        else:
                            print(err.msg)
                            return {'status': "check table"}

            return {"status": "tables created"}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))



## ------------------------------------------------- Search Query from the tables by the dealers------------------------



@app.route('/search_oem')
def search_in_oem():
    if request.method == "GET":
        try:
            mydb_cursor.execute("SELECT  * FROM `oem_specs` ")
            data = mydb_cursor.fetchall()

            return {"data": data}
        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))

@app.route('/search_inventory')
def search_in_inventory():
    if request.method == "GET":
        try:
            mydb_cursor.execute("SELECT  * FROM `inventory` ")
            data = mydb_cursor.fetchall()

            return {"data": data}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))



####----------------------------------- PHASE II APIs ------------------------------------------------------------------



"""
1.1)  API to query the number of OEM models available. 
"""
@app.route('/number_of_models',methods=['POST','GET'])
def find_number_of_models():

    if request.method == 'GET':
        try:
            mydb_cursor.execute("""
                   SELECT COUNT(*), `model_type`
                   FROM `oem_specs` 
                   GROUP BY `model_type`
                   """)

            result = mydb_cursor.fetchall()

            resp = {}
            for item in result:
                resp[item[1]] = item[0]

            return {"data": resp}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))


"""
1.2) API to find the number of cars for a given model. 
"""
@app.route('/number_of_cars',methods=['POST','GET'])
def find_number_of_cars_of_a_model():

    if request.method == 'POST':

        try:

            model_type_name = request.form['model_type']

            mydb_cursor.execute("""
                   SELECT COUNT(*)
                   FROM `oem_specs` 
                   WHERE `model_type`="{0}"
                   """.format(model_type_name))

            result = mydb_cursor.fetchall()

            return {"data": result[0][0]}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))



"""
2) API to find the Original Equipment Manufacturers Specifications of cars for a given model with year of manufacture. 
"""
@app.route('/oem_spec_of_model',methods=['POST','GET'])
def get_oem_specs_of_a_model_with_year():

    if request.method == 'POST':
        try:
            model_type = request.form['model_type']
            model_year = request.form['model_year']

            mydb_cursor.execute("""
                   SELECT *
                   FROM `oem_specs` 
                   WHERE `model_type`="{0}" AND `year_model`={1}
                   """.format(model_type, model_year))

            result = mydb_cursor.fetchall()

            resp = defaultdict(list)
            for spec in result:
                dic = {}
                dic["engine_number"] = spec[0]
                dic["model_type"] = spec[1]
                dic["model_year"] = spec[2]
                dic["list_price_in_lakhs"] = spec[3]
                dic["color"] = spec[4]
                dic["mileage_at_showroom"] = spec[5]
                dic["power_in_BHP"] = spec[6]
                dic["max_speed"] = spec[7]

                resp["data"].append(dic)



            return resp

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))





## ------------------------------------------------- insert into the tables by the dealers------------------------------
"""
Dealers can add their own information from their inventory. This information is stored in Marketplace_Inventory table
"""
"""
3.1) API to insert a row to "inventory" table by a dealer. 
"""
@app.route("/insert_inventory", methods=["POST"])
def insert_into_inventory():
    if request.method == "POST":
        try:
            item_id = int(request.form['item_id'])
            dealer_login_id = request.form['dealer_id']
            engine_number = request.form['engine_number']
            km_on_odometer = int(request.form['kms_odometer'])
            major_scratches = request.form['major_scratches']
            original_paint = request.form['original_paint']
            number_of_accidents_reported = int(request.form['number_of_accidents_reported'])
            number_of_previous_buyers = int(request.form['number_of_previous_buyers'])
            place_of_registration = request.form['place_of_registration']


            mydb_cursor.execute(
                "INSERT INTO `inventory` (`item_id`, `dealer_id`, `engine_number`, `kms_odometer`, `major_scratches`, `original_paint`, `accidents_reported`, `previous_buyers`, `registration_place`)  VALUES "
                "({0},'{1}','{2}', {3}, '{4}', '{5}', {6}, {7}, '{8}');"
                    .format(item_id,
                            dealer_login_id,
                            engine_number,
                            km_on_odometer,
                            major_scratches,
                            original_paint,
                            number_of_accidents_reported,
                            number_of_previous_buyers,
                            place_of_registration))

            mydb_conn.commit()


            return {"data": "Data Inserted Successfully"}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))



@app.route('/delete_from_inventory/<string:engine_number>',  methods = ['GET'])
def delete_from_inventory(engine_number):
    if request.method == "GET":
        try:
            mydb_cursor.execute("DELETE FROM `inventory` WHERE engine_number=%s", (engine_number,))
            mydb_conn.commit()


            return {"data": "Record Has Been Deleted Successfully"}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))



@app.route('/update_inventory',methods=['POST','GET'])
def update_inventory():

    if request.method == 'POST':
        try:
            dealer_login_id = request.form['dealer_id']
            engine_number = request.form['engine_number']
            km_on_odometer = request.form['km_on_odometer']
            major_scratches = request.form['major_scratches']
            original_paint = request.form['original_paint']
            number_of_accidents_reported = request.form['number_of_accidents_reported']
            number_of_previous_buyers = request.form['number_of_previous_buyers']
            place_of_registration = request.form['place_of_registration']


            mydb_cursor.execute(
                "UPDATE `inventory` SET (`dealer_login_id`, `engine_number`, `km_on_odometer`, `major_scratches`, `original_paint`, `number_of_accidents_reported`, `number_of_previous_buyers`, `place_of_registration`)  VALUES "
                "({0},{1}, {2}, {3}, {4}, {5}, {6}, {7}) WHERE `engine_number` = {1}"
                    .format(dealer_login_id, engine_number, km_on_odometer, major_scratches, original_paint, number_of_accidents_reported, number_of_previous_buyers, place_of_registration))


            mydb_conn.commit()


            return {"data": "Data Updated Successfully"}

        except Exception as e:
            utility_file.logger.exception("Exception occurs" + str(e))


