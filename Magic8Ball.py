#Magic8Ball.py
#Name: Jack Schulz
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  question = input("What is your yes or no question?: ")
  answers = ["As I see it, yes.", "Ask again later", "Better not tell you now.", "Cannot predict now.",
              "Concentrate and ask again.", "Don't count on it", "It is certain.", "It is decidedly so.",
               "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.",
               "Outlook good.", "Reply hazy, try again", "signs point to yes", "very doubtful",
                "without a doubt", "yes.", "yes - definitely", "You may rely on it."]

  #Answer question randomly with one of the options from your earlier list.
  length = len(answers) 
  r = random.random() * length
  r = int(r)
  response = answers[r]
  print(response)
 

if __name__ == '__main__':
  main()
