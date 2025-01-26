import pygame
from pygame.locals import *
import sys
import os
import random
import copy

pygame.init()

GREEN = (30, 92, 58)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BlackJack')
FPS = 60

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4

CARD_BACK = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'backCard.jpg')), (120, 220))

c2 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c2.jpg')), (70, 100))
c3 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c3.jpg')), (70, 100))
c4 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c4.jpg')), (70, 100))
c5 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c5.jpg')), (70, 100))
c6 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c6.jpg')), (70, 100))
c7 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c7.jpg')), (70, 100))
c8 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c8.jpg')), (70, 100))
c9 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c9.jpg')), (70, 100))
c10 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'c10.jpg')), (70, 100))
cA = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'cA.jpg')), (70, 100))
cJ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'cJ.jpg')), (70, 100))
cQ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'cQ.jpg')), (70, 100))
cK = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'cK.jpg')), (70, 100))

d2 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd2.jpg')), (70, 100))
d3 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd3.jpg')), (70, 100))
d4 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd4.jpg')), (70, 100))
d5 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd5.jpg')), (70, 100))
d6 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd6.jpg')), (70, 100))
d7 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd7.jpg')), (70, 100))
d8 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd8.jpg')), (70, 100))
d9 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd9.jpg')), (70, 100))
d10 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'd10.jpg')), (70, 100))
dA = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'dA.jpg')), (70, 100))
dJ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'dJ.jpg')), (70, 100))
dQ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'dQ.jpg')), (70, 100))
dK = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'dK.jpg')), (70, 100))

h2 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h2.jpg')), (70, 100))
h3 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h3.jpg')), (70, 100))
h4 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h4.jpg')), (70, 100))
h5 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h5.jpg')), (70, 100))
h6 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h6.jpg')), (70, 100))
h7 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h7.jpg')), (70, 100))
h8 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h8.jpg')), (70, 100))
h9 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h9.jpg')), (70, 100))
h10 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'h10.jpg')), (70, 100))
hA = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'hA.jpg')), (70, 100))
hJ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'hJ.jpg')), (70, 100))
hQ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'hQ.jpg')), (70, 100))
hK = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'hK.jpg')), (70, 100))

s2 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's2.jpg')), (70, 100))
s3 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's3.jpg')), (70, 100))
s4 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's4.jpg')), (70, 100))
s5 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's5.jpg')), (70, 100))
s6 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's6.jpg')), (70, 100))
s7 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's7.jpg')), (70, 100))
s8 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's8.jpg')), (70, 100))
s9 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's9.jpg')), (70, 100))
s10 = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 's10.jpg')), (70, 100))
sA = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'sA.jpg')), (70, 100))
sJ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'sJ.jpg')), (70, 100))
sQ = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'sQ.jpg')), (70, 100))
sK = pygame.transform.scale(pygame.image.load(os.path.join('Blackjack Cards', 'sK.jpg')), (70, 100))

CARD_DECK = [c2,c3,c4,c5,c6,c7,c8,c9,c10,cA,cJ,cQ,cK,d2,d3,d4,d5,d6,d7,d8,d9,d10,dA,dJ,dQ,dK,h2,h3,h4,h5,h6,h7,h8,h9,h10,hA,hJ,hQ,hK,s2,s3,s4,s5,s6,s7,s8,s9,s10,sA,sJ,sQ,sK]

font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 35)
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

active = False
records = [0, 0, 0]
player_score = 0
dealer_score = 0

initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'PLAYER BUSTED', 'Player WINS!', 'DEALER WINS', 'TIE GAME']

CARD = (random.choice(CARD_DECK))

def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card-1])
    current_deck.pop(card-1)
    return current_hand, current_deck

def draw_scores(player, dealer):
    screen.blit(font.render(f'Score[{player}]', True, WHITE), (350, 400))
    if reveal_dealer:
        screen.blit(font.render(f'Score[{dealer}]', True, WHITE), (350, 100))

#make card imiges
def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, WHITE, [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
        screen.blit(font.render(player[i], True, BLACK), (75 + 70 * i, 465 + 5 * i))
        screen.blit(font.render(player[i], True, BLACK), (75 + 70 * i, 635 + 5 * i))
        pygame.draw.rect(screen, BLACK, [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

    for i in range(len(dealer)):
        pygame.draw.rect(screen, WHITE, [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, BLACK), (75 + 70 * i, 165 + 5 * i))
            screen.blit(font.render(dealer[i], True, BLACK), (75 + 70 * i, 335 + 5 * i))
        else:
            screen.blit(CARD_BACK, (70 + 70 * i, 160 + 5 * i))

def calculate_score(hand):
    hand_score = 0
    aces_count = hand.count('A')
    for i in range(len(hand)):
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])

        if hand[i] in ['10', 'J', 'Q', 'K']:
            hand_score += 10

        elif hand[i] == 'A':
            hand_score += 11

    if hand_score > 21 and aces_count > 0:
        for i in range(1, aces_count+1):
            if hand_score > 21:
                hand_score -= 10

    return hand_score



def draw_game(act, record, result):
    button_list = []
    if not act:
        deal = pygame.draw.rect(screen, RED, [335, 275, 300, 100], 0, 5)
        pygame.draw.rect(screen, BLACK, [335, 275, 300, 100], 3, 5)
        deal_text = font.render('DEAL HAND', True, BLACK)
        screen.blit(deal_text, (350, 305))
        button_list.append(deal)
    else:
        hit = pygame.draw.rect(screen, RED, [700, 500, 300, 100], 0, 5)
        pygame.draw.rect(screen, BLACK, [700, 500, 300, 100], 3, 5)
        hit_text = font.render('HIT ME', True, BLACK)
        screen.blit(hit_text, (775, 530))
        button_list.append(hit)

        stand = pygame.draw.rect(screen, RED, [700, 600, 300, 100], 0, 5)
        pygame.draw.rect(screen, BLACK, [700, 600, 300, 100], 3, 5)
        stand_text = font.render('STAND', True, BLACK)
        screen.blit(stand_text, (775, 630))
        button_list.append(stand)

        score_text = smaller_font.render(f'Wins: {records[0]}   Losses:{record[1]}  Pushes:{record[2]}', True, WHITE)
        screen.blit(score_text, (250, 5))
    if result != 0:
        screen.blit(font.render(results[result], True, WHITE), (338, 50))
        deal = pygame.draw.rect(screen, RED, [700, 400, 300, 100], 0, 5)
        pygame.draw.rect(screen, RED, [700, 400, 300, 100], 3, 5)
        pygame.draw.rect(screen, BLACK, [700, 400, 300, 100], 3, 5)
        deal_text = font.render('NEW HAND', True, BLACK)
        screen.blit(deal_text, (730, 430))
        button_list.append(deal)
    return button_list

def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else:
            result = 4
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False
    return result, totals, add


    pygame.display.update()

while True:
    window.fill(GREEN)
    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        print(my_hand, dealer_hand)
        initial_deal = False

    if active:
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck == deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    outcome = 0
                    add_score = True
            else:
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        reveal_dealer = False
                        outcome = 0
                        add_score = True
                        dealer_score = 0
                        player_score = 0

    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    buttons = draw_game(active, records, outcome)

    pygame.display.update()

    clock.tick(FPS)
