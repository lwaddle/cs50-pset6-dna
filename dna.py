from sys import argv
from sys import exit
import csv
import dnahelpers

def main():
    
    dna_test_squence = ''           # DNA to be tested. Consider this the sample from a crime scene
    
    
    # Check for valid arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Get the csv
    with open(argv[1], newline='') as f:
        csv_reader = csv.reader(f)
        # data_list = list(csv_reader)
        
    # Get the DNA string
    with open(argv[2]) as f:
        dna_test_squence = f.read()        # Read the sequence

    dnahelpers.greet('Loren')

main()