import random
import math

low = int(input("enter the lowest number\n"));
high = int(input("enter the highest number\n"));

x = random.randint(low, high);
print("you have only",round(math.log(high - low + 1, 2)),"chances to guess the number\n");
count = 0;

while count < math.log(high - low +1, 2) :

    count += 1;

    guess = int(input("guess the number\n"));

    if x == guess:

       print("congratulations you have in ",count,"guess");

       break;
    elif x > guess :
        print("you guess too small");

    elif x < guess :
        print("you guess too high");

if count >= math.log(high - low +1,2) :
    print("the number is %d",x);
    print("better luck next time");
