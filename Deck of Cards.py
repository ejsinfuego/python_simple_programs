class Card:

 suitList = ['narf','Clubs', 'Diamonds','Hearts', 'Spades']
 rankList = ['narf', 'Ace', '2', '3', '4', '5', '6', '7','8', '9' '10', 'Jack', 'Queen', 'King']

 def __init__(self, suit=0, rank=2):
     self.suit = suit
     self.rank = rank
 
 def __cmp__(self, other):
     #check the suits
     if self.suit > other.suit:return 1
     if self.suit < other.suit:return -1
     if self.suit == other.suit:return  0
     if self.rank > other.rank:return 1
     if self.rank < other.rank:return -1
     if self.rank == other.rank:return 0

 def __str__(self):
     return(self.rankList[self.rank] + ' of ' + self.suitList[self.suit])

        
card1 = Card(1,3)
card2 = Card(3,5)
card2.suitList[3] = 'favorite lopes'
print(card1)
print(card2)
print(card2.suitList[1])



