weight = float(input("Enter Your Weight: "))
type_of_weight = input("Enter the units, L(for Pounds) or K(for kilograms): ")

if type_of_weight.upper() == 'L':
    weight_in_kg = weight * 0.454
    print(f'Your weight is {weight_in_kg} kilograms')

elif type_of_weight.upper() == 'K':
    weight_in_lbs = weight * 2.205
    print(f'Your weight is {weight_in_lbs} lbs')

else:
    print("Enter Correct Value of Units")