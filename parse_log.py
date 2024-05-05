# works in newer versions of python; copy output logs over

import re

def parse_time_costs(file_path):
    try:
        with open(file_path, 'r') as file:
            log_content_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

    for line in log_content_lines:
        print(len(line))

log_file = "output_cifar_3.log"
time_costs = parse_time_costs(log_file)

if time_costs:
    print("Time costs found in the log file:")
    for cost in time_costs:
        print(cost)
else:
    print("Time cost string not found in the log file.")