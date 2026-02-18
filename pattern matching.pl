match([H|_],H).

second([_,S|_],S).

last([X],X).
last([_|T],X) :- last(T,X).

len([],0).
len([_|T],N) :- len(T,N1), N is N1+1.

member(X,[X|_]).
member(X,[_|T]) :- member(X,T).
