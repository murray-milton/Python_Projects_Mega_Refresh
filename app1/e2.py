import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter city: ")


for row in data[1:]:
    print(row)
    if row[0] == city:
        print(row[1])


# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
#
# print(card_deck.pop())
# hand = []
#
# while sum(hand) <= 17:
#     hand.append(card_deck.pop(0))
#
# print(hand)
