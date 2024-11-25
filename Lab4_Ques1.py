# Find the number of palindrome words in the given sentence without defining any new function (feel free to use python’s in-built functions).

# ----------------------------------CODE-------------------------------

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

palindrome_count = sum(1 for word in words if word == word[::-1])

print(f"The number of palindrome words in the sentence: {palindrome_count}")
