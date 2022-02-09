global five_letter_words, new_five_letter_words
#five_letter_words = ['wordl','sense','paint','sande','lover','thame','shame']


# best_word = 'tareu'
# wrdle_word = 'blame'

def split(word):
    return [potato for potato in word]

def word_chosen(best_word, wrdle_word, five_letter_words):
    global coincided_letters, coincided_letters_position, no_coincided_letters, no_coincided_letters_position, new_five_letter_words
    letter_best_word = split(best_word)
    letter_wordl_word = split(wrdle_word)

    coincided_letters = list(set(letter_best_word) & set(letter_wordl_word))
    coincided_letters_position = [i if i == j else 0 for i, j in zip(letter_best_word, letter_wordl_word)]
    no_coincided_letters = list(set(letter_best_word) - set(letter_wordl_word))
    no_coincided_letters_position = [i if i != j else 0 for i, j in zip(letter_best_word, letter_wordl_word)]

    print('coincided_letters', coincided_letters)
    print('no_coincided_letters', no_coincided_letters)
    print('coincided_letters_position',coincided_letters_position)
    print('no_coincided_letters_position', no_coincided_letters_position)

    new_dict = word_validation(five_letter_words)
    return new_dict


def word_validation(five_letter_words):
    global new_five_letter_words
    new_five_letter_words=[]
    for wordi in five_letter_words:

        wordi_split = split(wordi)
        if not (list(set(wordi_split) & set(no_coincided_letters))): #If wordi_split has not excluded letters, go on
                # print('First statement passed', wordi)
                if list(set(coincided_letters)): #If there is coincided letters, go on
                    # print('Second statement passed', wordi)
                    # print('(list(set(coincided_letters) & set(wordi_split)))', (list(set(coincided_letters) & set(wordi_split))))
                    # print('list(set(coincided_letters))', list(set(coincided_letters)))
                    if ((list(set(coincided_letters) & set(wordi_split)))==list(set(coincided_letters))): #If wordi_split has included letter, go on
                        # print('Third statement passed', wordi)
                        if ([i if i == j else 0 for i, j in zip(wordi_split, coincided_letters_position)]==coincided_letters_position): #If there is coincided letters in position, go on
                            # print('Forth statement passed',wordi)
                            if len(set([i if i == j else 0 for i, j in zip(wordi_split, no_coincided_letters_position)]))<2:
                                new_five_letter_words.append(wordi)
                    no_coincided_letters_position
                else:
                    # print('Else statement passed', wordi)
                    new_five_letter_words.append(wordi)
    return new_five_letter_words

