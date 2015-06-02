#Author: AIM
#L3Cube Assignment No: 2
#Problem Statement: Write a code that verifies - birthday paradox is indeed correct. 


#The program calculates the birthday paradox by the standard formula and also
#by finding the duplicates in the list of birthdays. It then plots a graph for both 
#the methods for comparison. It allocates random birthdays to the persons using the 
#random integer generator function


#The program takes the input from the user  for the number of persons. 
#A range N1, N2 has to be taken as input (separated by a whitespace) to calculate 
#the probabilty for N1 to N2 number of persons.


from random import randint
import matplotlib.pyplot as plt


def generate_birthday(no_persons, days):
    #This function generates the random birthdays for number of persons 
    #by assigning random days from the total number of days
    return [randint(1, days) for _ in xrange(no_persons)]

def test_by_tries(bd_list):
    #This function checks if there are duplicate birthdays in the list
    return len(set(bd_list)) < len(bd_list)

def cal_by_tries(persons, days, tries):
    #This function calculates the probability by summing up the duplicates for all tries
    #and then divides it by the number of tries
    duplicates = sum(test_by_tries(generate_birthday(persons,days)) for _ in xrange(tries))
    return duplicates/float(tries)

def probability_formula(persons, days):
    #this function calculates the probablity by the standard formula
    probability_ans = 1.0
    days = float(days)
    for i in xrange(persons):
        probability_ans *= (days - i)/days
    return 1.0 - probability_ans


#Take the input from the user to for the number of persons. 
#A range N1, N2 has to be taken as input (separated by a whitespace) to calculate 
#the probabilty for N1 to N2 number of persons
 
count=raw_input("Enter a range of values (N1, N2) to calculate the probablity for N1 to N2 number of persons\n")
count=count.split(" ")
n1=int(count[0])
n2=int(count[1])

xvalues=[]
yvalues_f=[]
yvalues_t=[]

for n in xrange(n1,n2+1):
 
    ans_by_tries=cal_by_tries(n,365,1000) #number of tries can be increased from 1000 to any value required
    ans_by_formula=probability_formula(n,365)
    print("{:d} people: {:0.4f} probability of shared birthday (exact: {:0.4f})".format(n, ans_by_tries, ans_by_formula))
	
    xvalues.append(n)
    yvalues_f.append(ans_by_formula)
    yvalues_t.append(ans_by_tries)


#This will plot the graph of calculating the probablity using formula and by number of tries
xvalues=[int(i) for i in xvalues]
yvalues_f=[float(i) for i in yvalues_f]
yvalues_t=[float(i) for i in yvalues_t]
fig=plt.figure("Birthday Paradox")
plt.xlabel("Number of persons")
plt.ylabel("Probablity")
plt.gca().set_color_cycle(['red', 'blue'])
plt.plot(xvalues,yvalues_f)
plt.plot(xvalues,yvalues_t)
plt.legend(['By formula', 'By using number of tries'], loc='upper left')
plt.show()
