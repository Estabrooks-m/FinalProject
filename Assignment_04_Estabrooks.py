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
                
    remove= input ("Would you like to remove a task yes or no ")
    while (remove == "yes"):
        rem= input("What test would you like to get rid of (enter task number) ")
        
        if rem in Todo:
            del Todo[rem]
        remove= input ("Would you like to remove a task yes or no ")
    
    done= input("Would you like to mark a tast as done yes or no ")
    while (done == "yes"):
        complete=input("What task is done (enter the number) ")
        Todo[complete] = "Done"
        done= input("Would you like to mark a tast as done yes or no ")
    
    
    view= input("Would you like to view you tasks yes or no ")
    while (view == 'yes'):
        for key, value in Todo.items():
            print(f" {key}: {value}") 
        view= "no"
def file(Todo):
    Data= Todo
    
    
    
    
main()











