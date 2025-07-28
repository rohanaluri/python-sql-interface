# python-sql-interface

Application setup:

1- Install PyQt6
Run the following command on the terminal: pip install PyQt6
For more information, visit: https://pypi.org/project/PyQt6/

2- Install PyMySQL
Run the following command on the terminal: python3 -m pip install PyMySQL
Note: this is an optional package, but the GUI won't run without it
For more information: https://pypi.org/project/pymysql/

3- Update the database connection password
In the connection.py file, the connection to the database is made. For this connection to be successful, it needs some information. Most of that information is already filled out, but the password has to change because it's different on every machine. All you need to do is type your Workbench password in line 7, and assign the self.password variable a string containing your password.

Running the application and Technologies Used: Run the main.py file using whatever IDE you have. We used PyQt6 to make the GUI. Like many frontend technologies, PyQt6 is object-oriented. For each element on the screen, we create an object and call different functions on it. To make the application fucntion properly, we connect certain user actions with behaviors. We also used PyMySQL to connect our python script to the database, so that once we get the outcome of a query stored as a python variable, we can do whatever we want with it on python.

File Contents:

- main.py: Initializes and runs a GUI for the SImple Airline Management System. Provides users with the ability to engage with 25+ interactive buttons connected to specific backend SQL queries like adding airplanes, offering flights, assigning pilots, etc. 
- connection.py: Defines a MySQL context manager class that establishes a connection with the flight management MySQL database.
- queries.py: Defines the backend logic for each GUI button by connecting user inputs with corresponding MySQL stored procedures. Retrieves dropdown options from the database, such as airline ID's or location ID's, and handles data validation. 
