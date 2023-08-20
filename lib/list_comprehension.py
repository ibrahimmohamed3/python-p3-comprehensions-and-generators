#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers
    
num_list = [1,2,3,4,5,6,78,10,90]
result = return_evens(num_list)
print(result)   
       

def make_exclamation(sentence_list):
    return_exclamation = [sentence + "!" for sentence in sentence_list]
    return return_exclamation

sentence_list = ["How are you"]
result = make_exclamation(sentence_list)
print(result)    