#!/usr/bin/python
# -*- encoding: utf8 -*-

# ----------------------------------------------------------------------
# CKY
# ----------------------------------------------------------------------

class Symbol:
    # field name: String
    # (no methods)
    
    def __init__(self, name):
        # name: String
        
        self.name = name
    
    def __str__(self):
        return self.name

class Rule:
    # field lhs: Symbol
    # field rhs: list of Symbol
    # (no methods)
    
    def __init__(self, lhs, rhs):
        # lhs: Symbol
        # rhs: list of Symbol
        
        self.lhs = lhs
        self.rhs = rhs
        
    def __str__(self):
        return str(self.lhs) + " --> [" + ",".join([str(s) for s in self.rhs]) + "]"

class Grammar:
    # field symbols: list of Symbol
    # field axiom: Symbol
    # field rules: list of Rule
    # field name: String
    # field nonTerminals: set of Symbol
    # method createNewSymbol: String -> Symbol
    # method isNonTerminal: Symbol -> Boolean
        
    def __init__(self, symbols, axiom, rules, name):
        # symbols: list of Symbol
        # axiom: Symbol
        # rules: list of Rule
        # name: String
        
        self.symbols = symbols
        self.axiom = axiom
        self.rules = rules
        self.name = name
        
        self.nonTerminals = set()
        for rule in rules:
            self.nonTerminals.add(rule.lhs)
    
    # Returns a new symbol (with a new name build from the argument)
    def createNewSymbol(self, symbolName):
        # symbolName: String
        
        name = symbolName
        
        ok = False
        while (ok == False):
            ok = True
            for s in self.symbols:
                if s.name == name:
                    ok = False
                    continue
            
            if ok == False:
                name = name + "'"
        
        return Symbol(name)
        
    def isNonTerminal(self, symbol):
        # symbol: Symbol
        
        return symbol in self.nonTerminals
        
    def __str__(self):
        return "{" +\
            "symbols = [" + ",".join([str(s) for s in self.symbols]) + "]; " +\
            "axiom = " + str(self.axiom) + "; " +\
            "rules = [" + ", ".join(str(r) for r in self.rules) + "]" +\
            "}"

# Definition of the symbols
symS = Symbol("S")
symA = Symbol("A")
symB = Symbol("B")
symTerminalA = Symbol("a")
symTerminalB = Symbol("b")

# Definition of two grammars

g1 = Grammar(
    # Alphabet
    [symS, symA, symB, symTerminalA, symTerminalB],
    
    # Axiom
    symS,
    
    # List of rules
    [
        Rule(symS, [symA, symB]),                 # S --> AB
        Rule(symS, [symTerminalA]),                 # S --> a
        Rule(symA, [symS, symB]),                 # A --> SB
        Rule(symA, [symTerminalB]),                 # A --> b
        Rule(symB, [symTerminalB])                 # B --> b
    ],
    
    # name
    "g1"
)

g2 = Grammar(
    # Alphabet
    [symS, symA, symTerminalA, symTerminalB],
    
    # Axiom
    symS,
    
    # List of rules
    [
        Rule(symS, [symA, symS]),                 # S --> AS
        Rule(symS, [symTerminalB]),                 # S --> b
        Rule(symA, [symTerminalA])                 # A --> a
    ],
    
    # name
    "g2"
)


# ----------------------------------------------------------------------
# Version minimale de l'algorythme CYK
#
# Soit u un mot de longueur n ; pour 0 =< i < j <= n,
# T[i, j] est l'ensemble des non-terminaux A tels qu'il existe
# une dérivation de A vers le sous-mot 'u[i] u[i+1] ... u[j-1]'
# (i.e. A -->* u[i] ... u[j-1])
# ----------------------------------------------------------------------

print("Question 1 : création de la table d'analyse")
print("")

"Création et initialisation de la table T pour le mot u et la grammaire gr"
def init(u, gr):
    T = []
    for i in range(len(u)): #création d'une matrice de listes de listes
        T.append([[] for i in range(len(u))])

    for i in range(len(u)): #remplissage horizontal de la première ligne de la matrice pour un mot u donné
        table = T[0] 
        for k in gr.rules: 
            for c in k.rhs:
                if u[i] == c.__str__():
                    table[i].append(k.lhs.__str__()) 
    #la partie gauche (symbole non terminal) est ajoutée à une liste sur la première ligne de la matrice selon l'indice dans le mot
    return T


"Remplissage de la table T (initialisation déjà effectuée) pour le mot u et la grammaire gr"
def loop(T, u, gr): #insérer ici algorithme CKY qui parcoure la table diagonalement afin d'analyser si u est généré par gr
    
    
                   
            
            
        
            
                        
    
    

"Création de la table d'analyse du mot u pour la grammaire gr"
def buildTable(u, gr):
    T = init(u, gr)
    loop(T, u, gr)
    
    return T    

"Affichage d'une table T pour un mot de taille n"
def printT(T, n):
    for i in range(n):
        print(T[i])

#printT(buildTable("bb", g1), 2)

# ----------------------------------------------------------------------
# L'algo est entièrement codé dans les trois fonctions précédentes, les
# fonctions qui suivent servent uniquement à afficher les résultats,
# et à réaliser facilement quelques tests
# ----------------------------------------------------------------------

print("")
print("Question 2 : interprétation de la table d'analyse")
print("")

"Une fois la table T remplie, détermine si l'analyse a réussi"
def isSuccess(T, u, gr):
    if T[len(u)-1][0] == gr.axiom: #voit si la première case de la dernière ligne correspond à l'axiome de la grammaire gr
        return True
    else:
        return False

"Une fois l'analyse effectuée, retrouve et affiche l'arbre syntaxique à partir de la table"
def printTree(T, u, gr):
    for i in range(n):
        for j in range(i, n+1):
            print(str((i,j)) + ": " + ", ".join(str(s) for s in T[i]))

"Vérifie que la grammaire est en forme normale de Chomsky"
def checkCNF(gr):
    for r in gr.rules:
        if (len(r.rhs) > 2):
            return False 
        else:
            if (((len(r.rhs) == 1) and (r.rhs[0].__str__() == r.rhs[0].__str__().lower())) or ((r.rhs[0].__str__() == r.rhs[0].__str__().upper()) and (r.rhs[1].__str__() == r.rhs[1].__str__().upper()) and (len(r.rhs) == 2))):
                return True
            else:
                return False
       


"Fonction globale d'analyse syntaxique"
def parse(u, gr):
    print("--- \"" + u + "\" - " + gr.name + " ---")
    
    if not checkCNF(gr):
        print("la grammaire n'est pas en forme normale de Chomsky!")
    
    T = buildTable(u, gr)
    
    print("table d'analyse :")
    printT(T, len(u))
    print("")
    
    
    if isSuccess(T, u, gr):
        print("le mot est généré par la grammaire")
        print("")
        print("arbre :")
        printTree(T, u, gr)
    else:
        print("le mot N'est PAS généré par la grammaire")


