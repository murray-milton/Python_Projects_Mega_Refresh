# """Working with dir() and help() functions"""
#
# print(dir(list))  # Will return all the methods of the class
# print(help(list))  # Will return by the corresponding help page with class
def join_numbers(odd_number: [int]) -> list[int]:
    numbers = []
    for number in odd_number:
        if number % 2 == 0:
            numbers.append(number)
    return numbers


print(join_numbers([1, 2, 3, 4, 5]))
