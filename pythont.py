import myfunctions as d

'''
age = 24
major = "computer science"
university = "ENPO"
is_male = True

if is_male:
    print("My name is Anys and i am " + str(age) + " and i just graduated from " + university + "as a" + major + "engineer")
'''

# input


# calculator
'''
one = input("enter first number\n")
two =input("enter second number\n")
operator = input("enter operator \n")

if operator.__eq__("+"): result = float(one) + float(two)
elif operator.__eq__("/"): result = float(one) / float(two)
elif operator.__eq__("*"): result = float(one) * float(two)
elif operator.__eq__("-"): result = float(one) - float(two)


print(str(result))'''

'''
#lists

list = [["D","E","A"],["A","B","A"],["A","A","I"]]
#index -1 is the last of the list
list.sort()
print(list)'''
'''
#Tuples
#immutable cant be changed
#coordonnee = (144)

#functions


def BOMBO(A,S):
    return A+S

A = input("enter\n")
B = input("enter\n")
print(BOMBO(A, B))
'''
# A= 0
# B= 0
# if A>B or A==B and A :
'''
#Dictionnaries key value pairs

Months = {
     "01" : "January"
    ,"02" : "February"
    ,"03" : "March"
    ,"04" : "April"
    ,"05" : "May"
    ,"06" : "June"
    ,"07" : "July"
    ,"08" : "August"
    ,"09" : "September"
    ,"10" : "October"
    ,"11" : "November"
    ,"12" : "December"
}

def monthtomonth(A):

     print(Months.get(A))


monthtomonth("10")
'''
# a=0
# while 1 :
#     print("|"+str(a)+"|")
#
#     a=a+1
#     if a > 5 : break


# Exceptions
# try:
#     Num = int(input("enter num \n"))
#     print(Num)
# except ValueError as err :
#     print("Hey enter a fuking number")
#     print(err)



#________READ FILES____________
# r for read | a for append | w for write (overwrite)
# file = open("textu", "w")
#
# file.write("\nOPEN THE DOOR !")
#
# file.close()

#______Modules and pip____________
# file ="C:/Users/anys/Desktop/220px-IntelliJ_IDEA_Logo.svg"
# print (d.getfilename(file))

# Object Oriented Programming

class vehicule :
    def __init__(self, Roues, passager, vitessemax, carburateur):
        self.Roues = Roues
        self.passager = passager
        self.vitessemax = vitessemax
        self.carburateur = carburateur

    def Vitessemoy(self, vehicule1, vehicule2):
        self.vehicule1= vehicule1
        self.vehicule2= vehicule2

        return (vehicule2.vitessemax+vehicule1.vitessemax)/2

class moto(vehicule) :
    def __init__(self):
        return

