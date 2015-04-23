text = input("What is your name? ")
greetings = input("How many greetings? ")
probeer = False
try: 
    getal = int(greetings)
    probeer = True
except:
    print('Vul een getal in.')
if(probeer == True):
    print(str(getal) + ' x Hello, ' + text+'!')
