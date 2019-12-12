{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

def question_1():
    """This function prints out the first question and choices and takes in a letter input"""

    #print out question and 4 choices
    print ("Choose a type of batter")
    print ("a)red velvet")
    print ("b)vanilla")
    print ("c)funfetti")
    print ("d)swirled")
    
    #takes a letter answer as the input and stores it in a variable
    question_1.answer = input("Enter the letter of your answer here: ")
    
def question_2():
    """This function prints out the second question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("What kind of baking cup?")
    print ("a)plain white")
    print ("b)rainbow stripes")
    print ("c)polka dots")
    print ("d)animal print")
    
    #takes a letter answer as the input and stores it in a variable
    question_2.answer = input("Enter the letter of your answer here: ")

def question_3():
    """This function prints out the third question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("Choose a filling")
    print ("a)cream cheese")
    print ("b)chocolate")
    print ("c)caramel")
    print ("d)candy/sprinkles")
    
    #takes a letter answer as the input and stores it in a variable
    question_3.answer = input("Enter the letter of your answer here: ")
    
def question_4():
    """This function prints out the fourth question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("What kind of icing?")
    print ("a)cream cheese")
    print ("b)vanilla")
    print ("c)chocolate")
    print ("d)strawberry")
    
    #takes a letter answer as the input and stores it in a variable
    question_4.answer = input("Enter the letter of your answer here: ")
    
def question_5():
    """This function prints out the fifth question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("What kind of sprinkles?")
    print ("a)star shaped")
    print ("b)rainbow")
    print ("c)chocolate")
    print ("d)no sprinkles")
    
    #takes a letter answer as the input and stores it in a variable
    question_5.answer = input("Enter the letter of your answer here: ")
    
def question_6():
    """This function prints out the sixth question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("Choose a sauce to drizzle on top")
    print ("a)caramel")
    print ("b)chocolate")
    print ("c)stawberry")
    print ("d)none for me thanks")
    
    #takes a letter answer as the input and stores it in a variable
    question_6.answer = input("Enter the letter of your answer here: ")
    
def question_7():
    """This function prints out the seventh question and choices and takes in a letter input"""
    
    #print out question and 4 choices
    print ("Choose something to top it all off")
    print ("a)coconut flakes")
    print ("b)fruit")
    print ("c)chocolate bar")
    print ("d)no topping for me thanks")
    
    #takes a letter answer as the input and stores it in a variable
    question_7.answer = input("Enter the letter of your answer here: ")
    
def question_prompt():
    """This function runs the first part of the quiz and prints out all the functions"""

    #prints out an introduction to the quiz
    print("Hi! Answer these questions and build your own cupckae to find out your best personality trait!")

    #runs all the question functions
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()

    #puts all the inputs into a list so that the score can be calculated in a function
    all_answers = [question_1.answer, question_2.answer, 
                   question_3.answer, question_4.answer, 
                   question_5.answer, question_6.answer, question_7.answer]

    return all_answers


class ScoreCountClass():
    """Class calculates the score from all the answers from the prompt"""

    #takes the input from the answers
    def __init__(self, the_answers):
        self.answers = the_answers
    
    #runs a loop that calculates the total score
    def score_count(self):
        score = 0
        for answer in self.answers:
            if answer == "a":
                score += 1
            elif answer == "b":
                score += 2
            elif answer == "c":
                score += 3
            elif answer == "d":
                score += 4
        return score
    
    
#prints out the result of best trait using conditionals depending on the score calculated above
def score_results(score):
    if score <= 7:
        print("Your best trait is your positive energy! You never cease to radiate happiness to those around you, and your friends definitely keepy you around for your bright smile!")
    elif 7 < score <= 14:
        print("Your best trait is your sense of humour! You never cease to make your friends laugh, and they definitely like to keep you around for your hilarious jokes!")
    elif 14 < score <= 21:
        print("Your best trait is your intelligence! You never cease to amaze others at how well you do in your school work, no matter what subject, you seem to pick it up like a natural!")
    elif 21 < score <= 28:
        print("Your best trait is your compassion! You connect with everyone so well and never cease to amaze others with your kindness, no matter who it may be shown towards!")
    elif 28 < score <= 35:
        print("Your best trait is your tenacity! No matter what problem is at hand, you face it head on and do not give up until the job is done!")
    elif 35 < score <= 42:
        print("Your best trait is your independence! You don't need to rely on others to get the job at hand done. You have lived a lot of your life alone, and you don't mind it one bit!")
    elif 42 < score:
        print("Your best trait is your openness! You are always so easy for others to talk to, and always open to new experiences and to hear other people's perspectives on every situation.")

        
def take_quiz():
    """This function runs all the steps and performs the entire chatbot"""

    #first prints out the questions and takes in the inputs
    answer = question_prompt()
    
    #takes the list of answers and runs them in a loop to calculate score
    score_c = ScoreCountClass(answer)
    score = score_c.score_count()
    
    #takes the score and prints out result of quiz
    score_results(score)
    
    