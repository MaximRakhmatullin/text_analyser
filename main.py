import string

text = input("Введите текст: ")
text = text.lower()
word_frequency = {}

punctuation = string.punctuation
# print(punctuation)

for symbol in punctuation:
    text = text.replace(symbol, ' ')

words = text.split()
print(words)

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Количество разных слов:", len(word_frequency))
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")