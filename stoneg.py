import random
l2=["stone","paper","scissor"]
rounds =int(input("enter the rounds"))
i=1
umark=0
cmark=0
while(i<=rounds):
    uchoice=input("enter your choice [stone,paper,scissors]")
    cchoice=random.choice(l2)
    print("computer choice:")
    print(cchoice)
    if(uchoice=="stone" and cchoice=="stone"):
            umark=umark+0
            cmark=cmark+0
    if(uchoice=="stone" and cchoice=="paper"):
            cmark=cmark+1
    if(uchoice=="stone" and cchoice=="scissor"):
            umark=umark+1
    if(uchoice=="paper" and cchoice=="paper"):
            umark=umark+0
            cmark=cmark+0
    if(uchoice=="paper" and cchoice=="stone"):
            umark=umark+1
    if(uchoice=="paper" and cchoice=="scissor"):
            cmark=cmark+1
    if(uchoice=="scissor" and cchoice=="scissor"):
            umark=umark+0
            cmark=cmark+0
    if(uchoice=="scissor" and cchoice=="paper"):
            umark=umark+1
    if(uchoice=="scissor" and cchoice=="stone"):
            cmark=cmark+1
    i=i+1
print("your mark")
print(umark)
print("computer mark:")
print(cmark)
if(cmark>umark):
    print("YOU LOSS")
else:
       print("YOU WIN")