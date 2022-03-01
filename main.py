import time
import threading
from threading import Timer

#introduces variables
x = 0
action = ""
shopaction = ""
keyprice = 15
cookiemult = 1
keys = 0
keymult = 1
cookies = 0
typewriterprice = 100
typewriters = 0
typewritermult = 1



#tutorial
print("[1] to type one cookie")
print("[2] to open the shop")
print("")

#actions
while x == 0:
  print("You have " +str(cookies) + " cookies")
  print("You have " + str(keys) + " keys")
  print("You have " + str(typewriters) + " typewriters")
  action = input("What would you like to do? ")
  if action == "1":
    cookies += 1 * cookiemult
    print("")
  if action == "2":
    print("")
    print("keys are " + str(keyprice) + " cookies")
    print("typewriters are " + str(typewriterprice) + " cookies")
    print("")
    print("[1] to go back")
    print("[2] to buy one key")
    print("[3] to buy one typewriter")
    print("[4] to buy one keyboard")
    shopaction = input("What would you like to do? ")
    if shopaction == "1":
      print("")
      print("Returning to menu...")
      print("")
    if shopaction == "2":
      if cookies < keyprice:
        print("")
        print("Sorry, you do not have enough cookies")
        print("")
      else:
        cookies -= keyprice
        keys += 1
        keyprice = round(keyprice * 1.21)
        print("")
    if shopaction == "3":
      if cookies < typewriterprice:
        print("")
        print("Sorry, you do not have enough cookies")
        print("")
      else:
        cookies -= typewriterprice
        typewriters += 1
        typewriterprice = round(typewriterprice * 1.21)
        print("")
        
  if keys > 0:
    def keyproduction():
      global cookies
      cookies += keys * keymult
      print("")
      print("You now have " + str(cookies) + " cookies")
      print("")
    t = threading.Timer(5.0, keyproduction)
    t.start()

  if typewriters > 0:
    def typewriterproduction():
      global cookies
      cookies += typewriters * typewritermult
      print("")
      print("You now have " + str(cookies) + " cookies")
      print("")
    t1 = threading.Timer(1.0, typewriterproduction)
    t1.start()
