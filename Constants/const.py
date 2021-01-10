from Utility import utility_file



sql_crud_filepath = [ "./dataset/crud_oem.sql", "./dataset/crud_inventory.sql"]



OEM_Specs_fields = ["engine_number", "model_type", "year_of_model", "list_price_of_new_vehicle",
                          "available_colors", "mileage", "power", "max_speed"]

Marketplace_Inventory_fields = ["item_id", "engine_number", "km_on_odometer", "major_scratches", "original_paint",
                                     "number_of_accidents_reported", "number_of_previous_buyers", "place_of_registration", "dealer_login_id"]


DB_NAME = utility_file.config["mysql_credentials"]["database"]
TABLES = {}

###------------------------------------------ TABLE 1 ------------------------------------------------------------------

"""
Original Equipment Manufacturers Specifications:
• To make life easier for the dealers, SMC lists all major Original Equipment Manufacturers (OEM)
OEM specs on their portal
• The specs are stored in a table OEM_Specs
• These include the name of the model, Year of Model, list price of the new vehicle, available colors,
mileage as advertised by the manufacturer, Power (in BHP), Max Speed
• Dealers can search for this information in the table (For example, they can search for Honda City 2015)
and get all the OEM Specs

"""

TABLES['oem_specs'] = (
    "CREATE TABLE `oem_specs` ("
    "  `engine_number` varchar(11) NOT NULL,"
    "  `model_type` varchar(10) NOT NULL,"
    "  `year_model` varchar(14) NOT NULL,"
    "  `list_price` varchar(16) NOT NULL,"
    "  `colors` varchar(6) NOT NULL,"
    "  `mileage` float(5) NOT NULL,"
    "  `power` float(6) NOT NULL,"
    "  `max_speed` float(6) NOT NULL,"
    "  PRIMARY KEY (`engine_number`)"
    ") ENGINE=InnoDB")





###------------------------------------------ TABLE 2 ------------------------------------------------------------------
"""
Inventory Related Information:
• Dealers can add their own information from their inventory
• This information is stored in Marketplace_Inventory table
• The Marketplace_Inventory table includes information like KMs on Odometer, Major Scratches,
Original Paint, Number of accidents reported, Number of previous buyers, Registration Place
"""

TABLES['inventory'] = (
    "CREATE TABLE `inventory` ("
    "  `item_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `engine_number` varchar(11) NOT NULL,"    
    "  `dealer_id` varchar(10) NOT NULL,"
    "  `kms_odometer` float(10) NOT NULL,"
    "  `major_scratches` enum('yes','no') NOT NULL,"
    "  `original_paint` varchar(6) NOT NULL,"
    "  `accidents_reported` int(5) NOT NULL,"
    "  `previous_buyers` int(6) NOT NULL,"
    "  `registration_place` varchar(10) NOT NULL,"    
    "  PRIMARY KEY (`item_id`),"
    "  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`engine_number`) "
    "     REFERENCES `oem_specs` (`engine_number`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")





########################################################################################################################
########################################################################################################################
########################################################################################################################



# DB_NAME = 'employees'

# TABLES = {}
# TABLES['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")
# TABLES['departments'] = (
#     "CREATE TABLE `departments` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `dept_name` varchar(40) NOT NULL,"
#     "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#     ") ENGINE=InnoDB")
# TABLES['salaries'] = (
#     "CREATE TABLE `salaries` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `salary` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
# TABLES['dept_emp'] = (
#     "CREATE TABLE `dept_emp` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
# TABLES['dept_manager'] = (
#     "  CREATE TABLE `dept_manager` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`),"
#     "  KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
# TABLES['titles'] = (
#     "CREATE TABLE `titles` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `title` varchar(50) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date DEFAULT NULL,"
#     "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")


########################################################################################################################
########################################################################################################################
########################################################################################################################




