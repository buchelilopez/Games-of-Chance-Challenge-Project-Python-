import random

money = 100

#Write your game of chance functions here

#Flipping a coin
def flipping_coin(bet, selection):
    if bet > money:
        print("You don't have enough to make this bet")
        return 0
    elif bet < 0:
        print("You trying to make an negative bet")
        return 0
    else:
        num = random.randint(0, 1)
        if num == 0:
            result = "Heads"
        else: 
            result = "Tails"
        if selection == result:
            profit = bet
            print("Your selection was", selection, "and when the coin was flipped it was", result, "so you won", profit)
            money += profit #I will like to know why I can not add to the money variable this way?
        else:
            lose = bet * -1
            print("Your selection was", selection, "and when the coin was flipped it was", result, "so you lose", lose)
            money += lose #I will like to know why I can not add to the money variable this way?

#Cho-Han
def cho_han(bet, selection):
    if bet > money:
        print("You don't have enough to make this bet")
        return 0
    elif bet < 0:
        print("You trying to make an negative bet")
        return 0
    else:
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        total = num1 + num2
        if total % 2 == 0:
            result = "Even"
        else:
            result = "Odd"
        if selection == result:
            profit = bet
            print("Your selection was", selection, "and when the dice where rolled it was", num1, "and", num2, "for a total of", total, "which is", result, "so you won", profit)
            return profit
        else:
            lose = bet * -1
            print("Your selection was", selection, "and when the dice where rolled it was", num1, "and", num2, "for a total of", total, "which is", result, "so you lose", lose)
            return lose

#Playing Cards
def playing_cards(bet):
    if bet > money:
        print("You don't have enough to make this bet")
        return 0
    elif bet < 0:
        print("You trying to make an negative bet")
        return 0
    else:
        my_card = random.randint(1, 13)
        other_player_card = random.randint(1, 13)
        if my_card > other_player_card:
            profit = bet
            print("You picked the card", my_card, "which is higher than", other_player_card, "picked by the other player. You won", profit)
            return profit
        elif my_card == other_player_card:
            profit = 0
            print("You picked the card", my_card, "which is the same that", other_player_card, "picked by the other player. You don't have any profit or lose on this bet")
            return profit
        else:
            lose = bet * -1
            print("You picked the card", my_card, "which is lower than", other_player_card, "picked by the other player. You lose", lose)
            return lose

#Playing Roulette
def roulette(bet, selection):
    if bet > money:
        print("You don't have enough to make this bet")
        return 0
    elif bet < 0:
        print("You trying to make an negative bet")
        return 0
    else:
        num = random.randint(0, 37)
        if selection == "Odd" or selection == "Even":
            if num == 0:
                result = 0
            elif num == 37:
                result = "00"
            elif num % 2 == 0:
                result = "Even"
            else:
                result = "Odd"
            reward = 1
        else:
            result = num
            reward = 35
        if result == 37:
            result = "00"
        if selection == result:
            profit = bet * reward
            print("Your selection was", selection, "and the roulette got", result, "so you won", profit)
            return profit
        else:
            lose = bet * -1
            print("Your selection was", selection, "and the roulette got", result, "so you lose", lose)
            return lose

#Call your game of chance functions here
flipping_coin(200, "Heads")
print("Now you have", money, "in you pocket")
money += cho_han(30, "Odd")
print("Now you have", money, "in you pocket")
money += playing_cards(50)
print("Now you have", money, "in you pocket")
money += roulette(10, "Odd")
print("Now you have", money, "in you pocket")