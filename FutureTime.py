#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  

  #TODO:
  #Ask user for hours
  givenHours = input("Enter a number of hours: ")
  #Ask user for minutes
  givenMinutes = input("Enter a number of minutes: ")
  moreMins = int(givenMinutes)
  moreHours =int(givenHours)
  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  totalfutureHours= currentHour + extraHour + moreHours

  clockHours = (totalfutureHours) % 24

  futureMinsStr = str(futureMins)
  futureHoursStr = str(clockHours)

  print("In " + str(givenHours) + " hours and " + str(givenMinutes) + " minutes, the time will be: " + futureHoursStr + ":" + futureMinsStr)
  

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
