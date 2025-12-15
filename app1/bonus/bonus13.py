feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_local):
    numbs = [num for num in feet_inches_local.split(" ")]
    feet = float(numbs[0])
    inches = float(numbs[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)
print(result)

if result < 1:
    print("Return when the kid is taller.")
else:
    print("Enjoy the ride!!!")
