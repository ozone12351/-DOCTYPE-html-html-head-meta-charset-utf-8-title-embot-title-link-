from itertools import combinations

def find_the_combo(numbers):
    for combo in combinations(numbers, 7):
        if sum(combo) == 100:
            return combo
    return None


def check_range(numbers):
   for num in numbers:
      if not (1 <= num <= 99):
         return False
   return True

if __name__ == '__main__':
   in_num = []
   print("Welcome to combo finder!")

   run = 0
   while run == 0:
      in_num.clear()
      in_num.append(int(input("Please enter 1 number:")))
      in_num.append(int(input("Please enter 2 number:")))
      in_num.append(int(input("Please enter 3 number:")))
      in_num.append(int(input("Please enter 4 number:")))
      in_num.append(int(input("Please enter 5 number:")))
      in_num.append(int(input("Please enter 6 number:")))
      in_num.append(int(input("Please enter 7 number:")))
      in_num.append(int(input("Please enter 8 number:")))
      in_num.append(int(input("Please enter 9 number:")))

      if check_range(in_num):
         result = find_the_combo(in_num)
         if result:
            print("Combination found:", result)
         else:
            print("No combination found.")
         con = input("Do you want to find new combo? (y/n)")
         if con == "y" or con == "Y" or con == "yes" or con == "Yes":
            run = 0
         elif con == "n" or con == "N" or con == "no" or con == "No":
            print("Thankyou for finding combo with us!")
            run = 1
            break
         else:
            print("Please select y for yes or n for no")
            print("if you wish to continue please rerun the program")
            print("Thankyou!")
            run = 1
            break
      else:
         print("Please enter number from 1 - 99 only.")
         run = 0
