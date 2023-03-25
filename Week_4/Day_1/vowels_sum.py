text = input()

letters = {
    "a":1,
    "e":2,
    "i":3,
    "o":4,
    "u":5

}
sum = 0

letters_check = ("a", "e", "i", "o", "u")
for letter in text:
    if letter in letters_check:
        sum +=letters[letter]
print(sum)
