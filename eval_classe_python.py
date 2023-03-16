# EX 1
# Question 2, 3 et 4

class Player:
    def __init__(self,name):
        self.pseudo=name
        self.score=[0,0,0,0,0]

    def affiche(self):
        print(f"Score de {self.pseudo} :")
        for i in self.score:
            print(i)

    def ajouter(self,chanson,newscore):
        if newscore>self.score[chanson]:
            self.score[chanson]=newscore

    def moyenne(self):
        moyenne=0
        for i in self.score:
            moyenne+=i
        print(f"Moyenne des scores de {self.pseudo} :")
        print(moyenne/len(self.score))

    def total(self):
        total=0
        for i in self.score:
            total+=i
        print(f"Total des scores de {self.pseudo} :")
        print(total)

    def meilleur(self):
        print(f"Meilleur score de {self.pseudo} :")
        print(max(self.score))
        print("Sur la chanson :")
        print(self.score.index(max(self.score)))
        

    def pire(self):
        print(f"Pire score de {self.nom} :")
        print(min(self.score))
        print("Sur la chanson :")
        print(self.score.index(min(self.score)))
    
        

if __name__ =="__main__":
    chanson1=0
    chanson2=1
    chanson3=2
    chanson4=3
    chanson5=4

    def jouer(joueur:Player):
            from random import randint
            chanson=randint(0,len(joueur.score)-1)
            score=randint(50,100)
            joueur.ajouter(chanson,score)

    J1=Player("Mario")

    J1.affiche()
    for i in range(5):
        jouer(J1)
    J1.affiche()
    J1.meilleur()
    J1.pire()
    J1.moyenne()
    J1.total()
