from personofinterest import PersonOfInterest
import csv

class DNAController:
    # TODO Finish the init function
    def __init__(self, csv_data: csv.reader, dna_test_sequence: str):
        print("DNAController created")
        print(list(csv_data))
        print(dna_test_sequence)
        foo = PersonOfInterest("Loren", {"AGATT":3})
        foo.greet()

