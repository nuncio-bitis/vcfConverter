#! /usr/bin/env python3
# -----------------------------------------------------------------------------

import sys
import json
import utils

# -----------------------------------------------------------------------------

ARRAY_DEL = ","
CSV_SEPARATOR = ","
PRETTY_PRINT_JSON = True
JSON_FILE = ""
CSV_FILE = ""
FILE = ""

# -----------------------------------------------------------------------------

def conv():
    contacts = []
    field_set = set([])
    with open(FILE, "r") as file:
        contacts = utils.toObj(file)

    # extract all the fields
    for contact in contacts:
        field_set |= set(contact.keys())

    field_set = sorted(field_set)

    # -----------------------------------------------------
    # Parse all contacts and generate csv

    # CSV Header
    contactsCSV = ""
    for field in field_set:
        contactsCSV += f'"{field}"{CSV_SEPARATOR}'
    contactsCSV = contactsCSV[:-1] + "\n"

    # Contact data
    for contact in contacts:
        for field in field_set:
            if field in contact:
                entry = contact[field]
                if isinstance(entry, list):
                    entry = ARRAY_DEL.join(entry)
                contactsCSV += '"' + entry.replace('"', "'") + '"'
            contactsCSV += CSV_SEPARATOR
        # trim last comma and add new line
        contactsCSV = contactsCSV[:-1] + "\n"

    # -----------------------------------------------------
    # Write to CSV file

    if CSV_FILE != "":
        with open(CSV_FILE, "w") as f2:
            f2.write(contactsCSV)
            f2.close()

    # -----------------------------------------------------
    # Write to JSON file

    if JSON_FILE != "":
        with open(JSON_FILE, "w") as f2:
            if PRETTY_PRINT_JSON:
                json.dump(contacts, f2, ensure_ascii=False, indent=2)
            else:
                json.dump(contacts, f2, ensure_ascii=False)
            f2.close()

    # -----------------------------------------------------
    # No output file specified - dump to stdout

    if CSV_FILE == "" and JSON_FILE == "":
        print(json.dumps(contacts, indent=2))

# -----------------------------------------------------------------------------

def print_help():
    print(
        """Usage: python3 vcfConvert.py <vcf_file> [options]

    By default this prints json object to stdout if  no options are specified

    Options:
    -------
    -json <name> : export to json file, must specify file name
    -csv  <name> : export to csv file, must specify file name
    """
    )
    exit(1)

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()

    FILE = sys.argv[1]
    if FILE[0] == "-":
        print_help()

    for i in range(2, len(sys.argv[2:]) + 2):
        if sys.argv[i] == "-json":
            try:
                JSON_FILE = sys.argv[i + 1]
            except:
                print_help()
        elif sys.argv[i] == "-csv":
            try:
                CSV_FILE = sys.argv[i + 1]
            except:
                print_help()
    conv()

# -----------------------------------------------------------------------------
