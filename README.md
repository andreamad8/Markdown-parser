# About
A python implementation of a Recursive Descendent Parser for markdown sintax. 
Till now we have just considered some basic constructors, such as: 
- `#` or sequence of `#`, for the headers
- `** ciao **` for the bolt
- `* ciao *` for the italic

The parser is implemented using the following BNF grammar:
```
S -> HS | PS | e
H -> FT '\n'
F -> #F | e
T -> [a-zA-Z]*
P -> TP | IP | BP | e
I -> * G * | e
B -> ** G ** | e
G -> IBT
```
HTML code generation is going to be implement soon.
