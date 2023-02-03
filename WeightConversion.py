#Weight conversion based on the type of input provided

weight = float(input('Enter the weight : '))
type = input('Enter K/k for Kilograms and L/l for pounds : ')

trueWeight = 0

if (type == 'K' or type == 'k') :
    trueWeight = weight * 2.2
    print('Your weight in Pounds is : ', trueWeight)
elif (type == 'l' or type == 'L') :
    trueWeight  = weight / 2.2
    print('YOur weight in Kilograms is : ', trueWeight)
else :
    print("Incorrect input you illeterate piece of shit")
