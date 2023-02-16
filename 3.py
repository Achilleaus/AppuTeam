from nltk.stem import SnowballStemmer, LancasterStemmer;

snowball = SnowballStemmer(language='english');
lancaster = LancasterStemmer();

words = ['generous', 'generate', 'generously', 'generation'];

print("-----Snowball Stemmer-----")
for word in words:
    print(word, "-->", snowball.stem(word));

print("-----Lancaster Stemmer-----")
for word in words:
    print(word, "-->", lancaster.stem(word));