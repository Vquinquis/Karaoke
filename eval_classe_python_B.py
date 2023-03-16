class Player:
    def __init__(self,name):
        self.pseudo=name
        self.score=[0,0,0]
        self.meilleurScore=0
        self.scoreMoyen=0
        self.scoreTotal=0
        

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
        self.scoreMoyen=moyenne/len(self.score)
        print(f"Moyenne des scores de {self.pseudo} :")
        print(moyenne/len(self.score))

    def total(self):
        total=0
        for i in self.score:
            total+=i
        self.scoreTotal=total
        print(f"Total des scores de {self.pseudo} :")
        print(total)

    def meilleur(self):
        self.meilleurScore=max(self.score)
        print(f"Meilleur score de {self.pseudo} :")
        print(max(self.score))
        print("Sur la chanson :")
        print(self.score.index(max(self.score)))
        

    def pire(self):
        print(f"Pire score de {self.pseudo} :")
        print(min(self.score))
        print("Sur la chanson :")
        print(self.score.index(min(self.score)))

class Karaoke:

    def __init__(self,joueur1:Player,joueur2:Player,joueur3:Player):
        self.player=[joueur1,joueur2,joueur3]
        self.nbPlayer=3
        self.chansons=["Camel by camel", "Gourmet Race", "Dire Dire Dock"]
        self.nbchansons=3
    
    def ajouterPlayer(self,joueur:Player):
        self.player.append(joueur)
        self.nbPlayer+=1

    def supprimerPlayer(self,nom):
        for i in self.player:
            if i.pseudo==nom:
                self.player.pop(self.player.index(i))

    def afficherplayer(self):
        for i in self.player:
            print(i.pseudo)

    def meilleurScore(self,chansons):
        for i in self.chansons:
            if i==chansons:
                num=self.chansons.index(i)
                listeScore=[]
        for j in self.player:
            listeScore.append(j.score[num])
        print(f"Le meilleur score pour la chanson {chansons} est de :")
        print(max(listeScore))
        print(f"Par le joueur {self.player[listeScore.index(max(listeScore))].pseudo}")

    def meilleurPlayerTotal(self):
        listeScore=[]
        for i in self.player:
            listeScore.append(i.scoreTotal)
        print("Le plus grand score total est de :")
        print(max(listeScore))
        print(f"Par le joueur {self.player[listeScore.index(max(listeScore))].pseudo}")

    def meilleurPlayerScore(self):
        listeScore=[]
        for i in self.player:
            listeScore.append(i.meilleurScore)
        print("Le plus grand score toute chansons confondues est de :")
        print(max(listeScore))
        print(f"Par le joueur {self.player[listeScore.index(max(listeScore))].pseudo}")

    def meilleurPlayerMoyenne(self):
        listeScore=[]
        for i in self.player:
            listeScore.append(i.scoreMoyen)
        print("Le plus grands score moyen est de :")
        print(max(listeScore))
        print(f"Par le joueur {self.player[listeScore.index(max(listeScore))].pseudo}")

if __name__=="__main__":
    def jouer(joueur:Player):
            from random import randint
            chanson=randint(0,len(joueur.score)-1)
            score=randint(50,100)
            joueur.ajouter(chanson,score)

    J1=Player("Mario")
    J2=Player("Luigi")
    J3=Player("Toad")
    J4=Player("Yoshi")
    K=Karaoke(J1,J2,J3)


    J1.affiche()
    for i in range(100):
        jouer(J1)
        jouer(J2)
        jouer(J3)
    J1.affiche()
    J1.meilleur()
    J1.pire()
    J1.moyenne()
    J1.total()

    J2.affiche()
    J2.meilleur()
    J2.pire()
    J2.moyenne()
    J2.total()

    J3.affiche()
    J3.meilleur()
    J3.pire()
    J3.moyenne()
    J3.total()

    K.meilleurScore("Gourmet Race")
    K.meilleurPlayerTotal()
    K.meilleurPlayerScore()
    K.meilleurPlayerMoyenne()

    K.afficherplayer()
    K.ajouterPlayer(J4)
    K.afficherplayer()
    K.supprimerPlayer("Yoshi")
    K.afficherplayer()