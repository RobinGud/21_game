import random

LIMIT = 21
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'B', 'D', 'K', 'A'] # Колода карт
money = 100 # Начальный баланс игрока

def getStatus():
    print('Player:', player, ' Dealer: ', dealer)

def getSum(hand):
    num = countNum(hand)
    eleven = countAce(hand)
    one = 0
    while num + one + eleven * 11 > LIMIT and eleven > 0:
        eleven-=1
        one+=1
    return num + one + eleven * 11

def countAce(hand):
    ace = 0
    for card in hand:
        if card == 'A':
            ace += 1
    return ace

def countNum(hand):
    sum = 0
    for card in hand:
        if card == 'B' or card == 'D' or card == 'K':
            sum += 10
        elif card != 'A':
            sum += card
    return sum

def playPlayer():
    while True:
        print(getStatus())
        if input(' Want another card? 1 - YES, otherwise - NO: ') == '1':
            player.append(random.choice(cards))
            if getSum(player) >= LIMIT:
                break
        else:
            break

def playDealer():
    while getSum(dealer) < 17:
        dealer.append(random.choice(cards))
    getStatus()

def getResult():
    if getSum(dealer) == LIMIT:
        print('Dealer have Black Jack :(')
        return False
    elif getSum(player) == LIMIT:
        print('You have Black Jack *_*')
        return True
    elif getSum(player) > LIMIT:
        print('You bust :::(')
        return False
    elif getSum(dealer) > LIMIT:
        print('Dealer bust T_T')
        return True
    elif getSum(player) > getSum(dealer):
        print('You Win!')
        return True
    else:
        print('You lost!')
        return False

def game():
    global player
    global dealer
    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards)]
    playPlayer()
    playDealer()
    return getResult()

def betPlayer():
    bet = int(input('Choose your bet: '))
    while 0 > bet > money:
        bet = int(input('You don\'t have so much money. Try again: '))
    return bet

print('Welcome to our casino! \nYour balance:', money, '$')
while True:
    if money <= 0:
        print('Game Over! Your balance: 0 :(')
        break
    if input('Want to play? 1 - YES, otherwise - NO: ') != '1':
        print('I\'ll see you next time. Your winnings:', money - 100, '$')
        break
    bet = betPlayer()
    if game() == True:
        money += bet * 0.5
    else:
        money -= bet
    print('Your balance:', money, '$')
