#H A N G M A N 

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
lives = 6 
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = ["_"]* len(chosen_word)
 

while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    
    if guess not in chosen_word:
        lives = lives -1
        print(stages[lives])

        if lives == 0 :
            print("you loose ")
            end_of_game = True
            print(f"the word is {chosen_word}")
    
    if guess in chosen_word:
        for i in range(0,len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    b = ' '.join(display)
    print(b)

    if "_" not in display:
        end_of_game = True
        print("you win")
            

        
