contents = [
    "To be or not to be",
    "That is the question",
    "All the world's a stage",
    "And all the men and women merely players",
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", "w")
    file.write(content)
