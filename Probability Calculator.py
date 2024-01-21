import random
import copy



class Hat:
  def __init__(self,**kwargs):
      self.contents=[]
      for k,v in kwargs.items():# posso somar listas em python
          self.contents+=[k]*v # estou add k v vezes na lista self.contents



  def draw(self,balls):
        checar=[]
        self.removidas=[]

        if len(self.contents)>=balls: #retirar as bolas do chapéu de maneira aleatório

           c=0
           while c!=balls:

              n_aleatorio=random.randint(0,(len(self.contents)-1))
              if n_aleatorio not in checar:
                  self.removidas.append(self.contents[n_aleatorio])
                  self.contents.remove(self.contents[n_aleatorio])#remove a bola tirada da lista content

                  checar.append(n_aleatorio)
                  c+=1
           return self.removidas


        else:
            return self.contents

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    queremos=[]
    experimentos=0

    M=0
    N=num_experiments
    nosso_chapeu=copy.deepcopy(hat)
    removidas=nosso_chapeu.draw(num_balls_drawn)
    for k,v in expected_balls.items():
        queremos+=[k]*v

    while experimentos <num_experiments:
        c=0
        nosso_chapeu=copy.deepcopy(hat)#fazer uma cópia independente do objeto
        removidas=nosso_chapeu.draw(num_balls_drawn) 
        for b in expected_balls.keys():#comparação para ver se o caso nos interessa
            if  removidas.count(b)>=expected_balls[b]:
                c+=1    
            if c == len(expected_balls):
                M+=1    

        experimentos+=1 

    probabilidade=M/N

    return print(probabilidade)
        
         
    
#hat=Hat(blue=3,red=2,green=6)
#experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
hat=Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

                 
        
    
    
    
    
                        