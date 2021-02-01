ODDELOVAC = "=" * 70

user = {
     'bob': '123',
     'ann': 'pass123',
     'mike': 'password123',
      'liz': 'pass123'
     }

print("Welcome to our text analyzing app!".center(70," "))
print(ODDELOVAC)

user_name = input("Please enter your user name: ").lower()
password = input("Please enter your password: ")
if password.isalnum():
     print("Verifing user name and password..")
else:
     print("Password needs to consist of letters and numbers, ending..")
     quit()
if user_name in user and user[user_name] == password:
     print("Verified...")
else:
     print("The user name or password are not correct, ending..")
     quit()


TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

text_choice = input("Please choose the number of the text to analyze.. 1, 2 or 3: ")

if text_choice in ('1', '2', '3'):
    print("analyzing text...")

else:
    print("You can choose only numbers 1, 2 or 3...ending")
    quit()

print(ODDELOVAC)

split_words = (TEXTS[int(text_choice) - 1]).split()
number_of_words = len(split_words)
print(f"There are {number_of_words} words in the selected text.")

titlecased = 0
count1 = 0
count2 = 0
numeric = 0
sum_of_numbers: int = 0

for i in split_words:
    if (i.istitle()):
        titlecased = titlecased + 1
    elif (i.islower()):
        count1 = count1 + 1
    elif (i.isupper()):
        count2 = count2 + 1
    elif (i.isnumeric()):
        numeric = numeric + 1
        if i.isnumeric():
            sum_of_numbers = (int(i)) + sum_of_numbers

print(f"There are {titlecased} titlecase words.")
print(f"There are {count1} lowecase words.")
print(f"There are {count2} uppercase words.")
print(f"There are {numeric} numeric words.")
print(f"If we summed up all the numbers in this text we would get: {sum_of_numbers}.")

print(ODDELOVAC)

striped_words = []
for word in split_words:
    clear_words = len(word.strip("., "))
    striped_words.append(clear_words)

occurence = {}
for word in striped_words:
    if word not in occurence:
        occurence[word] = 1
    else:
        word in occurence
        occurence[word] += 1

for x,y in occurence.items(): print(x, y * '*', y)
