import random

a=[0,1,2,3,4]
b=[0,1]
print ('      BATTLESHIP!')
board=[]
flag=0
def print_board(board_in):
    for i in board:
        print ("           ".join(i))
n=int(input('Enter your choice:\n1.Play game\n2.Quit\n'))
while(n!=2):
    for i in range(0,5):
        board.append(['O']*5)
    print ('**********************')
    print ('Welcome to Battleship!')
    print ('This your board layout.')
    print_board(board)
    print ('There is 1 boat hidden in the grid.\nThe boat occupies 3 blocks.\nYou have 10 turns to find it.')
    r1=random.choice(a)
    c1=random.choice(a)
    ori=random.randint(0,2)
    r2,r3,c2,c3=0,0,0,0
    if(ori==0):
        c2=c1
        c3=c1
        if(r1==0):
          r2=1
          r3=2
        elif(r1==4):
          r2=3
          r3=2
        else:
          r2=r1-1
          r3=r1+1
    elif(ori==1):
        r2=r1
        r3=r1
        if(c1==0):
          c2=1
          c3=2
        elif(c1==4):
          c2=3
          c3=2
        else:
          c2=c1-1
          c3=c1+1
    count=0
    for turn in range(1,11):
        print ('Turn Number: ',turn)
        ur=int(input('Enter row: '))
        uc=int(input('Enter column: '))
        if((ur-1==r1 and uc-1==c1)or(ur-1==r2 and uc-1==c2)or(ur-1==r3 and uc-1==c3)):
            count=count+1
            board[ur-1][uc-1]='H'
            if(count!=3):
                print ('You got a hit!')
                print_board(board)
            else:
                print ('Congratulations!\nYou sunk my Battleship!')
                flag=1                
                print_board(board)
                break
        else:
            if(ur-1 not in range(0,5) or uc-1 not in range(0,5)):
                print ('That is not even in the ocean!')
            elif(board[ur-1][uc-1]=='M'):
                print ('You already tried that!Take another guess.')
                turn-=1
            else:
                print ('You missed it...')
                board[ur-1][uc-1]='M'
                print_board(board)
    if(flag==0):
        print ('The ship was at: ('+str(r1+1)+','+str(c1+1)+'),('+str(r2+1)+','+str(c2+1)+'),('+str(r3+1)+','+str(c3+1)+')')
    board=[]
    n=int(input('Enter your choice:\n1.Play game\n2.Quit\n'))
if(n==2):
    print ('GOODBYE!')
