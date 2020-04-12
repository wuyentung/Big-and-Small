import PokerCard
import player


######### GAME DESCRIBTION #########
input( '沒朋友嗎？來比大小吧！')
input( '遊戲規則是 A 最大 2 最小；花色大小順序為 黑桃> 愛心> 方塊 >梅花')
input( '每人會拿到13張撲克牌，共比13回合，獲勝最多次的即為贏家')
input( '平手的話則有兩位以上玩家獲勝')
input( '請按enter 繼續')
user_name= input( '\n請輸入使用者名稱: ')
print("\n----- GAME START -----\n")

using_deck = PokerCard.Poker()
using_deck.deck_shuffle()
p1 = player.User( user_name)
cpu1 = player.CPU("cpu1")
cpu2 = player.CPU("cpu2")
cpu3 = player.CPU("cpu3")
player_list = [ p1, cpu1, cpu2, cpu3]

### 洗、發牌 ###
def shuffle_n_distribute( full_deck, players, num_of_players): ## Poker,player in list, num

      full_deck.deck_shuffle()
      for i in range( len( full_deck.deck)):
            players[ i % num_of_players].get_cards( full_deck.deck[ i])
      return players ## player in list
### UNIT TEST for shuffle_n_distribute ###
'''
for i in range( len( player_list)):
      print( player_list[ i].show_cards_on_hand())
'''
## main##
shuffle_n_distribute( using_deck, player_list, len( player_list))

#print( player_list[ 0].show_cards_on_hand())
score_list = []
turn_list = []
for i in range( len( player_list)):
      score_list.append( player_list[ i].score)
      turn_list.append( 0)
### 每一回合的情況 ###
'''
## 按照玩家順序出牌
## 每回合比大小並計分
'''
def play_round():
      print( player_list[ 0].show_cards_on_hand())
      for i in range( len( player_list)):
            turn_list[ i] = player_list[ i].turn()
      turn_winner = turn_list.index( max( turn_list))
      print( player_list[ turn_winner].name + " 出了 " +
             PokerCard.number_of_suit( turn_list[ turn_winner]) + " 贏了這一回合")
      score_list[ turn_winner] = score_list[ turn_winner] +1
      print( "\n現在比分為：")
      for i in range( len( player_list)):
            print( "%s : %d 分" %( player_list[ i].name, score_list[ i]))
      print("-----------------\n\n")
            
for i in range( 13):
      print( "第 %d 回合" % ( i + 1))
      if i == 12:
            print( "最後一回合")
      print( "")
      play_round()
print( "------- GAME OVER-------\n")
## 選出獲勝者
winning_point = max( score_list)
print( "比大小的獲勝者是:")
if score_list.count(winning_point) == 1:
      print( player_list[ score_list.index(winning_point)].name)
else:
      for i in range( len( player_list)):
            if score_list[ i] == winning_point:
                  print( player_list[ i].name)



















