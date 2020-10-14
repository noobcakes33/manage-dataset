# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:31:14 2019

@author: harsh
"""

import csv
import unittest

class Harsh:

    file_name = 'Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv'
    def __init__(self):
        # number of records to show
        self.n_records = 10
        # making a range list of 10 records starting from index 2 in the csv file
        self.num_records = range(2, self.n_records+2)
        # reading the csv file
        with open(self.file_name, 'r', encoding="ISO-8859-1") as fp:
            reader = csv.reader(fp, delimiter=',', quotechar='"')
            #store the rows in the records list
            self.records = [row for row in reader]
        # infinite loop
        while True:
            #to show your fullname each iteration
            self.display_fullname()
            #to show the options each iteration
            self.show_options()

    def display_records(self):
        """Display number of records"""
        try:
            #num_records = range(2, num_records+2)
            print("[len records]", len(self.records))
            # displaying (num_records) records
            for j in self.num_records:
                try:
                    print((self.records[j]))
                except:
                    pass
        # handling error if the file specified is not in the directory or not spelled right
        except FileNotFoundError:
            print("[ERROR] No such file or directory. Make sure you write the file name right.")

        return self.records

    def display_fullname(self):
        """Display fullname"""
        name = "Harsh 4199" # change it to your fullname
        print("[Created by] {}".format(name))

    def create_new_record(self):
        """Create a new record and store it in the simple data structure"""
        #asks the user to enter a record (string)
        new_record = input("Enter record: (comma separated record)")
        #splits the string by comma to be in a list
        new_record = new_record.split(',')
        # 'a' for appending; to append new record to the file
        with open(self.file_name, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_record)

        #with open(self.file_name, 'r', encoding="ISO-8859-1") as inp:
        #    reader = csv.reader(inp, delimiter=',', quotechar='"')
        #    self.records = [row for row in reader]
        #self.records = self.records[2:12] + [self.records[-1]]

        #adding the record to the records already stored from idx 2 to idx 12
        self.records = self.records[2:12] + [new_record]
        print("[records] ", self.records)
        # increment the n_records by 1
        self.n_records += 1
        print("[n_records] ", self.n_records)
        # increasing the num_records range list so it can include the new record when we iterate through the records list to display the records
        self.num_records = range(2, self.n_records + 2)
        print("[num_records] ", self.num_records)

    def select_disp_edit(self):
        """Select, display and edit a record held in the simple data structure"""
        #asks the user to enter the index of record that the user wants to select
        record = input("Select record index: ")
        # reads the csv file and also creates a new one for editing
        with open(self.file_name, 'r', encoding="ISO-8859-1") as inp, open("edited_"+self.file_name, 'w') as out:
            writer = csv.writer(out)
            reader = csv.reader(inp, delimiter=',', quotechar='"')
            records = [row for row in reader]
            print(len(records))
            print("[selected record] ", records[int(record)-1])
            # asks the user to enter the edited record (string)
            edited_row = input("Enter edited record: (comma separated record)")
            # splits the string by comma to be in a list
            edited_row = edited_row.split(',')
            # stores the edited record to its own index
            records[int(record)-1] = edited_row
            # iterating through the records then writes them row by row in the output csv file after edition
            for row in records:
                writer.writerow(row)

        return records



    def delete_record(self):
        """Delete a record from the csv file"""
        # asks the user to enter the record index that the user wishes to delete
        n = int(input("Select record index to delete: "))
        # reading the csv file and creating a new csv file that doesn't contain the record deleted
        with open(self.file_name, 'r', encoding="ISO-8859-1") as inp, open("after_deletion_"+self.file_name, 'w') as out:
            writer = csv.writer(out)
            reader = csv.reader(inp, delimiter=',', quotechar='"')
            records = [row for row in reader]
            # writing all the rows in our csv file to the new csv file except for the row that we wish to delete
            for row in records:
                # keep writing the rows to the new csv file as long as the want-to-delete row index is not equal to the current index while iteration
                if n != records.index(row)+1:
                    writer.writerow(row)
                else:
                    # removes the record from the records list
                    records.pop(records.index(row))
                    print("record deleted")

        return records

    def reload_data(self):
        """restarting variables to their initial values"""
        self.__init__()


    def show_options(self):
        """Provide the user the options to choose a function"""
        print("[1] Reload data")
        print("[2] Display records")
        print("[3] Create a new record")
        print("[4] Select, display and edit a record held in the simple data structure")
        print("[5] Delete a record from the simple data structure")

        # asks the user to enter their option
        option = input("[OPTION] Please enter your option: ")
        if int(option) == 1:
            self.reload_data()
        elif int(option) == 2:
            self.display_records()
        elif int(option) == 3:
            self.create_new_record()
        elif int(option) == 4:
            self.select_disp_edit()
        elif int(option) == 5:
            self.delete_record()
        else:
            print("OPTION NOT FOUND")



class UnitTests(unittest.TestCase, Harsh):

    def testcase1(self):
        self.assertEqual(self.display_records()[2], ['Dryas integrifolia', '2016', '169', '10', '12', '0', '0', 'AF, IW', ''])



if __name__ == "__main__":
    h = Harsh()
    #unittest.main()