from textblob import TextBlob
a = TextBlob("Today was a raeny daay and I had caake and biskiuts.")
a = a.correct()
print(a)

