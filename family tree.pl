parent(ram,raj).
parent(rani,sunny).
parent(Lenovo,HP).

father(X,Y) :- parent(X,Y).
grandparent(X,Z) :- parent(X,Y), parent(Y,Z).

