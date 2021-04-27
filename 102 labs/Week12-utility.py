# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 12 - Utility using Git and Incremental Development
# References: No one
# Time: 50 minutes

# load_file function
def load_file(file_name):
    with open(file_name) as file:
        file_read = file.read()
        for line in file_read:
            lines = line.strip()
    return lines

