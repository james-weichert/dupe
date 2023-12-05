# Read prompts from text file

with open('/dupe/prompts.txt', 'r') as file:
    data = file.read().splitlines()

prompts = [line for line in data]
print(prompts)