"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Riley Pollard
Lab Time: Thursday 2pm lab, wednesday class
"""

def norm():
    # Write your code here
    number_floats = int(input())
    numarr = {}
    highnum = float(0)
    for x in range (0,number_floats):
        numarr[x] = float(input())
    
    highnum = numarr[0]
    for x in range (1,number_floats):
        if highnum < numarr[x]:
            highnum = numarr[x]
    for x in range (0,number_floats):
        numarr[x] /= highnum 
        print(f'{numarr[x]:.2f}')

if __name__ == "__main__":
    norm()