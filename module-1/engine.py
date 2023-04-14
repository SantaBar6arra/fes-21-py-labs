from constants import *
import random

class Engine:
    def __init__(self):
        self.playersturn = WHITE
        self.message = ''
        self.gameboard = {}
        self.is_active = True
        self.setupBoard()
        print('enter moves like "b1 c3"')
        self.run()
        
    def setupBoard(self):
        self.gameboard[(random.randint(2, 5), 0)] = King(WHITE, uniDict[WHITE][King]) 
        self.gameboard[(random.randint(2, 5), 7)] = King(BLACK, uniDict[BLACK][King]) 

        whiteFiguresCount, blackFiguresCount = random.randint(5, 10), random.randint(5, 10)

        self.placeFigures(WHITE, whiteFiguresCount)
        self.placeFigures(BLACK, blackFiguresCount)

    def placeFigures(self, color, figuresCount):
        figures_av = {
            Queen: 1,
            Rook: 2,
            Knight: 2,
            Bishop: 2,
            Pawn: 8
        }

        figures = [Rook,Knight,Bishop,Queen,Pawn]

        for i in range(figuresCount):
            figureType = figures[random.randint(0, len(figures)-1)]
        
            figure = Figure(None, None) # mock to save it for bigger scope
            if figureType == Pawn:
                figure = figureType(color, uniDict[color][figureType], 1 if color == WHITE else -1)
            else:
                figure = figureType(color, uniDict[color][figureType])
            self.setFigureToField(figure)

            figures_av[figureType] -= 1
            if figures_av[figureType] == 0:
                figures.remove(figureType)

    def setFigureToField(self, figure):
        isFieldSet = False

        while isFieldSet == False:
            pretendedField = (0,0)

            if hasattr(figure, 'direction'):
                if figure.Color == WHITE:
                    pretendedField = (random.randint(0, 8), random.randint(1, 4))
                else:
                    pretendedField = (random.randint(0, 8), random.randint(3, 6))
            else:
                pretendedField = (random.randint(0, 8), random.randint(0, 8))

            if  pretendedField not in self.gameboard: # if no one is there
                isFieldSet = True
                self.gameboard[pretendedField] = figure

        if self.isCheck() == True:
            del self.gameboard[pretendedField]
            self.setFigureToField(figure)
    
    def run(self):
        while self.is_active:
            self.render()
            print(self.message)
            self.message = ''
            startpos,endpos = self.parsePrompt()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = 'Could not find the piece'
                target = None
                
            if target:
                print('found ' + str(target))
                if target.Color != self.playersturn:
                    self.message = "You aren't allowed to move that piece now"
                    continue

                if target.is_valid(startpos,endpos,target.Color,self.gameboard):
                    self.message = 'Move is valid'
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]

                    if self.isMate() == True:
                        self.is_active = False
                        continue

                    self.isCheck()

                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
                else : 
                    self.message = 'Move invalid -> ' + str(target.get_av_mvs(startpos[0],startpos[1],self.gameboard))
                    print(target.get_av_mvs(startpos[0],startpos[1],self.gameboard))
            else : self.message = 'There is no piece in that space'

        print(self.message)
        self.render()
                    
    def isCheck(self):
        kingDict = {}
        pieceDict = {BLACK : [], WHITE : []}
        for position,piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            pieceDict[piece.Color].append((piece,position))

        if self.isKingReachable(kingDict[WHITE],pieceDict[BLACK]):
            self.message = 'White player is in check'
            return True
        if self.isKingReachable(kingDict[BLACK],pieceDict[WHITE]):
            self.message = 'Black player is in check'
            return True
        
        self.message = ''
        return False

    def isMate(self):
        kingDict = {}
        for position,piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position

        if WHITE not in kingDict:
            self.message = '1 - 0 black won'
            return True
        if BLACK not in kingDict:
            self.message = '1 - 0 white won'
            return True
        
        return False    

    def isKingReachable(self,kingpos,piecelist):
        for piece,position in piecelist:
            if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                return True
            
        return False
                
    def parsePrompt(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return (a,b)
        except:
            print('Error decoding input, please try again')
            return((-1,-1), (-1,-1))
    
    def render(self):
        print("  " + "_" * 33)
        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(8):
            print("--" + "|---" * 8 + "|")
            print(" " + chr(i+97), end="| ")
            for j in range(8):
                item = self.gameboard.get((i,j), " ")
                print(str(item) + ' |', end = " ")
            print()
        print("  " + "-" * 33)
