import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
text = "What is the question"
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)
filtered_sentence = []
for word in words:
    if word.lower() not in stop_words:
        filtered_sentence.append(word)
print("Original sentence:", text)
print("Filtered words:", filtered_sentence)
