# Phantom
Phantom is a (in development) game of Chess written in Python.  It's not very graphical but what it does have at the moment is the ability to pretty-print the board to the screen, ex:
```
  a b c d e f g h
8 r n b q k b n r 8
7 p p p p p p p p 7
6                 6
5                 5
4                 4
3                 3
2 P P P P P P P P 2
1 R N B Q K B N R 1
  a b c d e f g h
```
and will use Unicode characters as well.  A proper GUI is underway for the iOS app [Pythonista][].  

Please note: this project is a huge learning experience for me.  This is the 3rd revision (I've restarted from scratch twice) of my ongoing chess project, each one getting better.  Hopefully there is no 4th revision.  If you find a bug, *please* don't hesitate to let me know so I can fix it.

Things that it lacks:
- Checkmate detection  (work-in-progress)
- Analysis engine  (work-in-progress)
- Descriptive game notation

Things that work:
- Move validation
- Pretty printing
- Save/load boards
- Read/write FEN strings
- Algebraic chess notation

[Pythonista]: http://omz-software.com/pythonista