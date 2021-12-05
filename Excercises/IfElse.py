land_value = 1000000
buyer_good_credit = False
if buyer_good_credit:
    down_payment = 0.1 * land_value
else:
    down_payment = 0.2 * land_value
print(f'Your down payment is ${down_payment}')
