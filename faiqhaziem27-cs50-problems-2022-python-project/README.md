Contact & Log Data Harvester
Video Demo: https://youtu.be/kOqqnzP5RWw
What is this project?
This is a command-line tool I built in Python to help pull and clean up contact information (like names, emails, and phone numbers) from messy text files and spreadsheets.

When working with data, contact details are often scattered across random places like chat dumps, server logs, or unformatted text files. Instead of manually copying and pasting everything, this tool automatically scans those files, cleans up the mess, checks that the information is valid, and saves everything neatly into a single CSV file.

Key Features
Supports .txt and .csv files: Automatically checks the file type you feed into it and handles the data accordingly.

Smart Text Parsing: Uses regular expressions (regex) to find names, emails, and phone numbers even inside messy text notes.

Ignores Extra Noise: Filters out common text like "Hello Team" or "Good Morning" so it only grabs actual contact details.

Handles Missing Data: If a contact is missing an email or phone number, it fills in "N/A" or "Unknown" so the output file stays neat and aligned.

Exports to CSV: Saves all valid contacts directly into a clean spreadsheet format.

How the Code is Built
project.py: The main Python script.

Uses a class called ContactManager to store and manage the contacts.

Uses @property to quickly filter valid contacts.

Handles reading .csv and .txt files, validating the data, and writing the final CSV file.

test_project.py: Contains unit tests using pytest to make sure the file reading, parsing, and writing functions work as expected.

requirements.txt: Lists the external library needed (pytest).

How to Install and Run
Prerequisites
Make sure you have Python 3 installed on your computer.

1. Install Dependencies
Open your terminal in the project folder and run:
pip install -r requirements.txt

2. Run the Program
You can run the script by passing an input file and an output file name in the terminal:

To clean a messy text file:
python project.py sample.txt output.csv

To filter a spreadsheet file:
python project.py sample.csv output.csv

3. Run the Unit Tests
To verify that all the tests pass:
pytest test_project.py
