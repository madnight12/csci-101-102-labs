# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 12 - Utility using Git and Incremental Development
# References: No one
# Time: 50 minutes

# load_file function
def load_file(file_name):
    with open(file_name, 'r') as f:
        read_file = f.read().splitlines()
        output = []
        for line in read_file:
            output.append(line)
    return output

# update_string funcntion
def update_string(some_string_1, some_string_2, index):
    new_string = some_string_1.replace(some_string_1[index + 1], some_string_2)
    print('OUTPUT', new_string, end = '')
