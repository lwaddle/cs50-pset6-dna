from personofinterest import PersonOfInterest
import csv

class DNAController:
    def __init__(self, data: list, dna_test_sequence: str):
        self.data = data                            # data converted from CSV reader object
        self.dna_test_sequence = dna_test_sequence  # Single DNA string
        self.people_of_interest = []

    def get_str_criterias(self):
        """Returns a list of strings that are the STR criterias from the csv file"""
        criterias = []
        header = self.data[0]
        for col in header[1:len(header)]:
            criterias.append(col)

        return criterias

    def populate_people_of_interest(self):
        """Populate the people_of_interest dict"""
        criterias = self.get_str_criterias()        # List of the criterias ie 'AAGTC'

        for row in self.data[1:]:                   # Excluding the header in row 0
            name = row[0]
            str_values = row[1:]                    # Just the STR values for each row. Need to associate them with a criteria like 'ATTAG'
            sequences = {}                          # Populate with {criteria: value} ie: {"AAGTC": 12, "GAAAT": 3}

            for i in range(len(str_values)):
                sequences[criterias[i]] = int(str_values[i])    # Cast int because it was stored as str

            person = PersonOfInterest(name, sequences)
            self.people_of_interest.append(person)

    def print_people_of_interest(self):
        for p in self.people_of_interest:
            p.greet()

    def short_tandem_repeats(self, dna: str, criteria: str):
        """Returns the maximum number of consecutive DNA criteria repeats"""

        master_counter = 0

        for i in range(len(dna)):
            if dna[i : i + len(criteria)] == criteria:
                # Match found. Start new loop at index i and continue
                # until criteria is no longer consecutive. Increment master_counter
                # if sub_counter is greater than master_counter

                sub_counter = 0
                tmp_index = i
                while dna[tmp_index : tmp_index + len(criteria)] == criteria:
                    sub_counter += 1
                    tmp_index += len(criteria)

                if sub_counter > master_counter:
                    master_counter = sub_counter
        return master_counter

    def match(self):
        """Returns match from data or invalid if not found"""
        # Make a tmp dict using the using the test sequence. Once it's populated
        # compare it to each from the database

        test_subject = {}

        for criteria in self.get_str_criterias():
            test_subject[criteria] = self.short_tandem_repeats(self.dna_test_sequence, criteria)

        for person in self.people_of_interest:
            if person.str_values.items() == test_subject.items():
                return person.name
                break
        
        return "No match."