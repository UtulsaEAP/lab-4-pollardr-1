"""
Complete the following python code to reverse the string entered by the user.

Name: Riley Pollard
Lab Time: Thursday 2pm lab, wednesday class
"""

def reverse_string():
    # YOUR CODE HERE
    
    output = ''
    length = 0
    word = input()
    outputfinal = ''
    while word != 'done' and word != 'Done' and word != 'd':
        
        
        while length < len(word):
            output += word[len(word)-length-1]
            length += 1
        outputfinal += output + '\n'
        word = input()
        output = ''
        length = 0

    print(outputfinal)
if __name__ == "__main__":
    reverse_string()