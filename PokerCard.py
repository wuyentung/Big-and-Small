####  舊版  ###
'''
def show_number(num):
      if (num > 51):
            return "out of the deck"
      return num % 13 +1
z = 5
      
def show_suit(num):
      if (num > 51):
            return "out of the deck"
      thissuit = num % 4
      suit =["梅花","紅心","方塊","黑桃"]
      return suit[thissuit]
print ("%d in poker card means %s of %s"
       %(z, show_number(z), show_suit(z)))
'''
### 優化 ###
def number_of_suit(num): ##int
      ### 最小為 0 ，從 梅花 2 開始
      this_number = num // 4 +2
      if this_number > 10:
            if this_number == 11:
                  this_number = "J"
            elif this_number == 12:
                  this_number = "Q"
            elif this_number == 13:
                  this_number = "K"
            elif this_number == 14:
                  this_number = "A"
      this_suit = num % 4
      suit =["梅花","方塊","紅心","黑桃"]
      #showing = str( num) + " in poker card means " + str( this_number) + " of " + str( suit[this_suit])
      showing = str( suit[this_suit]) + " " + str( this_number) ## 花色 數字

      return showing # str
### 測試用 ###
'''
z = 20
print( number_of_suit(z))
'''



















