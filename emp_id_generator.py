# Write a function generate_ids(names: list[str]) -> list[str] that generates an ID for each employee in the following format:
# "EMP_" + first letter of first name + full last name + "_" + 3-digit serial (starting from 1)
# Format all names to uppercase in the ID.

def generate_id(list):
    res = []
    for i,emp in enumerate(list):
        first,last = (str.split(emp))
        res.append("EMP_" + first[0] + last.upper() + "_" + str(i+1).zfill(3))
    return res

print(generate_id(["John Doe", "Lisa Ray"]))
# output: ["EMP_JDOE_001", "EMP_LRAY_002"]