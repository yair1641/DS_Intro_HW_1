
 #Q1
def my_func(x1= float, x2= float, x3= float):
    if type(x1)==float and type(x2)==float and type(x3)==float:
        if (x1 + x2 + x3) != 0:
            solution= ((x1+x2+x3)*(x2+x3)*(x3))/(x1+x2+x3)
            return solution
        else:
            print("Not a number – denominator equals zero")
    else:
         print("Error: parameters should be float")

#Q2

import math
def  convert(hours, minutes):
    if type(hours)==float or type(hours)==int and type(minutes)==float or type(hours)==int and hours > 0  and minutes > 0 :
        h= math.modf(hours)
        numofminutes= h[0]*60
        numofhours= h[1]
        secmin= numofminutes*60
        sechours= numofhours*3600
        secfromminutes=minutes*60
        numofseconds= secmin+sechours+secfromminutes
        return numofseconds
    else:
        print("Input error!")



