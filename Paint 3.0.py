
#Peter GOlenev Paint

#Defining Float Input
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

# Def Function + Math

def getGallonOfPaint(fSqFeetOfWall, fSqFeetPerGallon):
    import math
    iGallons = math.ceil(fSqFeetOfWall / fSqFeetPerGallon)
    return iGallons

def getLaborHours(fLaborHoursPerGallon, iGallons):
    fLaborHours = fLaborHoursPerGallon * iGallons
    return fLaborHours

def getLaborCost(fLaborHours, fLaborChargePerHour):
    fLaborCost = fLaborHours * fLaborChargePerHour
    return fLaborCost

def getPaintCost(fPaintPrice, iGallons):
    fPaintCost = fPaintPrice * iGallons
    return fPaintCost

def getSalesTax(sState):
    taxRates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return taxRates.get(sState.upper(), 0.0)

def showCostEstimate(sCustomer, fSquareFeetWall, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sState, iGallons, fLaborHours, fLaborCost, fPaintCost, sTaxRate, fTotalCost):
    print(f"Cost Estimate for {sCustomer}")
    print(f"Square Feet of the Wall: {fSquareFeetWall}")
    print(f"Paint Price: ${fPaintPrice}")
    print(f"Feet per Gallon of Paint: {fFeetPerGallon}")
    print(f"Labor Hours per Gallon: {fLaborHoursPerGallon}")
    print(f"Painting Labor charge per hour: ${fLaborChargePerHour}")
    print(f"State: {sState}")
    print(f"Gallons of Paint Needed: {iGallons}")
    print(f"Labor Hours: {fLaborHours}")
    print(f"Labor Cost: ${fLaborCost:.2f}")
    print(f"Paint Cost: ${fPaintCost:.2f}")
    print(f"Sales Tax Rate: {sTaxRate * 100}%")
    print(f"Total Cost: ${fTotalCost:.2f}")
    
# Creating File
    fileName = f"{sCustomer}_PaintJobOutput.txt"
    with open(fileName, "w") as file:
        file.write(f"Cost Estimate for {sCustomer}\n")
        file.write(f"Square Feet of the Wall: {fSquareFeetWall}\n")
        file.write(f"Paint Price: ${fPaintPrice}\n")
        file.write(f"Feet per Gallon of Paint: {fFeetPerGallon}\n")
        file.write(f"Labor Hours per Gallon: {fLaborHoursPerGallon}\n")
        file.write(f"Painting Labor charge per hour: ${fLaborChargePerHour}\n")
        file.write(f"State: {sState}\n")
        file.write(f"Gallons of Paint Needed: {iGallons}\n")
        file.write(f"Labor Hours: {fLaborHours}\n")
        file.write(f"Labor Cost: ${fLaborCost:.2f}\n")
        file.write(f"Paint Cost: ${fPaintCost:.2f}\n")
        file.write(f"Sales Tax Rate: {sTaxRate * 100}%\n")
        file.write(f"Total Cost: ${fTotalCost:.2f}\n")
    
    print(f"File '{fileName}' created with the cost estimate.")
# Info
def main():
    fSquareFeetWall = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter Paint Price: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ")
    sCustomer = input("Customer Last Name: ")

    iGallons = getGallonOfPaint(fSquareFeetWall, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(fPaintPrice, iGallons)
    fTaxRate = getSalesTax(sState)
    fTotalCost = fLaborCost + fPaintCost + (fPaintCost * fTaxRate)

    showCostEstimate(sCustomer, fSquareFeetWall, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sState, iGallons, fLaborHours, fLaborCost, fPaintCost, fTaxRate, fTotalCost)

if __name__ == "__main__":
    main()
