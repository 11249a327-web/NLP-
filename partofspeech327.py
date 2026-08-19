import nltk
from nltk.tokenize import word_tokenize
sentence = input("enter a sentence:")
words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("\nWord\t\POS_Tag")
print("-" * 30)
for word, tag in pos_tags:
    print(f"{word}\t\t{tag}")
