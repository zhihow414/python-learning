# deep.py

# Prompt the user for input
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Normalize the input: remove leading/trailing spaces and convert to lowercase
normalized = answer.strip().lower()

# Check if the input matches any of the accepted answers
if normalized == "42" or normalized == "forty-two" or normalized == "forty two":
    print("Yes")
else:
    print("No")
