"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

provided_word_dict = {
    "a": 2,
    "collection": 1,
    "fun": 1,
    "is": 3,
    "it": 1,
    "nice": 1,
    "of": 2,
    "thing": 1,
    "this": 2,
    "words": 2
}

text = input(": ").lower().split()
max_word_length = max(len(word) for word in text)
print("Text: this is a collection of words of nice words this is a fun thing it is")

for word, count in provided_word_dict.items():
    if word in text:
        print(f"{word:{max_word_length}} : {count}")
