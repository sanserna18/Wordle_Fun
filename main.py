from wordle_best_word import *
from reduce_dictionary import *
import os


global new_five_letter_words, new_dict, my_word, wordl_right_word
path = r'C:\Users\sanse\PycharmProjects\Wordle_Fun\Word lists in csv'  # use your path

my_word = 'crane'
wordl_right_word = 'frame'

## Export five letter words, there are some issues with the csv so we can't used pandas
five_letter_words = []
#five_letter_words = ['wordl','sense','paint','sande','lover','thame','shame','blame','vlame']
for filei in os.listdir(path):

    with open(filei, encoding="utf8", errors='ignore') as f:
        for wordi in f.readlines():
            wordi = wordi.strip()
            if len(wordi) == 5 and wordi.isalnum():
                five_letter_words.append(wordi)

# Eliminate duplicates
five_letter_words = list(dict.fromkeys(five_letter_words))
print('five_letter_words COUNT--->', len(five_letter_words))

five_letter_words = word_chosen(my_word, wordl_right_word, five_letter_words)

print('five_letter_words COUNT 2--->', len(five_letter_words))

def party_rock(five_letter_words):
    for potato in range(6):
        print('five_letter_words_FIRST--->', five_letter_words)
        best_words = find_best_word(five_letter_words)
        print('best_words', best_words)
        if best_words == wordl_right_word:
            print('rounds-->', potato + 2)
            break

        else:
            five_letter_words.remove(best_words)
            print('five_letter_words removed--->', five_letter_words)
            five_letter_words = word_chosen(best_words, wordl_right_word, five_letter_words)
            print('five_letter_words_SECOND--->', len(five_letter_words))
            print('five_letter_words_SECOND--->', five_letter_words)


    print('rounds-->', potato + 2)


party_rock(five_letter_words)






