# /c:/Users/Mounika/zkiran_latest_Rep/01/string.py

# crow_story = (
#     "Once upon a time, a clever crow was very thirsty. "
#     "It found a pot with a little water at the bottom. "
#     "The crow dropped stones into the pot, one by one, "
#     "and the water rose high enough for it to drink. "
#     "The crow learned that patience and thinking can solve hard problems."
# )

# print(crow_story)
# word = "crow"
# count = crow_story.lower().split().count(word)
# /c:/Users/Mounika/zkiran_latest_Rep/01/string.py

# Define a multi-line string variable containing the crow story
# Define the story about the crow as a multi-line string
crow_story = (
    "Once upon a time, a clever crow was very thirsty. "
    "It found a pot with a little water at the bottom. "
    "The crow dropped stones into the pot, one by one, "
    "and the water rose high enough for it to drink. "
    "The crow learned that patience and thinking can solve hard problems."
)

# Replace all "crow" words with "kiran" and save the new story
modified_story = crow_story.replace("crow", "kiran")

# Show the story with "kiran" instead of "crow"
print(modified_story)

# Show the whole story in all lowercase letters
print(crow_story.lower())

# Show the whole story in all uppercase letters
print(crow_story.upper())

# Break the story into a list of individual words
words = crow_story.split()

# Go through the list of words, taking two at a time
for i in range(0, len(words), 2):
    # Get the first word in the pair
    word1 = words[i]
    # Get the second word if there is one, otherwise use nothing
    word2 = words[i+1] if i+1 < len(words) else ""
    # Print both words side by side
    print(word1, word2)
