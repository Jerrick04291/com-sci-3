def birthyear(year):
    return year

year = int(input("Enter your birth year: "))

if year <= 0:
    print("not a true year")
elif year < 1900:
    print("your birth year must be greater than 1900")
elif year % 12 == 0:
    print("Your Chinese zodiac sign is the Monkey.")
elif year % 12 == 1:
    print("Your Chinese zodiac sign is the Rooster.")
elif year % 12 == 2:
    print("Your Chinese zodiac sign is the Dog.")
elif year % 12 == 3:
    print("Your Chinese zodiac sign is the Pig.")
elif year % 12 == 4:
    print("Your Chinese zodiac sign is the Rat. ")
elif year % 12 == 5:
    print("Your Chinese zodiac sign is the Ox.")
elif year % 12 == 6:
    print("Your Chinese zodiac sign is the Tiger.")
elif year % 12 == 7:
    print("Your Chinese zodiac sign is the Rabbit.")
elif year % 12 == 8:
    print("Your Chinese zodiac sign is the Dragon.")
elif year % 12 == 9:
    print("Your Chinese zodiac sign is the Snake.")
elif year % 12 == 10:
    print("Your Chinese zodiac sign is the Horse.")
else:
    print("Your Chinese zodiac sign is the Goat.")  # com-sci-3
main.py
