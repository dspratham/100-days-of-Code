'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1= name1.lower()
name2= name2.lower()

name= name1+name2

sum1 = 0
sum1+=name.count("t")
sum1+=name.count("r")
sum1+=name.count("u")
sum1+=name.count("e")

sum2 = 0
sum2+=name.count("l")
sum2+=name.count("o")
sum2+=name.count("v")
sum2+=name.count("e")

score = int(str(sum1)+str(sum2))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}.")
