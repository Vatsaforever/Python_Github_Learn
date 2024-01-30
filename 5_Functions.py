def dollarizer(word)-> str:
    return word.replace("s","$").replace("S","$")
print(dollarizer("sensei"))
def Euroriser(word)-> str:
    return word.replace("e","€").replace("E","€")
print(Euroriser("Euthnaise"))
def replacer(word, char1, char2):
    return word.replace(char1,char2)
print(replacer("Negotiate","e","€"))
def wonky_text(word):
    word = dollarizer(word)
    word = Euroriser(word)
    word = replacer(word,"l","£")
    return word
print(wonky_text("Constantinples"))
def celsius_to_farenheit(temp)-> float:
    Temp_in_Farenheit = (temp*(9/5))+32
    return Temp_in_Farenheit
print(celsius_to_farenheit(32))
def age_in_days(age)-> int:
   return (age*365)
print(age_in_days(35)) 
def simple_int(PA, ROI, T)-> int:
    return(PA*(ROI/100)*T)
print(simple_int(1300000,8,5))
def plan_finances(PA, ROI, T , DA) -> float:
    if (simple_int(PA, ROI, T)) + PA >= DA:
        return("Target acheived")
    else:
        return("Target Failed")
print(plan_finances(1300000,8,5,1800000))