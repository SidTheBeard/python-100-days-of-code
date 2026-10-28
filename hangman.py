from wonderwords import RandomWord

def hangman():
    w = RandomWord()
    answer = w.word()
    spaces = ["_" for _ in range(len(answer))]
    chances = 6
    
    print("".join(spaces))
    while chances > 0 and "".join(spaces).lower() != answer.lower():
        guess = input("Guess a letter\n")
        if len(guess) > 1:
            guess = guess[0]
        if guess.lower() not in answer.lower():
            print(f"Wrong, no {guess.upper()}\n")
            chances -= 1
        else:
            indices = [i for i, c in enumerate(answer.lower()) if c == guess.lower()]
            while len(indices) > 0:
                spot = indices.pop(0)
                spaces[spot] = answer[spot]
        print("".join(spaces).upper())
    
    if chances > 0:
        print(f"\n\n\nYou Win!")
    else:
        print(f"Game Over! The word was: {answer}")
    

hangman()