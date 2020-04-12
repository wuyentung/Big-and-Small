import random

class Poker():
      def __init__( self):
            self.num_of_cards = 52
            self.deck = []
            self.creat_deck()

      def creat_deck( self):## 創建牌組
            for i in range( self.num_of_cards):
                  self.deck.append( i)
            return self.deck
      
      def deck_shuffle( self):
            random.shuffle( self.deck)
### unit test ###
'''
deck1 = Poker()
deck1.deck_shuffle()
print( deck1.deck)
'''
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

### 優化 顯示花色 ###
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
### unit test ###

'''
z = 20
print( number_of_suit(z))
'''

### 洗牌 + 發牌 ###
import random
def shuffle_n_distribute( deck, players, num_of_players): ## list,list in list, num
      random.shuffle( deck)
      for i in range( len( deck)):
            players[ i % num_of_players].append( deck[ i])
      return players ## list in list
'''
### unit test ###
z1 = []
z2 = []
z3 = []
z4 = []
z = [ z1, z2, z3, z4]
a = [ 1, 2, 3, 4, 5, 6, 7, 8]

print( z ,"\n")
shuffle_n_distribute( a, z, 4)
print( z)
'''



























