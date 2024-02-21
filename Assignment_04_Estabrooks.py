# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:43:23 2024

@author: Estabrooks
"""
#To do list
def main():
    keys=[]
    values=[]
    add= input("Would you like to add a task yes or no ")
    while (add == 'yes'):
        task= str(input("Enter task: "))
        key = str(input("Enter the number of the task "))
        keys.append(key)
        values.append(task)
        add= input("Would you like to add a task yes or no ")
        
    view= input("Would you like to view you tasks yes or no ")
    while (view == 'yes'):
        Todo = dict(zip(keys, values))
        for key, value in Todo.items():
            print(f" {key}: {value}") 
        view= "no"

main()
