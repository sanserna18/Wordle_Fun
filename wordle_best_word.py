import numpy as np
import pandas as pd


def split(word):
    return [potato for potato in word]

def divide_in_letters(five_letter_words):
    first_character = []
    second_character = []
    third_character = []
    forth_character = []
    fifth_character = []

    for wordi in five_letter_words:
        first_character.append(wordi[0])
        second_character.append(wordi[1])
        third_character.append(wordi[2])
        forth_character.append(wordi[3])
        fifth_character.append(wordi[4])
    return first_character, second_character, third_character, forth_character, fifth_character


def count_letter_repetition(character,list):
    global df
    unique_values = set(list)
    for i in unique_values:
        curr_frequency = list.count(i)
        to_append = [character, i, curr_frequency, None]
        df_length = len(df)
        df.loc[df_length] = to_append

# Count the repetition of letters to do a ranking per character
def give_rank_to_letters(five_characters):
    global df
    df = pd.DataFrame(columns=["Character","Letter", "Count","Rank"])
    new_dtypes = {"Count": np.float64, "Rank": np.float64}
    df = df.astype(new_dtypes)
    count_letter_repetition('first_character', five_characters[0])
    count_letter_repetition('second_character', five_characters[1])
    count_letter_repetition('third_character', five_characters[2])
    count_letter_repetition('forth_character', five_characters[3])
    count_letter_repetition('fifth_character', five_characters[4])

    df['Rank'] = df.groupby('Character')['Count'].rank(ascending=False)






#df = df.sort_values(by=['Character','Count'], ascending = False).groupby('Character')
#print('df-->',df)

# words_to_check = ['wordl','cleve','fanee','apple']

def word_ranked(five_letter_words):
    df_points = pd.DataFrame(columns=["Word", "Points"])

    for potato in five_letter_words:
        first_value = df.loc[(df["Letter"] == potato[0]) & (df["Character"] == "first_character")]["Rank"].values[0]
        second_value = df.loc[(df["Letter"] == potato[1]) & (df["Character"] == "second_character")]["Rank"].values[0]
        third_value = df.loc[(df["Letter"] == potato[2]) & (df["Character"] == "third_character")]["Rank"].values[0]
        forth_value = df.loc[(df["Letter"] == potato[3]) & (df["Character"] == "forth_character")]["Rank"].values[0]
        fifth_value = df.loc[(df["Letter"] == potato[4]) & (df["Character"] == "fifth_character")]["Rank"].values[0]

        points = first_value + second_value + third_value + forth_value + fifth_value
        to_append = [potato, points]
        df_length = len(df_points)
        df_points.loc[df_length] = to_append
    print(df_points)
    print(df_points.loc[df_points['Points'] == df_points['Points'].min()])
    return (df_points.loc[df_points['Points'] == df_points['Points'].min()]).iloc[0,0]

 #print(df_points['Word'].where(df_points['Points'] == df_points['Points'].min()))
   # return df_points

def find_best_word(five_letter_words):
    # Divide all words in letters and position
    five_characters = divide_in_letters(five_letter_words)

    # Give ranking to every letter
    give_rank_to_letters(five_characters)

    # Rank every word
    best_words = word_ranked(five_letter_words)

    return best_words