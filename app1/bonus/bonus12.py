def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    temperatures = data[1:]
    temperatures = [float(i) for i in temperatures]
    average = sum(temperatures) / len(temperatures)
    return round(average)


temp_average = get_average()
print(temp_average)
