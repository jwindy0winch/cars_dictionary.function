# cars_dictionary.function


# Overview of Program Requirements
Write a function that stores information about a car in a dictionary that includes: 
●	A function that always receive a manufacturer and model name
●	A function that accept an arbitrary number of keyword arguments 
●	Calling upon the function with required information and two other name-value pairs 

# Defined Scope:
Create a Dictionary Function, that includes mandatory and optional keyword arguments for details to several cars
# Intended Usage:
A database/dictionary for a car dealership to assist sales associates in selling cars for people looking for specific features. 

# Processing Logic


#Control & Data Flow:
The Car Dictionary Program begins by defining Required Program Parameters for the ‘car_dicationary’ function, including additional optional arguments with the use of the ‘**kwargs’ function. Inside the Function on Line 3 the dictionary; ‘car_detail’, is initalized which includes several Key-Value pairs.  Line 4 ‘car_detail.update(kwargs)’ updates the ‘car_detail’ Dictionary with additional optional arguments present in each car instance. The last section of the function, returns the program back to the ‘car_detail’ dictionary. 
The Second Part the Program on Lines 8, 13, & 18 begins the several car instances. Each  Instance starts by defining the instances; using the ‘car_dictionary’ function. Every instance includes the Required Parameters for the ‘car_dictionary’ function, and optional arguments; which are Collected with use of the ‘**kwargs’ function. 
The final section of the Car Dictionary Program is the output; which uses several ‘print’ statements, that are stored in the ‘car_dictionary’. For each instance a ‘print’ statement, prints a header; which includes the Cars Manufacturer and Model. Followed by a second ‘print’ statement, which prints all details of the car’s instance from the ‘car_dictionary’. 

# (PDL) Program Design Language:
●	FUNCTION ‘car_dictionary’ WITH PARAMETERS ‘manufacturer’, ‘model’, ‘color’, ‘year’, **kwargs
○	SET ‘car_detail’ TO A NEW Dictionary WITH ‘Manufacturer’, ‘Model’, ‘Color’, ‘Year’ KEYS AND CORRESPONDING VALUES
●	UPDATE ‘car_detail’ WITH ANY ADDITIONAL KEYWORK ARGUMENTS
○	PASSED (**kwargs)
○	RETURN ‘car_detail’

●	INITIALIZE ‘car1’ BY CALLING ‘car_dictionary’ WITH PARAMETERS (‘Subaru’, ‘Outback’, ‘Blue’, 2023, fuel = ‘87 Unleaded Gasoline’, tow_package = True)
●	PRINT “\nSubaru Outback:”
●	PRINT ‘car1’

●	INITIALIZE ‘car2’ BY CALLING ‘car_dictionary’ WITH PARAMETERS (‘Jeep’, ‘Wrangler’, ‘Red’, 2015, fuel = ‘87 Unleaded Gasoline’, four_wheel_drive = True)
●	PRINT “\nJeep Wrangler:”
●	PRINT ‘car2’

●	INITIALIZE ‘car3’ BY CALLING ‘car_dictionary’ WITH PARAMETERS (‘Ferrari’, ‘LaFerrari’, ‘Ferrari Red’, 2013, fuel = ‘97 Premium Unleaded Gasoline’, turbocharged_engine = True)
●	PRINT “\nFerrari LaFerrari”
●	PRINT ‘car3’

# Pseudo Code:
●	FUNCTION ‘car_dictionary’ WITH PARAMETERS ‘manufacturer’, ‘model’, ‘color’, ‘year’, **kwargs
○	CREATE A NEW DICTIONARY AND ASSIGN IT TO ‘car_detail’
○	ADD ‘Manufacturer’, ‘Model’, ‘Color’, ‘Year’ TO ‘car_detail’ WITH CORRESPONDING VALUES
○	ADD ANY ADDITIONAL KEYWORD ARGUMENTS TO ‘car_detail’
○	RETURN ‘car_detail’

●	‘car1’ = CALL ‘car_dictionary’ WITH PARAMETERS (‘Subaru’, ‘Outback’, ‘Blue’, 2023, fuel = ‘87 Unleaded Gasoline’, tow_package = True)
●	PRINT “Subaru Outback:”
●	PRINT ‘car1’


●	‘car2’ = CALL ‘car_dictionary’ WITH PARAMETERS (‘Jeep’, ‘Wrangler’, ‘Red’, 2015, fuel = ‘87 Unleaded Gasoline’, four_wheel_drive = True)
●	PRINT “\nJeep Wrangler:”
●	PRINT ‘car2

●	‘car3’ = CALL ‘car_dictionary’ WITH PARAMETERS (‘Ferrari’, ‘LaFerrari’, ‘Ferrari Red’, 2013, fuel = ‘97 Premium Unleaded Gasoline’, turbocharged_engine = True)
●	PRINT “\nFerrari LaFerrari”
●	PRINT ‘car3’

# Flowchart: 
START PROGRAM. → Define Function: ‘car_dictionary’ → Initialize ‘car1’ → Print “Subaru Outback:” → Print ‘car1’ → Initialize ‘car2’ → Print “Jeep Wrangler:” → Print ‘car2’ → Initialize ‘car3’ → Print “Ferrari LaFerrari:” → Print ‘car3’ → END PROGRAM.

# Program Flow & Specific Algorithms:
‘car_dictionary’ is the only function called in the Car Dictionary Program. This function is called three times: to create the dictionary for the Subaru Outback, Jeep Wrangler, and Ferrari Laferrari. The ‘car_dictionary’ function creates three dictionaries with details about each card that includes both required and optional arguments. 
There are no subroutines, methods, or algorithms being called/used. However there is a keyword argument used in this function. The Argument **kwargs, updates the function when additional arguments are present by identifying, capturing and storing details as key-value pairs in a dictionary. 



# Data (INPUT/OUTPUT)
●	‘Manufacturer’: 
○	Type: String
○	Dimension: Scalar
○	Description: Name of the car manufacturer. The primary function ‘car_dictionary’ takes in this mandatory argument.
○	Range: Any string value
○	Initial Values: Argument to the ‘car_dictionary’ function
●	‘Model’:
○	Type: String
○	Dimension: Scalar
○	Description: Model name of the car. The primary function ‘car_dictionary’ takes in this mandatory argument. 
○	Range: Any string value
○	Initial Values: Argument to the ‘car_dictionary’ function
●	‘Color’: 
○	Type: String
○	Dimension: Scalar
○	Description: Color of the car. The primary function ‘car_dictionary’ takes in this mandatory argument. 
○	Range: Any string value
○	Initial Value: Argument to the ‘car_dictionary’ function
●	‘Year’: 
○	Type: Integer
○	Dimension:Scalar 
○	Description: Year of the manufacturers release of the car. The primary function ‘car_dictionary’ tkanes in this mandatory argument. 
○	Range: Any integer value
○	Initial Value: Argument to the ‘car_dictionary’ function
●	‘**kwargs’: Keyword argument representinting additional other details of the car
○	Type: Dictionary
○	Dimension: Varies; on additional other details, if any
○	Description: Keyword argument representing “Additional Other” details of the car. Identifies, captures, and stores details as key-value pairs in a dictionary. 
○	Range: Any key-value paris where keys are strings and values vairy
○	Initial Value: Dynamically populated


# Software Components: 
●	Name: ‘car_dictionary’ 
○	Class: Function Definition
○	Purpose: This function create a dictionary including mandatory arguments: manufacturer, model, color, year. With Additional key-value pairs passed as keyword arguments with the use of ‘**kwargs’
●	Name: ‘car1’, ‘car2’, ‘car3’
○	Class: Function Calls
○	Purpose: These function calls use the ‘car_dictionary’ function to create dictionaries that include details of different cars. 
●	Name: Print Statements 
○	Class: Output
○	Purpose: Displays information about each car’s specific details

# UML Class Diagram:
●	Car 
○	manufacturer: str
○	model: str
○	color: str
○	year: str
■	_ _init_ _: (manufacturer:str, model:str, color:str, year:int)
■	_ _str_ _ :str 

# Properties and Constraints:
●	Car Class Properties:
○	‘manufacturer’: Class: String, Constraints: None
○	‘model’: Class: String, Constraints: None
○	‘color’: Class: String, Constraints: None
○	‘year’: Class: Integer, Constraints: None
●	Additional Keyword Arguments:
○	‘fuel’: Class: String, Constraints: None
○	‘tow package’: Class: Boolean, Constraints: None
○	‘four-wheel drive’: Class: Boolean, Constraints: None
○	‘turbocharged engine’: Class: Boolean, Constraints: None

# Algorithms defined in Processing Logic:
There are no algorithms defined in the processing logic,  however there is a keyword argument used in this function. The Argument **kwargs, updates the function when additional arguments are present by identifying, capturing and storing details as key-value pairs in a dictionary. 



# Testing
# Input Data:
Each car data set must include: 
●	Manufacturer
●	Model
●	Color
●	Year
(Optional) Additional desired details; such as fuel type and special features
Example: Using the Ferrari LaFerrari
●	Manufacturer: Ferrari
●	Model: LaFerrari
●	Color: Ferrari Red
●	Year: 2013
●	Additional Details:
○	Fuel Type: 97 Premium Unleaded 
○	Special Feature: Turbocharged Engine

# Expected Output Data: Example: Using the Ferrari LaFerrari
{‘Manufacturer’: ‘Ferrari’, ‘Model’: ‘LaFerrari’, ‘Color’: ‘Ferrari Red’, ‘Year’: 2013, ‘Fuel’: ‘97 Premium Unleaded’, ‘Turbocharged Engine’: True}


# Success Criteria: 
●	The program must generate several dictionaries for each car accurately; including all the mandatory information and additional optional details. 
●	The output must match each car with the expected output.
