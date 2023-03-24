secret_letter = "lock"
guess =  ""
guess_count = 0
limit = 3
out_of = False

while guess != secret_letter and not(out_of):
        if guess_count <= limit :
            guess = input("enter the guess")
            guess_count += 1
        else : 
              out_of = True

if(out_of):
      print("you are out of guess!")
else :
      print("you won")
print(guess_count)