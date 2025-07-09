import string
s = "The quick brown fox jumps over a lazy dog"
if set(string.ascii_lowercase) <= set(s.lower()):
    print("Pangram")
else:
    print("Not a Pangram")
