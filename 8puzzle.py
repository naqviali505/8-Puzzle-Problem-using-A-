import copy
row,col=(3,3)
used=[]    
class Game:
    def __init__(self):
        self.start=[]
        self.goal=[['1','2','3'],['8','X','4'],['7','6','5']]
        self.result=[]
    def printlist(self,node):
        print("Current State")
        for i in range(row):
            for j in range(col): 
                print(node[i][j],end=' ')
            print("\n")
                
    def startgame(self):
        print("Please enter the initial state(Input X for space)")
        for i in range(row):
            temp=[]
            for j in range(col):
                initialstate=input()
                temp.append(initialstate)
            self.start.append(temp)
        
        self.result=copy.deepcopy(self.start)
        used.append(self.start)
        #self.printlist(self.result)
        print("\n")
        self.gaming()    
    def gamecalculation(self):
        temp=[]
        temporary=copy.deepcopy(self.result)
        
        x,y=self.getxy(self.result,'X')
        if x-1>=0 and x-1<=2:
            temporary[x][y],temporary[x-1][y]=temporary[x-1][y],temporary[x][y]
            temp.append(temporary)
        temporary=copy.deepcopy(self.result)
        if x+1>=0 and x+1<=2:
            temporary[x][y],temporary[x+1][y]=temporary[x+1][y],temporary[x][y]
            temp.append(temporary)
        temporary=copy.deepcopy(self.result)
        if y-1>=0 and y-1<=2:
            temporary[x][y],temporary[x][y-1]=temporary[x][y-1],temporary[x][y]
            temp.append(temporary)
        temporary=copy.deepcopy(self.result)
        if y+1>=0 and y+1<=2:
            temporary[x][y],temporary[x][y+1]=temporary[x][y+1],temporary[x][y]
            temp.append(temporary)
        var=0 
        lowest=100
        for i in temp:
            if i not in used:
                if self.fvalue(i)<lowest:
                    lowest=self.fvalue(i)
                    var=copy.deepcopy(i)          
        if var :
            used.append(var)
            self.result=copy.deepcopy(var)
                                
        print(used.__len__())
    def gaming(self):
        while (self.hvalue(self.result) !=0):
            self.gamecalculation()
            self.printlist(self.result)
      #      print("Result",self.result)      
    def getxy(self,node,data):
            for i in range(row):
                for j in range(col):    
                    if(node[i][j]==data):
                        return i,j
    def fvalue(self,src):
        fval=0
        i,j=self.getxy(self.start,'X')
        x,y=self.getxy(src,'X')
        fval=self.hvalue(src)+self.gvalue(x,y,i,j)
        return fval
    def gvalue(self,x,y,i,j):
        gval=0
        smallx=0
        largex=0
        smally=0
        largey=0
        if i>x:
            largex=i
            smallx=x
        elif i<x:
            largex=x
            smallx=i
        if j>y:
            largey=j
            smally=y
        elif j<y:
            largey=y
            smally=j
        while smallx<largex:
            gval=gval+1
            smallx=smallx+1
            
        while smally<largey:
            gval=gval+1
            smally=smally+1
        return gval
    def hvalue(self,src):
        hval=0
        for i in range(row):
            for j in range(col):
                if src[i][j]!=self.goal[i][j] and src[i][j]!='X':
                    hval=hval+1
        
        return hval+self.sumofdistance(src)+self.reversaloftiles(src)
    #no of misplaced tiles + no of reversed tiles+ euclidean distance
    def reversaloftiles(self,src):
        temp=0
        for i in range(row):
            for j in range(col):
                if(src[i][j]==self.goal[j][i] and src[j][i]==self.goal[i][j] and i!=j and src[i][j]!='X'):
                    temp=temp+1
        return temp
    def sumofdistance(self,src):
        temp=0
        for i in range(row):
            for j in range(col):
                if(self.goal[i][j]!='X'):
                    a,b=self.getxy(src,self.goal[i][j])
                    #a,b stores element index in result
                    temp+=self.gvalue(a,b,i,j)
        
        return temp
game=Game()
game.startgame()
