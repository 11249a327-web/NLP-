import nltk
from nltk.tokenize import word_tokenize
sentence = input("enter a sentence:")
tokens = word_tokeenize(sentence)
tagged_words = nltk.pos_tag(tokens)
grammer = r"""
NP: {<DT>?<JJ>*<NN.*>+}
VP: {<VB>*><DT>?<JJ>*<NN>*>+}
"""
chunker = nltk.RegrexParser(grammer)
chunk_tree = chunker.parse(tagged_words)
print("\nPOS Tagged sentence")
print(tagged_words)
print("\nChunk tree")
print(chunk_tree)
chun_tree.draw()
