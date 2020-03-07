from random import randint

class Die(object):
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1,6)

    def getvalue(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Player(object):
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        self.rollsCount = 0
        self.start = 0
        self.state = 0

    def __str__(self):
        result = ""
        for (v1,v2) in self.rolls:
            result = result + str((v1, v2)) + " = " + \
                     str(v1 + v2) + "\n"
            return result

    def play(self):
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getvalue(),self.die2.getvalue())
        self.rolls.append((v1,v2))
        initialSum = v1 + v2
        if initialSum in (2,3,12):
            return False
        elif initialSum in (7,11):
            return True
        while True:
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getvalue(),self.die2.getvalue())
            self.rolls.append((v1,v2))
            laterSum = v1+v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True
            
    def getNumberOfRolls(self):
        return len(self.rolls)
    
    def rollDice(self):
        self.rollsCount += 1
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getvalue(),self.die2.getvalue())
        self.rolls.append((v1,v2))
        initialSum = v1 + v2
        print("Roll number %d: (%d, %d)" %(self.rollsCount,v1,v2))
        if self.rollsCount == 1:    
            self.start = initialSum
            if initialSum in (2,3,12):
                return self.isLoser()
            elif initialSum in (7,11):
                return self.isWinner()
            self.rollDice()
            return self.state
        else:
            if initialSum == self.start:
                self.state = self.isWinner()
                return self.state
            elif initialSum == 7:
                self.state = self.isLoser()
                return self.state
            else:
                self.rollDice()
                return self.state
              
    def getRollsCount(self):
        return self.rollsCount

    def isWinner(self):
        return 1
        
    def isLoser(self):
        return 2
        

"""
def playOneGame():
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The Total number of wins is",wins)
    print("The Total number of losses is", losses)
    print("The Average number of rolls per win is %0.2f" %(winRolls/wins))
    print("The Average number of rolls per loss is %0.2f" %(lossRolls/losses))
    print("The winning percentage is %0.3f" %(wins/number))
"""

def playOneGame():
    player = Player()
    youWin = player.rollDice()
    if youWin==1:
        print("You win!")
    elif youWin==2:
        print("You lose!")

def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    for _ in range(number):
        player = Player()
        hasWon = player.rollDice()
        print("--------------")
        rolls = player.getRollsCount()
        if hasWon==1:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The Total number of wins is",wins)
    print("The Total number of losses is", losses)
    print("The Average number of rolls per win is %0.2f" %(winRolls/wins))
    print("The Average number of rolls per loss is %0.2f" %(lossRolls/losses))
    print("The winning percentage is %0.3f" %(wins/number)) 

playOneGame()    
#playManyGames(5)

