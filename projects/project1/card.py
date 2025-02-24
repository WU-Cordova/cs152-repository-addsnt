from enum import Enum
from dataclasses import dataclass
from datastructures.bag import Bag
import random
import copy

class Suit(Enum):
    HEARTS = "♥️"
    SPADES = "♠️"
    DIAMONDS = "♦️"
    CLUBS = "♣️"

class Face(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    def face_value(self) -> int:
        match self:
            case Face.JACK | Face.QUEEN | Face.KING:
                return 10
            case Face.ACE:
                return 11
            case _:
                return int(self.value)

@dataclass
class Card:
    face: Face
    suit: Suit

    def __hash__(self) -> int:
        return hash(self.face.name) * hash(self.suit.name)

    def __str__(self) -> str:
        return f"[{self.face.value}{self.suit.value}]"

@dataclass
class MultiDeck:
    def __init__(self):
        self.one_deck_list = [Card(face, suit) for suit in Suit for face in Face]
        self.deck_count = random.choice([2, 4, 6, 8])
        self.initialize_deck()

    def initialize_deck(self):
        self.multi_deck_list = [card for _ in range(self.deck_count) for card in copy.deepcopy(self.one_deck_list)]
        random.shuffle(self.multi_deck_list) # randomizes the order of cards
        self.deck_bag = Bag(*self.multi_deck_list)

    def draw_card(self):
        if len(self.deck_bag.items) == 0:
            self.initialize_deck()
        return self.deck_bag.items.pop(0) # removed the card from the multideck, first from "deck"

