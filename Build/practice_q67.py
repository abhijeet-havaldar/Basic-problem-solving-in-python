#Q:Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter
#  of mercury (mmHg) and atmosphere pressure.


kpa = float(input("Input pressure in kilopascals:"))

psi = kpa / 6.89475729

mmhg = kpa * 760 / 101.325

atm = kpa / 101.325

print("The pressure in pounds per squre inch: %.2f psi"%(psi))

print("The pressure in milimeters of murcury: %.2f mmhg"%(mmhg))

print("Atomosphere pressure :%.2f atm "%(atm))