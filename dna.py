from sys import argv
from sys import exit
import csv
from dnacontroller import DNAController

def main():
    # Check for valid command line args
    check_args()

    # Get database in csv format from crime lab
    data = convert_data()

    # Get main test sequence submitted from crime lab
    # Example: 'TAAGTTTGTGAGTTAAATAG'
    dna_test_sequence = get_dna_test_sequence()

    # Create the DNAController object
    dna_controller = DNAController(data, dna_test_sequence)
    
    # Populate the controller
    dna_controller.populate_people_of_interest()
    
    # Print result
    print(dna_controller.match())

def check_args():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    
    # TODO
    # Continue checking for more crieteria. Are the file types correct?
    # The DNAController object will further check for correct data stucture.

def convert_data():
    """Returns a list of the csv data"""
    with open(argv[1], "r", newline='') as f:
        if f.readable():
            data = []
            for row in iter(csv.reader(f)):
                data.append(row)
            
            return data
        else:
            print("Invalid csv file.")
            exit(1)

def get_dna_test_sequence():

    with open(argv[2], "r", newline='') as f:
        if f.readable():
            return f.read()
        else:
            print("Invalid DNA sequence.")
            exit(1)

main()