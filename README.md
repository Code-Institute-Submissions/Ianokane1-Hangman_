# Hangman

Hangman is a game usually played by two or more people, where one person thinks of a word while the others guess what the word is by guessing one letter at a time until the whole word is revealed.
For this project I wanted to create a version of this game that you can play against the computer rather than playing against another person.
This is done by using python to generate the word and check if the user's guesses are correct, incorrect, invalid or if the user has already guessed the letter.

<img src="images/amireponsive.png" alt="image of app on different sized screens">

[Click here to go to the live website!](https://iankanehangman.herokuapp.com/) 

## Table of contents 

1. [Plans and structure](#plans-and-structure)
    - [Objectives](#objectives)
    - [Changes throughout the process](#changes-throughout-the-process)
2. [Color scheme](#color-scheme)
3. [Features](#features)
    - [Welcome page](#welcome-page)
    - [Instructions](#instructions)
    - [Game](#game)
    - [Losing message](#losing-message)   
    - [Winning message](#winning-message) 
    - [Colored text](#colored-text) 
    - [Clear terminal](#clear-terminal)
    - [Extra features](#extra-features)
4. [Testing](#testing)
    - [Python](#python)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
5. [Deployment](#deployment)
6. [Finished product](#finished-product)
7. [Credits](#credits)

## Plans and structure 

<img src="images/hangmanflowchart.png" alt="Screenshot of the hangman flow chart">  

### Objectives

- I want to create a game that is easy to navigate. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - This was achieved by creating three categories for user to choose from.
                        
 - I want the game to run in a smooth loop to allow the user to keep playing as many times as they'd like to. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - If a user either loses or wins the game it will take them to game menu where they can choose another category.

- To make it clear to the user how many tries they have left until the game is over.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong the characters will print out the traditional hangman image. The user will also know what letters they have selected below image. Reselecting the same letter in error will not result in fail.

### Changes throughout the process

Throughout the process of making this project I decided to change a couple of things due to the time limit I had to make the game. 

- Originally, I planned to have difficulty settings where user could select easy, medium or hard. I opted to keep it simple and instead use three category options.

I decided that this idea was not as important as all the other functions so I would like to either implement them if I have time to at the end of the process or if not, I would like to implement them in the future so I can continue to use this game with family and friends. 

Go back to [Table of contents](#table-of-contents)         
