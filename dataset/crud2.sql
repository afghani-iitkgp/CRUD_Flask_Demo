
--CREATE TABLE `OEM_Specs` (
--  `id` int(11) NOT NULL,
--  `modelName` varchar(255) NOT NULL,
--  `yearOfModel` varchar(255) NOT NULL,
--  `priceOfNewCar` varchar(255) NOT NULL,
--  `availableColors` varchar(255),
--  `mileage` varchar(255),
--  `power` varchar(255),
--  `maxSpeed` float(15),
--
--  PRIMARY KEY (`id`),
--) ENGINE=MyISAM DEFAULT CHARSET=latin1;
--
--
--CREATE TABLE `Marketplace_Inventory` (
--  `id` int(11) NOT NULL,
--  `engineNumber` varchar(100) NOT NULL,
--  `kmsOnOdometer` float(255) NOT NULL,
--  `majorScratches` varchar(255) NOT NULL,
--  `originalColor` varchar(255),
--  `numberOfAccidentsReported` int(25),
--  `numberOfPreviousBuyers` int(20),
--  `placeOfRegistration` varchar(50),
--
--   PRIMARY KEY (`id`)
--   CONSTRAINT FK FOREIGN KEY ('engineNumber')
--   REFERENCES `OEM_Specs` ('id')
--
--) ENGINE=MyISAM DEFAULT CHARSET=latin1;






INSERT INTO `oem_specs` (`engine_number`, `model_type`, `year_model`, `list_price`,
                          `colors`, `mileage`, `power`, `max_speed`) VALUES

('50WVC329931',	'Honda',	'2010',	'5.34',	'red',	'20',	'12',	'100')
('50WVC329932',	'Toyota',	'2015',	'7.23',	'blue',	'21',	'10',	'180')
('50WVC329933',	'Maruti',	'2016',	'4.33',	'green',	'17',	'14'	'200')
('50WVC329934',	'Cheverlett',	'2017',	'10.25',	'pink',	'12',	'8',	'300')
('50WVC329935',	'Audi',	'2018',	'22.36',	'scarllet blue',	'14',	'21',	'180')
('50WVC329936',	'Tata',	'2019',	'10.23',	'white',	'10',	'17.8',	'220')
('50WVC329937',	'Honda',	'2008',	'18.22',	'black',	'18',	'19.4',	'190')
('50WVC329938',	'Mahindra',	'2009',	'8.25',	'green',	'16',	'21',	'190')
('50WVC329939',	'Maruti',	'2014',	'10.25',	'red',	'14',	'22.6',	'180')
('50WVC329940',	'Cheverlett',	'1999',	'9.26',	'blue',	'21',	'24.2',	'150')
('50WVC329941',	'mahindra',	'2001',	'8.27',	'green',	'20',	'25.8',	'190')
('50WVC329942',	'Mercedes',	'2018',	'30.29',	'pink',	'21',	'27.4',	'320')
('50WVC329943',	'Honda', '2000',	'14.26',	'scarllet blue',	'18',	'29',	'180')
('50WVC329944'	'Jeep'	'2017'	'25.24'	'white'	'20',	'30.6', '228')
('50WVC329945', 'Tata',	'2003',	'8.69',	'black',	'15',	'32.2',	'198');










INSERT INTO `inventory` (`item_id`, `engine_number`, `kms_odometer`, `major_scratches`, `original_paint`,
                                     `accidents_reported`, `previous_buyers`, `registration_place`, `dealer_id`) VALUES

('abc112',	12222,	'yes',	'green',	1,	1,	'Jamshedpur',	'50WVC329931', 'ABC')
('abc113',	15455,	'no',	'blue',	    0,	1,	'kolkata',	'50WVC329932', 'ABC')
('abc114',	145578,	'yes',	'white',	2,	1	'bangalore',	'50WVC329933', 'ABC')
('abc115',	174481,	'no',	'black',	1,	2	'mumbai',	'50WVC329934', 'ABC')
('abc116',	451520,	'no',	'pink',	    1,	1,	'mumbai',	'50WVC329935', 'ABC')
('abc117',	456787,	'no',	'red',	    1,  2,	'delhi',	    '50WVC329936', 'ABC')
('abc118',	4165464,'no',	'white',	3,	3,	'chennai',	'50WVC329937', 'ABC')
('abc119',	4654783, 'yes',	'black',	4,	4,	'delhi',	    '50WVC329938', 'ABC')
('abc120',	698445,	'yes',	'black',	5,	2,	'indore',    '50WVC329939', 'ABC')
('abc121',	87452,	'no',	'black',	2,	1,	'ahmedabad',	'50WVC329940', 'ABC');

('abc122',	456787,	'no',	'red',	    1,  2,	'delhi',	    '50WVC329936', 'DEF')
('abc123',	4165464,'no',	'white',	3,	3,	'chennai',	'50WVC329937', 'DEF')
('abc124',	4654783, 'yes',	'black',	4,	4,	'delhi',	    '50WVC329938', 'DEF')
('abc125',	698445,	'yes',	'black',	5,	2,	'indore',    '50WVC329939', 'DEF')
('abc126',	87452,	'no',	'black',	2,	1,	'ahmedabad',	'50WVC329940', 'DEF');



