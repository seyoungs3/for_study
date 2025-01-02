words = input().upper()

unique_words = list(set(words))


number = []
for i in unique_words:
    number.append(words.count(i))

if number.count(max(number)) > 1:
    print('?')
else:
    max_index = number.index(max(number))
    print(unique_words[max_index])