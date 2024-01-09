#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_letter = sentence[0]
    if not sentence:
        result = (length, "None")
        return result
    else:
        result = (length, first_letter)
        return result

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
