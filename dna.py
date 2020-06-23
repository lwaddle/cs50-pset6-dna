from sys import argv
from sys import exit
from csv import reader
from dnacontroller import DNAController

def main():
    # Check for valid command line args
    check_args()

    # Get database in csv format from crime lab
    csv_data = get_csv_data()

    # Get main test sequence submitted from crime lab
    # Example: 'TAAGTTTAGAATATAAAAGGTGAGTTAAATAG'
    dna_test_sequence = get_dna_test_sequence()

    # Create the DNAController object
    dna_controller = DNAController(csv_data, dna_test_sequence)

    # TODO Use controller to print result

def check_args():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    
    # TODO
    # Continue checking for more crieteria. Are the file types correct?
    # The DNAController object will further check for correct data stucture.

def get_csv_data():
    """Returns a csv reader object"""
    with open(argv[1]) as f:
        if f.readable():
            return f.read()
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