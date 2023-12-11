
def christmasTreeCreator(num):
   i = 0
   while i < num:
      print("    ^    ", end='')
      i+=1
   print("")
   i=0
   while i < num:
      print("   /*\\   ", end='')
      i += 1
   print("")
   i = 0
   while i < num:
      print("  /***\\  ", end='')
      i += 1
   print("")
   i = 0
   while i < num:
      print(" /*****\\ ", end='')
      i += 1
   print("")
   i = 0
   while i < num:
      print("/*******\\", end='')
      i += 1
   print("")
   i = 0


if __name__ == '__main__':
   num_str = input("Please enter how many Christmas Tree you want:")
   num = int(num_str)
   run = 1
   while run == 1:
      christmasTreeCreator(num)
      con = input("Do you wish to continue? (y/n)")
      if con == "y" or con == "Y" or con == "yes" or con == "Yes":
         num_str = input("Please enter how many Christmas Tree you want:")
         num = int(num_str)
      elif con == "n" or con == "N" or con == "no" or con == "No":
         print("Thankyou for printing christmas tree with us!")
         run = 0
         break
      else:
         print("Please select y for yes or n for no")
         print("if you wish to continue please rerun the program")
         print("Thankyou!")
         run = 0
         break