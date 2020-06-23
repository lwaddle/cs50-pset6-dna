from personofinterest import PersonOfInterest
import csv

class DNAController:
    # TODO Finish the init function
    def __init__(self, data: list, dna_test_sequence: str):
        self.data = data                    # data converted from CSV reader object
        self.dna_test_sequence = dna_test_sequence  # Single DNA string
        self.people_of_interest = {}

    def get_str_criterias(self):
        """Returns a list of strings that are the STR criterias from the csv file"""
        criterias = []
        header = self.data[0]
        for col in header[1:len(header)]:
            criterias.append(col)

        return criterias

    def populate_people_of_interest(self):
        """Populate the people_of_interest dict"""
        people_of_interest = []

        for row in self.data[1:len(self.data)]:
            name = row[0]

            #person = PersonOfInterest()


    # def short_tandem_repeats(dna: str, criteria: str):
    #     """Returns the maximum number of consecutive DNA criteria repeats"""

    #     master_counter = 0

    #     for i in range(len(dna)):
    #         if dna[i : i + len(criteria)] == criteria:
    #             # Match found. Start new loop at index i and continue
    #             # until criteria is no longer consecutive. Increment master_counter
    #             # if sub_counter is greater than master_counter

    #             sub_counter = 0
    #             tmp_index = i
    #             while dna[tmp_index : tmp_index + len(criteria)] == criteria:
    #                 sub_counter += 1
    #                 tmp_index += len(criteria)

    #             if sub_counter > master_counter:
    #                 master_counter = sub_counter
    #     return master_counter