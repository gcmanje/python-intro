#strings
sentence= "The quick brown fox jumps over the lazy dog"
# builtin functionality
# functions
print(sentence)
print(sentence.upper()) # using builtin function is termed as call a function
print(sentence.lower())
print(sentence.title()) # jaNe njeRi ==> Jane Njeri
print(sentence.count("dog"))
print(sentence.isspace())

sentence= "ok"
if sentence.isspace() or sentence.isdigit() or sentence.isnumeric():
    print("Invalid name")
else:
    print("Valid name")
