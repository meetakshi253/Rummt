# INDIAN RUMMY

A game of Indian Rummy developed using PyGame for CSE 101 Introduction to Programming Bonus Assignment.

## Run Locally

Clone the project

```bash
  git clone https://github.com/meetakshi253/Rummy/
```

Go to the project directory

```bash
  cd Rummy
```

Install python modules

```bash
  pip install pygame
```

Run the script

```bash
  python code.py
```

## Rules and gameplay

The main objective is to create melds consisting of three cards. The melds can be of the following forms:

> Three consecutive cards of the same suit (wrap around not allowed). <br/>
> Three cards of the same rank and different suits

- The rank of the cards goes like: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.
- The deck consists of 104 cards i.e. 2 decks of cards. The user and the computer (Joe) are given 10 cards at the start.
- There are two other piles- the selection deck (which remains face down) and the discard pile. A player can select a card from any of these two provided that the discard pile as more than one card in it.
- After choosing a card the player can now discard it and continue the game or click on the show button if they think that they have the best possible cards to make a show.
- After clicking on show, the player selects a card from their pile and places it facedown on the discard pile.
- The player will then choose 3 cards and click on the GROUP button to make a group. If they select more than 3 cards, the selection doesn't count. The grouped cards will be displayed alongside in a pile.
- When there's only a single card left while grouping, clicking on it will display the result.

## Scoring

- Maximum score is 10. It is given when consecutive cards of the same suit are grouped.
- If the face cards are grouped, 20 points are awarded.
- Groups of cards of the same rank and different suits carry 5 points.

## Contact

- [Meetakshi Setiya](meetakshisetiya.vercel.app)
- [Github: meetakshi253](https://github.com/meetakshi253)
- [LinkedIn: meetakshisetiya](https://www.linkedin.com/in/meetakshisetiya/)
