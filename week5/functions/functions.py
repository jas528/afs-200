
#Python functions that accepts a string and calculate the number of upper case letters and lower case letters.

def calcCase(myString):
    upperCase = 0
    lowerCase = 0

    for character in myString: 

        if(character.isupper()):
            upperCase += 1
        else: 
            lowerCase += 1

    print('Upper Case: ' + str(upperCase))
    print('Lower Case: ' + str(lowerCase))

#Input the string: W3resource

calcCase('Python')




   #messg = [
    #lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    #lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    # lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    #lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    #result = [x for x in [i(str1) for i in messg] if x != True]
    #if not result:
        #result.append('Valid string.')
    #return result    
    #s = input("Input the string: ")