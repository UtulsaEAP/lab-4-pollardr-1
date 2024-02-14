"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Riley Pollard
Lab Time: Thursday 2pm lab, wednesday class
"""

def inc_5():
    # Write your code here
    i = int(input())
    j = int(input())
    group = ''
    if i>j:
        print("Second integer can't be less than the first.")
    else:

        while i<=j:
            group += str(i) + ' '
            i += 5
        print(group + ' ')

if __name__ == '__main__':
    inc_5()