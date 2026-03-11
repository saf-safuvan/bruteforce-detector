log_file = input("Enter auth log file: ")

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "failed password" in line.lower():
        print("Possible brute force attempt:", line)
