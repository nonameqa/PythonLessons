class Bands:

    Genre = 'Rock'

    def __init__(self,Lead_Singer,Guitarist,Drummer,Bassist):
        self.Lead_Singer = Lead_Singer
        self.Guitarist = Guitarist
        self.Drummer = Drummer
        self.Bassist = Bassist

    def Members(self):
        print("Members are", self.Lead_Singer, self.Guitarist,self.Drummer,self.Bassist)


greenDay = Bands('Billie','Billie','Tre','Mike')
avengedS = Bands('Matt','Synister','Jimmy','Johnny')
askingA = Bands('Danny', 'Ben','Cassels','Sam')


greenDay.Members()
askingA.Members()
avengedS.Members()

print(greenDay.Bassist)
print(avengedS.Drummer)
print(askingA.Guitarist)

print(greenDay.Genre)

print(avengedS.Genre)