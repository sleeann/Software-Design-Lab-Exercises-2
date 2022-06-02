from die import Die

class Player(object):
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.rolls =[]
        self.rollscount = 0
        self.atStartup = True
        self.winner = False
        self.looser = False

    def __str__(self):
        result =""
        for (v1,v2)in self.rolls:
            result = result + str((v1,v2)) + " " +\
                    str(v1+v2) + "n"
        return result
    def getNumberofRolls(self):
        return len(self.rolls)

    def rollDice(self):
        self.die1.roll()
        diefirst = self.die1.getValue()
        self.die2.roll()
        diesecond = self.die2.getValue()
        res =(diefirst, diesecond)
        self.rollscount +=1
        self.rolls =[]
        v1 = diefirst
        v2 = diesecond
        self.rolls.append((v1,v2))
        initialSum = v1 + v2
        if initialSum in (2,3,12):
            self.looser = True
        elif initialSum in (7,11):
            self.winner = True
        else:
            while(True):
                self.die1.roll()
                self.die2.roll()
                (v1, v2) = (self.die1.getValue(),
                self.die2.getValue())
                self.rolls.append((v1, v2))
                laterSum = v1 + v2
                if laterSum == 7:
                    self.looser = True
                    self.winner = False
                    break
                elif laterSum == initialSum:
                    self.winner = True
                    self.looser = False
                    break
            return res

    def isWinner(self):
        if self.winner is True:
            return True
    def isLooser(self):
        if self.looser is True:
            return True

    def __str__(self):
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str ((v1, v2)) + " " +\
            str (v1 + v2) + "\n"
        return result

    def playOneGame(self, yourDice):
        player = Player()
        youWin = player.rollDice()
        print("Your Dice result is: ", yourDice)
        youWin = player.isWinner()
        youLoose = player.isLooser()
        if youWin:
            print("You Win!")
        if youLoose:
            print("You Lose!")

    def playManyGames(number):
        wins = 0
        losses = 0
        winRolls = 0
        lossRolls = 0
        player = Player()
        for count in range(number):
            dicenum = player.rollDice()
            print("your dice num is: ", dicenum)
            hasWon = player.isWinner()
            rolls = player.getNumberofRolls()
            if hasWon:
                wins  += 1
                winRolls += rolls
            else:
                losses +=1
                lossRolls += rolls
        print("The total Number of wins is: ", wins)
        print("The total Number of losses is: ", losses)
        print("The average number of rolls per win is %0.2f" % \
              (winRolls / wins))
        print("The average number of rolls per loss is %0.2f" % \
              (winRolls / losses))
        print("The winning percentage is %0.3f" % (wins*100 / number) + "%")

    def main():
        number = int(input("Enter a number of games: "))
        playManyGames(number)

    if __name__ == "__main__":
        main()