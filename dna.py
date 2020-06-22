from sys import argv
from sys import exit
import csv

def main():
    
    # Old code    
    # # Get the DNA string
    # with open(argv[2]) as f:
    #     dna_test_squence = f.read()        # Read the sequence

    dna_test_sequence = get_dna_test_sequence()

    # TODO
    # Create the DNAController object


def check_args():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    
    # TODO
    # Continue checking for more crieteria. Are the file types correct?
    # The DNAController object will further check for correct data stucture.

def get_dna_test_sequence():

    check_args()

    with open(argv[2], "r", newline='') as f:
        if f.readable():
            return f.read()
        else:
            print("Invalid DNA sequence.")
            exit(1)

main()