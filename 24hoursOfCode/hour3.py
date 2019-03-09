total = 15.23 + 17.19 + 14.00 + 11.25 + 13.50 + 11.00
party = 0


try:
    average_ticket = total / party
    print('Here is your receipt for your meal: ')
    if party >= 5:
        total = total + total * .2
        print('We have added your tip in since you had ' + str(party) + ' in your party!')

    print('Thank you for dining with us! Your total is: $', total)
    print('Have a great day!')
except:
    print('There was an error')
