from string import punctuation as p
from typing import Optional


def reverse(input: str) -> str:
    result = ""
    punctuations = []
    split_input = input.split(" ")

    for i in split_input:
        punctuation = get_punctuation(i)
        if punctuation != None:
            punctuations.append(punctuation)

    index = 0

    split_input_length = len(split_input)

    for i in reversed(range(split_input_length)):
        word = split_input[i]
        punctuation = get_punctuation(word)

        if i>0 and get_punctuation(split_input[i-1]) != None:
            if i== split_input_length-1 and punctuation != None:
                result += f" {word[:-1]}{punctuations[index]}"
            else:
                 result += f" {word}{punctuations[index]}"
            index += 1
        elif punctuation != None:
            result += f" {word[:-1]}"
        else:
            result += f" {word}"
        
    if index != len(punctuations):
        result += punctuations[-1]

    return result

def get_punctuation(input: str) -> Optional[str]:
    last_char = input[-1]
    if p.__contains__(last_char):
        return last_char

if __name__ == "__main__":
   print(reverse("Hello. I'm Edwin A.J, and you?"))
   print(reverse("What time is it? Hammer time."))
   print(reverse("What time is it? Hammer time. hehehe"))

