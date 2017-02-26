from enum import Enum

class Token(Enum):
    TXT = 1
    STA = 2 # star
    NL  = 4 # New line
    EOF = 5
    SRP = 6 # sharp


file_ = open("test.md","r")
p = file_.read(1)
current_tosk = None



def peak():
    return p

def consume():
    global p
    p = file_.read(1)



def read_txt():
    txt=''
    while(peak()!= '*' and peak()!= '\n' and peak()!= ''):
        txt+=peak()
        consume()
    return txt

def consume_token():
    global current_tosk
    if peak()=='':
        consume()
        current_tosk = (Token.EOF,"")
    elif peak()=='\n':
        consume()
        current_tosk = (Token.NL,"")
    elif peak()=='#':
        consume()
        current_tosk = (Token.SRP,"")
    elif peak()=='*':
        consume()
        current_tosk = (Token.STA,"")
    else:
        current_tosk = (Token.TXT,read_txt())

def pick_token():
    return current_tosk

def F(n):
    if pick_token()[0] ==Token.SRP:
        consume_token()
        return F(n+1)
    else:
        return n

def H():
    header_lev = F(0)
    if(pick_token()[0] == Token.TXT):
        _,section_txt = pick_token()
        consume_token()
        tok,_ = pick_token()
        if(tok == Token.NL or tok == Token.EOF):
            # print(section_txt,header_lev)
            return {"type":"Header", "h":header_lev, "txt":section_txt}
        else:
            print("ERROR_2")
    else:
        print("ERROR_1")

def G():
    if(pick_token()[0] == Token.STA):
        consume_token()
        if(pick_token()[0] == Token.STA):
            consume_token()
            return B()
        else:
            return I()
    elif(pick_token()[0] == Token.TXT):
        val= pick_token()[1]
        consume_token()
        return val
    else:
        print("ERROR MISSING TXT INSIDE G")



def I():
    node = G()
    if(pick_token()[0] == Token.STA):
        consume_token()
        #print("italic",node)
        return {"type":"italic","txt":node}
    else:
        print("MISSING STAR ITA")


def B():
    node = G()
    if(pick_token()[0] == Token.STA):
        consume_token()
        if(pick_token()[0] == Token.STA):
            consume_token()
            #print("bolt",node)
            return {"type":"bolt","txt":node}
        else:
            print("MISSING STAR BOLD")
    else:
        print("MISSING SECOND STAR BOLD")


def P(node):
    if(pick_token()[0] == Token.STA):
        consume_token()
        if(pick_token()[0] == Token.STA):
            consume_token()
            node.append(B())
        else:
            node.append(I())
        return P(node)
    elif(pick_token()[0] == Token.TXT):
        node.append(pick_token()[1])
        # print(pick_token()[1])
        consume_token()
        return P(node)
    else:
        return node


def S(AST):
    if pick_token()[0] == Token.SRP:
        AST.append(H())
        consume_token()
        return S(AST)
    elif pick_token()[0] == Token.EOF:
        print("finish")
        return AST
    else:
        AST.append(P([]))
        consume_token()
        return S(AST)

def parse():
    consume_token()
    print(S([]))


parse()
