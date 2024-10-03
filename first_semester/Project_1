# -*- coding: utf-8 -*-

'''
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
    – takes as parameters 
      a string (int_seq) and a positive integer (subtotal >= 0), and 
    – returns the number of substrings of int_seq such that 
      the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
    elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,0,5,0,4,2' and subtotal = 9, 
    the function should return 7. The following substrings, indeed, consist of
    values whose sum is equal to 9:
    int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
            => _'0,4,0,3,1,0,1,0'_____________
               _'0,4,0,3,1,0,1'_______________
               ___'4,0,3,1,0,1,0'_____________
               ___'4,0,3,1,0,1'_______________
               ___________________'0,0,5,0,4'_
             _____________________'0,5,0,4'_
                 _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
    1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)
'''

def ex1(int_seq, subtotal):
    #transfrom the string into a list of integers
    int_list = list(map(int, int_seq.split(',')))
    
    #for every single possible solution I have to increase this, for every 
    #zero in the list near one solution increase also by 1
    total_possibilities = 0
    
    #if all are one or zero is easy to calculate, so for more efficient code 
    #its better to calculate like this
    
    if int_list.count(1) == len(int_list) and subtotal <= len(int_list):
        total_possibilities = len(int_list) - subtotal + 1
        
    elif int_list.count(0) == len(int_list) and subtotal > 0:
        total_possibilities = 0
    
    else:
        #loops through every value
        for index in range(len(int_list)):
            #resets the partial sum so that it can be done and compared for every loop
            partial_sum = 0
            #loops for every value every value, so it can check one by one
            for index_2 in range(index, len(int_list)):
                #adds to the partial sum
                partial_sum += int_list[index_2]
                
                if partial_sum == subtotal:
                    #if the adding reaches the partial sum thats one possibility
                    total_possibilities += 1
                    
                elif partial_sum > subtotal:
                    break
                
    return total_possibilities
    
if __name__ == '__main__':
    pass
    

    

