pangram = "The quick brown fox jumped over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

another_pangram = sorted("The quick brown fox jumps over the lazy dog",
                         key=str.casefold)
print(another_pangram)

name = ["Rupam",
        "Subho",
        "purba",
        "Srijita",
        "soumo"
        ]

name.sort(key=str.casefold)
print(name)

