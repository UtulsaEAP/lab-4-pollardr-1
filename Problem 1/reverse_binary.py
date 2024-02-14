"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Riley Pollard
Lab Time: Thursday 2pm lab, Wednesday class

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binary_val = ''
#write your while loop here
    while user_num > 0:
        #write your code
        placement = user_num %2
        binary_val += str(placement)
        user_num = user_num // 2
        


    print(binary_val)

if __name__ == "__main__":
    reverse_binary()


    