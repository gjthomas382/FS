import time

print(" ")
print("Pick your story, enter 1 for 'Vacation, or 2 for Party Invite")
sel = input()
sel = int(sel)
if sel == 1:
    print("adjective?")
    var1 = input()
    print("adjective?")
    var2 = input()
    print("noun?")
    var3 = input()
    print("noun?")
    var4 = input()
    print("plural noun?")
    var5 = input()
    print("game?")
    var6 = input()
    print("plural noun?")
    var7 = input()
    print("verb ending in 'ing'?")
    var8 = input()
    print("verb ending in 'ing'?")
    var9 = input()
    print("plural noun?")
    var10 = input()
    print("verb ending in 'ing'?")
    var11 = input()
    print("noun?")
    var12 = input()
    print("plant?")
    var13 = input()
    print("body part?")
    var14 = input()
    print("place?")
    var15 = input()
    print("verb ending in 'ing'?")
    var16 = input()
    print("adjective?")
    var17 = input()
    print("number?")
    var18 = input()
    print("plural noun?")
    var19 = input()

    print("Generating story........Please wait")
    time.sleep(2.5)
    print("     ")
    print("     ")
    print("-------------------------------------------------------")
    print("A vacation is when you take a trip to some ", var1, "place")
    print("with your ", var2, "family. Usually you go to some place") 
    print("that is near a/an ", var3, " or up on a/an ", var4, ".")
    print("A good vacation place is one where you can ride ", var5)
    print("or play ", var6, " or go hunting for ", var7, " . I like") 
    print("to spend my time ", var8, " or ", var9, ".")
    print("When parents go on a vacation, they spend their time eating") 
    print("three ", var10, " a day, and fathers play golf, and mothers") 
    print("sit around ", var11, ". Last summer, my little brother") 
    print("fell in a/an ", var12, " and got poison ", var13, " all") 
    print("over ", var14, ". My family is going to go to (the)") 
    print(var15, ", and I will practice ", var16, ". Parents") 
    print("need vacations more than kids because parents are always very") 
    print(var17, " and because they have to work ", var18)
    print("hours every day all year making enough ", var19, " to pay") 
    print("for the vacation")
    print("-------------------------------------------------------")

elif sel == 2:
    print("name?")
    var1 = input()
    print("adverb?")
    var2 = input()
    print("name?")
    var3 = input()
    print("theme?")
    var4 = input()
    print("place?")
    var5 = input()
    print("day of the week?")
    var6 = input()
    print("time?")
    var7 = input()
    print("verb?")
    var8 = input()
    print("animal?")
    var9 = input()
    print("body part?")
    var10 = input()
    print("contact information?")
    var11 = input()
    
    print("Generating story........Please wait")
    time.sleep(2.5)
    print("     ")
    print("     ")
    print("-----------------------------")
    print("Dear ", var1, ",")
    print("You are", var2, "invited!!!")
    print("-----------------------------")
    print("IT'S TIME FOR A PARTY!!!")
    print("-----------------------------")
    print(" ")
    print("----------------------------------------------")
    print(var3, "is having a ", var4, "party!")
    print("It's going to be at ", var5, "on ", var6, ".")
    print("Please make sure to show up at ", var7, "or else")
    print("you will be required to ", var8)
    print("a/an ", var9, "with your ", var10)
    print(" ")
    print("RSVP at ", var11)
    print("----------------------------------------------")

else: 
    print("---INVALID SELECTION---")

quit()
