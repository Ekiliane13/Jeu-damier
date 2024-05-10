import random

class Case:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    
    def _str_(self):
        return f"({self.x}, {self.y})"

    def _eq_(self, other):
        return self.x == other.x and self.y == other.y

class Creature:
    def _init_(self, nom, position):
        self.nom = nom
        self.position = position
    
    def _str_(self):
        return f"Creature {self.nom} en position {self.position}"

class Jeu:
    def _init_(self, taille):
        self.listeDesCases = [Case(x, y) for x in range(taille) for y in range(taille)]
        self.listeDesCreatures = []
        self.tour = 0
        self.actif = None
    
    def _str_(self):
        return f"Tour {self.tour}, Actif : {self.actif}\nCases : {', '.join(str(case) for case in self.listeDesCases)}\nCreatures : {', '.join(str(creature) for creature in self.listeDesCreatures)}"

    def estOccupee(self, case):
        for creature in self.listeDesCreatures:
            if creature.position == case:
                return True
        return False
    
    def adjacentes(self, case):
        adj = []
        for c in self.listeDesCases:
            if abs(c.x - case.x) <= 1 and abs(c.y - case.y) <= 1 and c != case:
                adj.append(c)
        return adj
    
    def choisirCible(self, creature):
        adj = self.adjacentes(creature.position)
        occupees = [case for case in adj if self.estOccupee(case)]
        if occupees:
            return random.choice(occupees)
        else:
            return random.choice(adj)
    
    def deplacer(self, creature, case):
        if case in self.adjacentes(creature.position):
            if self.estOccupee(case):
                print(f"{creature.nom} a capturé la case occupée par une autre créature et a gagné!")
                return True
            else:
                creature.position = case
                self.tour += 1
                self.actif = self.listeDesCreatures[self.tour % len(self.listeDesCreatures)]
                return False
        else:
            print("Déplacement non autorisé.")
            return False

# Initialisez le plateau de jeu
jeu = Jeu(4)
creature1 = Creature("A", jeu.listeDesCases[0])
creature2 = Creature("B", jeu.listeDesCases[-1])
jeu.listeDesCreatures.extend([creature1, creature2])
jeu.actif = creature1

# Affrontement des créatures jusqu'à ce qu'une gagne
while True:
    print(jeu)
    cible = jeu.choisirCible(jeu.actif)
    if jeu.deplacer(jeu.actif, cible):
        break