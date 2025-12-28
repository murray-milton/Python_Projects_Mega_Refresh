# Method 1: Using a for loop to create a set of counters


book_title = [
    "great",
    "expectations",
    "the",
    "adventures",
    "of",
    "sherlock",
    "holmes",
    "the",
    "great",
    "gatsby",
    "hamlet",
    "adventures",
    "of",
    "huckleberry",
    "fin",
]
word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# Method 2: Using the get method
book_title_2 = [
    "great",
    "expectations",
    "the",
    "adventures",
    "of",
    "sherlock",
    "holmes",
    "the",
    "great",
    "gatsby",
    "hamlet",
    "adventures",
    "of",
    "huckleberry",
    "fin",
]
word_counter_2 = {}

for word in book_title:
    word_counter_2[word] = word_counter_2.get(word, 0) + 1

print(word_counter_2)
