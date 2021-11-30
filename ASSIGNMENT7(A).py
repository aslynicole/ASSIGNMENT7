import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
columns = shutil.get_terminal_size().columns

print(bcolors.HEADER + "HELLO!".center(columns))
print(bcolors.OKGREEN + "WELCOME TO CHARACTER COUNTER".center(columns) + bcolors.OKBLUE + bcolors.ENDC )


# Create a program that ask for a sentence as input.
userInput = (input("\nWrite or paste your sentence here: "))
vowels = 0
consonants = 0
letters = 0
words = 1

# code that count letters
for i in range(0, len(userInput)):  
    if(userInput[i] != ' '):  
        letters = letters + 1;  


# code that count words
for i in range(len(userInput)):
    if(userInput[i]==' ' or userInput == '/n' or userInput == '\f'):
        words = words + 1


# code that count consonants and vowels
for i in range(0,len(userInput)):   
    #Checks whether a character is a vowel  
    if userInput[i] in ('a',"e","i","o","u",'A',"E","I","O","U")  :  
        vowels = vowels + 1;  
    #Checks whether a character is a consonant
    elif (userInput[i] >= 'a' and userInput[i] <= 'z'):
        consonants = consonants + 1;  
    elif (userInput[i] >='A' and userInput[i] <='Z'):  
        consonants = consonants + 1;  
# Display the number of words, vowels and consonants in the input 
print("\nTotal number of letters:", letters);  
print("Total number of words: ",words)
print("Total number of vowels:",vowels)
print("Total number of consonant:",consonants)