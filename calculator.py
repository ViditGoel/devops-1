#CALCULATOR:
#FEATURE
import sys

class claculator_tool:
    def __init__(self, A):
        self.A = A
    
    def addition(self):
        print("SUM: {A}".format(A=sum(self.A)))
    
    def multiplication(self):
        if len(self.A)==1:
            print(self.A[0])
        
        if len(self.A)==2:
            print(self.A[0]*self.A[1])

        if len(self.A)>2: 
            k=self.A[0]*self.A[1]
            for i in range(2,len(self.A)):
                k=k*self.A[i]
            
            print("MULTIPLICATION: {A}".format(A=k))



if __name__=="__main__":
    obj=claculator_tool(list(map(int,sys.argv[1].rstrip().split(","))))
    obj.addition()
    obj.multiplication()