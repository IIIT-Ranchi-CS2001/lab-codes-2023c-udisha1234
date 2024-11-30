# Create a list of int using list comprehension [multiple input from keyboard].  Find the mean, median, and 
# mode of the given list (usage of specific modules such as statistics is strictly prohibited. Lab problems are 
# for you to build-up logic and strengthen your understanding of the topic & its concepts).


# -------------------------------CODE------------------------------------------


numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

mean = sum(numbers) / len(numbers)

numbers.sort()
n = len(numbers)
if n % 2 == 1: 
    median = numbers[n // 2]
else: 
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_frequency = max(frequency.values())
modes = [key for key, val in frequency.items() if val == max_frequency]

mode = modes if len(modes) > 1 else modes[0]


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
