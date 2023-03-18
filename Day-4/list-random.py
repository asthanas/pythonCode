# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#Write your code below this line 👇

length=len(names)
random_choice=random.randrange(len(names))
print(random_choice)
bill_pay=names[random_choice]
print(bill_pay+ "is going to buy the meal today!" )