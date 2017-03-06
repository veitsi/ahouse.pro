The goal of this exercise is to understand what you consider production-quality code with a small set of requirements.

The application will be run from the command-line and take as a command-line argument the path to a csv file. The csv file is expected to have the following field layout:
fbid - integer
token - string
username - string

Example:
90409536523418567,EAAT2K6PlqfMBAIicutagzk,Erin Little
1015404977861488,EAAT2K6PlqfMBAAzO6ws,Matan Ami

The program should calculate the approximate date of the user registration in Facebook for each record from the csv file.

The output of the program should be written to the console with the following format:
username,fbid,registration_date. registration_date mask - %Y-%m-%d

Example output:
Erin Little,90409536523418567,2012-09-23
Matan Ami,1015404977861488,2016-05-07

Requirements:
- python 3 (preferably 3.5)
- input csv file can contains large dataset
- cover code with some level of unit testing. No need to cover all the code, just show ability to write good and well maintainable unit tests

If you use any 3rd party library, please specify which version you are using.