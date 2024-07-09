print("The Love Calculator is calculating your score...")
name1 = input("Your name: ")
name2 = input("Your partner's name: ")
combined_name=name1+name2
lower_comb= combined_name.lower()
t=lower_comb.count("t")
r=lower_comb.count("r")
u=lower_comb.count("u")
e=lower_comb.count("e")
first_digit= t+r+u+e

l=lower_comb.count("l")
o=lower_comb.count("o")
v=lower_comb.count("v")
e=lower_comb.count("e")

second_digit=l+o+v+e

score=int(str(first_digit)+str(second_digit))

if(score<=10 or score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
