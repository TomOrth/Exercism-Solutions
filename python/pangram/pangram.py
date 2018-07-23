def is_pangram(sentence):
    if sentence == '': return False
    ascii_chars = [0] * 26
    sentence = sentence.lower()
    for char in sentence:
        if ord(char) >= ord('a'):
            ascii_chars[ord(char)-ord('a')] = 1
    sum_ascii = sum(ascii_chars)
    return sum_ascii == 26
