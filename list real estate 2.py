
#Peter Golenev List and Real Estate

# Defining Float function

def getFloatInput(sPrompt):
    while True:
        try:
            fInput = float(input(sPrompt))
            if fInput > 0:
                return fInput
            else:
                print("Enter a number that is greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Function to find the Median

def getMedian(fSalesPrice):
    fSalesPrice.sort()
    sMedian = len(fSalesPrice)
    mid = sMedian // 2

    if sMedian % 2 == 0:
        return (fSalesPrice[mid - 1] + fSalesPrice[mid]) / 2
    else:
        return fSalesPrice[mid]


#Meat and Potatoes
def main():
    sValues = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        sValues.append(fSalesPrice)

        while True:
            sBool = input("Enter another value Y or N: ").upper()
            if sBool in ['Y', 'N']:
                break
            else:
                print("Error: Please Enter Y or N.")

        if sBool == 'N':
            break

    sValues.sort()
    
#Calculations
    
    iMin = sValues[0]
    iMax = sValues[-1]
    iSum = sum(sValues)
    fAvg = iSum / len(sValues)
    iMed = getMedian(sValues)
    iCom = iSum * 0.03
    
#List Creation Output 
    iNumber = 1
    for value in sValues:
        print(f"Property {iNumber} $ {value:16.2f}")
        iNumber += 1
#Standard Output
    print(f"{'Minimum:':15} {'$':2}{iMin:13.2f}")
    print(f"{'Maximum:':15} {'$':2}{iMax:13.2f}")
    print(f"{'Total:':15} {'$':2}{iSum:13.2f}")
    print(f"{'Average:':15} {'$':2}{fAvg:13.2f}")
    print(f"{'Median:':15} {'$':2}{iMed:13.2f}")
    print(f"{'Commission:':15} {'$':2}{iCom:13.2f}")
    

#Start
main()
