'''
########################################
################遊戲介紹################
########################################
'''
none= input( '沒朋友嗎？來比大小吧！')
none= input( '遊戲規則是 A 最大 2 最小；花色大小順序為 黑桃> 愛心> 方塊 >梅花')
none= input( '每人會拿到13張撲克牌，共比13輪，獲勝最多次的即為贏家')
none= input( '平手的話則有兩位以上玩家獲勝')
none= input( '請按enter 繼續')
user_name= input( '\n請輸入使用者名稱: ')
'''
########################################
#############建立撲克牌字典#############
########################################
'''
cards= list( range(1, 53))
number= range(1, 53)
deck= dict(zip( cards, number))
#print( deck)

suits= [ '黑桃 ', '梅花 ', '方塊 ', '愛心 ']

numbers= [ '2', '3', '4', '5', '6', '7', '8', '9', '10',
           'J', 'Q', 'K', 'A']

suit_and_number= deck.copy()
for i in range( 0, 52): #分印出的花色      
      #print( i, cards[ i], '\t', cards[ i]% 4)
      suit= cards[ i]% 4
      number= (cards[ i]- 1)// 4
      for ii in range( 0, 4):
            if suit == ii:
                  suit_and_number[ i+1]= suits[ ii]+ numbers[ number]

#print( suit_and_number)



'''
########################################
############設定使用者手牌字典##########
########################################
'''
player1 = dict()
player2 = {}
player3 = {}
player4 = {}


'''
########################################
################洗牌發牌################
########################################
'''
cards= list( range(1, 53))
shuffled_cards= cards

import random
random.shuffle( shuffled_cards)
#print( shuffle_cards, '\n')
p1hands= shuffled_cards[ 0: 49: 4]
p2hands= shuffled_cards[ 1: 50: 4]
p3hands= shuffled_cards[ 2: 51: 4]
p4hands= shuffled_cards[ 3: 52: 4]


'''
########################################
######按大小順序顯示顯示使用者手牌######
########################################
'''
p1hands.sort()
for i in range( 0, 13):
      player1[ i+ 1]= p1hands[ i]
#print( player1)
for i in range( 0, 13):
      player2[ i+ 1]= p2hands[ i]
for i in range( 0, 13):
      player3[ i+ 1]= p3hands[ i]
for i in range( 0, 13):
      player4[ i+ 1]= p4hands[ i]

'''
########################################
############## P1手牌顯示###############      
########################################
'''
print( '\n%s 的手牌從小到大是' %user_name, end= '\n \t')
for i in range( 1, 13):
      print(suit_and_number[ player1[ i]], end= ', ')
print(suit_and_number[ player1[ 13]])
print(' ')
'''
########################################
#################字典複製###############      
########################################
'''
score_all= [ 0, 0, 0, 0]
all_hands= [ player1, player2, player3, player4]
all_names= [ user_name, 'player2', 'player3', 'player4']
player1_copy= player1.copy()
player2_copy= player2.copy()
player3_copy= player3.copy()
player4_copy= player4.copy()
all_hands_copy= [ player1_copy, player2_copy,
                  player3_copy, player4_copy]
every_round= [ 0, 0, 0, 0]

'''
########################################
#############建立查找用字典#############      
########################################
'''
reverse_suit_and_number= {} #建立反向查找花色數字的字典
for i in range( 1, 53):
      reverse_suit_and_number[ suit_and_number[ i]]= i
reverse_player1= {} #建立反向查找 player1 手牌花色數字的字典
for i in range( 1, 14):
      reverse_player1[ player1[ i]]= i
      

'''
########################################
##################打牌##################
########################################
'''

#串列可以放字典 呼叫方式:[0](list)[0](dict)
none= input( '請按enter 繼續')
print('\n=============比大小開始=============')

for i in range( 1, 14):
      print( '\n-------- round %s -------' % i)
      print( '\n%s 手中有' %user_name, end= '\n\t')
      for ii in player1_copy:
            print(suit_and_number[ player1_copy[ ii]],
                  end= ', ')
      round1= input( '\n\n  請出牌(花色 數字): ')
      while True:  #round1 要在第一個迴圈裡面轉換好才能到第二個迴圈
            while True:  ##轉換中文值成字典suit_and_number的鍵
                  if round1 in reverse_suit_and_number:
                        round1= reverse_suit_and_number[ round1]
                        break
                  else:
                        round1= input( '請輸入要出的牌(如: 梅花 3): ')
      
            if round1 in all_hands_copy[ 0].values():
                  every_round[ 0]= all_hands_copy[ 0].pop(
                        reverse_player1[ round1])
                  print( '%-7s 出了 %s' %( user_name, suit_and_number[round1]))
                  break
            else:
                  round1= input( '\n請輸入手中的牌: ')
      for ii in range( 1, 4):
            every_round[ ii]= all_hands_copy[ ii].pop( i)
            print( '%s 出了 %s' %( all_names[ ii],
                                 suit_and_number[ every_round[ ii]]))
      '''
      ########################################
      ##################計分##################
      ########################################
      '''  
      biggest=  max( every_round)
      for ii in range( 0, 4):
            if biggest in all_hands[ ii].values():
                  print( '\n恭喜 %s 用 %s 贏了這回合' %( all_names[ ii],
                                             suit_and_number[ every_round[ ii]]))
                  score_all[ ii] += 1
                  
                  print( '目前比分為:')
                  for j in range( 0, 4):
                        print( '\t %-10s: %s' %(all_names[ j], score_all[ j]))

print( '=============遊戲結束=============')        
winner= max( score_all)
for i in range( 0, 4):
      if winner== score_all[ i]:
            print('最終獲勝的是 %s, 總共拿了 %s 分'
                   %( all_names[ i], winner))
      
none= input( '請按enter 繼續')

            

























