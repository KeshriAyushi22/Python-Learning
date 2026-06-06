name = input("enter your name: ")

print(f"Good Morning Miss, {name.upper()}") #f to make string to add dynamic value

letter = '''Dear <|Name|>
            you are selected.'''

print(letter.replace('<|Name|>', 'Moon')) #strings are immutable

letter = "Dear Ayushi Keshri, \n\tyou are earning 1cr now. \nThanks universe!"
print(letter)