# Print words with their length

s = input("Enter a string: ")

words = s.split()

print("Word\tLength")
for word in words:
    print(word, "\t", len(word))
