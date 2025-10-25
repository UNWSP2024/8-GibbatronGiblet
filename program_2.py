# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    index = 0
    for char in sentence:
        if char.isupper() and index > 0:
            processed_str = sentence[:index]  # exclusive ending
            space_fodder = sentence[index - 1]
            edit_str1 = sentence[index - 1:]
            edit_str2 = edit_str1.replace(space_fodder, " ", 1)
            sentence = processed_str + edit_str2
            print(sentence)
            if char == "I":
                count = index + 1
                if sentence[count].islower():
                    first_letter = sentence[0]
                    sentence = sentence.replace(char, char.lower())
                    # sentence = sentence.replace(first_letter, first_letter.upper(), 1)
                elif sentence[count] == "'" or sentence[count].isupper():
                    pass
            else:
                first_letter = sentence[0]
                sentence = sentence.replace(char, char.lower())
                # sentence = sentence.replace(first_letter, first_letter.upper(), 1)
                print(sentence)
            index += 2
        else:
            index += 1




    new_sentence = sentence
    return new_sentence

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)

#This program was written by Logan Gibson on 10/24/25
#Its name is "Camel Case Converter"