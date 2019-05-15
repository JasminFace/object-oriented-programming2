#EXERCISE 1
def sum_of_odd(numbers):
    sum = 0
    for num in numbers:
        if num % 2 !=0:
            sum += num
        else:
            None
    return sum

print(sum_of_odd(range(1,11)))

#EXERCISE 2
names = ["Jeannine", "Dylan", "Mollin"]

def person(your_name):
    if your_name in names:
        print(f"Sup {your_name}.")
    else:
        print("Who goes there?")

print("Enter your name please")
your_name = input()
person(your_name)
