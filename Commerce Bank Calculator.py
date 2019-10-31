#  A PROGRAM TO CALCULATE HOW  MUCH I'VE SPENT
sDollars = ""
sDecimals = ""
dollars = 0
decimals = 0
string = input()
while string != "End":
    if "-$" in string:
        smallerlist = string.split(".")
        for i in smallerlist[0]:
            if i.isdigit():
                sDollars += i
        for i in smallerlist[1]:
            if i.isdigit():
                sDecimals += i
    if sDollars:
        dollars += int(sDollars)
    if sDecimals:
        decimals += int(sDecimals)
    sDollars = ""
    sDecimals = ""
    string = input()
sum = dollars + decimals/100
print("Your sum is:", sum)