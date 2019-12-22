import re
def getInput():
    while True:
        data = input("Please enter products:")
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0123456789 ]')
        regex2= re.compile('[-]')
        regex3 = re.compile(r'-$')
        if not (regex.search(data)==None) or (regex2.search(data)==None) or not (regex3.search(data)==None):
            print("Incorrect Format")
            continue
        else:
            break   
    return data

def conStrToList(p_str):
    p_str1 = p_str.upper()
    fruits = filter(None, p_str1.split('-'))
    return (fruits)

fr_pr=dict()
def putPrice(product_List):
    for fruit in (product_List):
        while True:
            try:
                price = float(input("Please enter the price for {} : ".format(fruit)))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                break
        fr_pr[fruit]=price
    resu = print("The Price List: \n" + "\n".join("{}\t{}".format(k, v) for k, v in fr_pr.items()))
    return resu
    
products = getInput()
p_list = conStrToList(products)
putPrice(p_list)