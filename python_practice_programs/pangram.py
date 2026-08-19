#pangram program
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    for char in s:
        if char in alphabet:
            alphabet.remove(char)
    return len(alphabet) == 0   
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram.")         