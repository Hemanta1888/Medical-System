# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:46:12 2021

@author: Hemant
"""

class PriorityQueue:
    def __init__(self,queue=[]):
        self.priorityqueue = queue
    def insert(self):
        n = int(input(name+',Please enter the number of patients you want to admit: '))
        if n <=10:
            for i in range(n):
                a = int(input('Enter the patient emergency level: '))
                b = input('Enter the patient name: ')
                self.priorityqueue.append((a,b))
            print("The patients are:\n"+str(self.priorityqueue))
            que = input("Do you want to treatment the patient[yes/no]: ")
            if que == 'yes':
                return str(PriorityQueue.treat_first(self))
            elif que == 'no':
                print("It's fine.Later, you can treat the patient.")
                return 'Stay safe & Stay healthy.'
        else:
            return "Sorry, We can add " + str(n)+" patients to our medical."
    def treat_first(self):
        self.priorityqueue.sort()
        return 'The emergency patient is to treat : '+str( self.priorityqueue.pop()[1])
    def __str__(self):
        if len(self.priorityqueue) == 0:
            print(f"{name},rightnow you have listed zero medical name.")
            que = input('Do you want to list medical name[yes/no]: ')
            if que  == 'yes':
                medical = input('Enter the medical name please: ')
                print(f"{name}, Your medical name is '{medical.title()}'.")
                Que = input('Do you want to admit patients into your medical[yes/no]: ')
                if Que == 'yes':
                    return str(PriorityQueue.insert(self))
                elif Que == 'no':
                    return 'This means you have no patients rightnow.'
                else:
                    return 'Sorry to say, you choose wrong option.'
            elif que == 'no':
                return 'Bye.....See you soon....'
            else:
                return "Sorry, I didn't get it. Please try again."
        else:
            return 'The patient list are...\n'+str(self.priorityqueue)
    
p = PriorityQueue()
print('I have created a medical admit system where the emergency patient will admit first.')
name = input('Enter your name please: ').capitalize()
print(p)