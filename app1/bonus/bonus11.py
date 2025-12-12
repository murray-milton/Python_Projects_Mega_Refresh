try:
    width = float(input("Enter width e.g. 22.7: "))
    length = float(input("Enter length e.g. 10.5: "))

    if width == length:
        exit("That appears to be a square.")

    area = width * length
    print(f"Area of rectangle is {area} sq. units")
except ValueError:
    print("Invalid input. Please try again.")
