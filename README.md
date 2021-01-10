# CRUD operations in Flask Python3.7


Please enter the SQL credentials and Database name in "settings.yml" file in Configuration folder.

"""
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
    
    
    



"""

Two tables: 
	a) OEM_Specs_fields = ["engine_number"(PrimaryKey), 
				"model_type", 
				"year_of_model", 
				"list_price_of_new_vehicle",
				"available_colors", 
				"mileage", 
				"power", 
				"max_speed"
				]
	
	b) Marketplace_Inventory_fields = [   "item_id" (PrimaryKey), 
					    	"engine_number" (Foreign Key), 
					    	"km_on_odometer", 
					    	"major_scratches", 
					    	"original_paint",
                                     		"number_of_accidents_reported", 
                                     		"number_of_previous_buyers", 
                                     		"place_of_registration", 
                                     		"dealer_login_id"
                                     		]



APIs List:
	1. /create_database :-> To create DataBase in MySQL. Schema is present 'const.py' file.
	2. /delete_database :-> To delete DataBase.
	3. /create_table    :-> To create tables with given schema present in 'const.py' file.
	4. /delete_table    :-> To delete tables.
	5. /populate_table  :-> To populate/fill tables with entries given "crud_oem.sql" and "crud_inventory.sql".
	
	6. /search_oem         :-> To search all entries in OEM_Specs table.
	7. /search_inventory   :-> To search all entries in OEM_Specs table.
	
	8. /number_of_models   	:-> To get numbers of vehicles for each model in OEM_Specs table.
	9. /number_of_cars	   	:-> To get numbers of vehicles for a given model in OEM_Specs table.
	
	10. /oem_specs_of_model	:-> To get all features from OEM_Specs table for a given model type and model year.
	
	11. /insert_inventory 		:-> To insert a new entry by the dealer to the "Marketplace_Inventory". 
						These items must be entered by the dealer.
						[
						item_id,
                            			dealer_login_id,
                            			engine_number,
                            			km_on_odometer,
                            			major_scratches,
                            			original_paint,
                            			number_of_accidents_reported,
                            			number_of_previous_buyers,
                            			place_of_registration
                            			]
                            			
        12. /delete_from_inventory/engine_number   :-> To delete an entry from the "Marketplace_Inventory".
        13. /update_inventory 		:-> To update an entry with updated features.
                            			
	
	 
