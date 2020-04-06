import PokerCard
## 匯入撲克牌
class Player():
      def __init__(self, name):
            self.name = name
            self.score = 0
            self.on_hand = [ 42, 43, 47, 51]
            self.on_hand_index = [ 0, 1, 2 , 3, 4]

      def get_cards(self, card):
            self.on_hand.append( card)
            self.on_hand_index.append( int( self.on_hand_index[ -1]) +1)

      def turn(self): ## 回合分兩部分撰寫，前半部分給子類別繼承，後半部分統一運作
            pass
      def turn_part2(self, index):
            chosen = self.on_hand.pop( index)
            del self.on_hand_index[ -1]
            return chosen

      def show_cards_on_hand(self):## 逐一顯示撲克牌花色與數字 ##
            showing = self.name + " have "
            if ( self.on_hand_index[ -1] > 0):                  
                  for i in range( self.on_hand_index[ -2]):
                        showing = showing + PokerCard.number_of_suit( self.on_hand[ i]) + ", "
                        
                  showing = showing + PokerCard.number_of_suit( self.on_hand[ self.on_hand_index[ -2]])  
            else:
                  showing = showing + "NO MORE CARDS"
                  
            return showing # str

class User(Player):
      def turn(self):
            ## 要出第 user_input 張牌
            user_input =  input( "which number of card on your hand you wanna choose? ")
            if  user_input not in str( self.on_hand_index) or user_input == "0":
                  ## 檢驗輸入是否正確
                  print( "UNVALID CARD NUMBER, please try again \n")
                  return self.turn() 
            userturn = self.turn_part2( int( user_input) -1)
            print("%s choose card %s"
                 % (self.name, userturn))
            left = self.show_cards_on_hand()
            print( "after your turn, " + left + " remain")


class CPU(Player):
      def turn(self): ## 電腦只會出最後一張牌
            cputurn = self.turn_part2( -1)
            print("%s choose card %s"
                 % (self.name, 1))

### 測試 ###
user1 = User("hhhh")
print(user1.name)
print (user1.show_cards_on_hand ())
user1.get_cards (12)
print (user1.show_cards_on_hand ())
user1.turn()

cpu1 = CPU("cpu1")
print (cpu1.show_cards_on_hand ())
cpu1.turn()
print (cpu1.show_cards_on_hand ())












