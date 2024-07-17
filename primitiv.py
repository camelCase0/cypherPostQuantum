def normalize(poly):
    while poly and poly[0] == 0:
        poly=poly[1:]
    if poly == []:
        poly.append(0)

def multiply_polynomials(poly1, poly2, mod):
        # Довжини поліномів
    
    m = len(poly1)
    n = len(poly2)
    
    # Створення списку для зберігання результатів множення
    result = [0] * (m + n - 1)
    
    # Перемноження коефіцієнтів поліномів
    for i in range(m):
        for j in range(n):
            result[i + j] = ( result[i + j] + poly1[i] * poly2[j])%mod# MODULE
    
    while result[0] == 0 and len(result)>=2:
        result=result[1:]
    
    return result

def add_polynomias(poly1,poly2):
        # Determine the lengths of the input lists
        poly1 = poly1[::-1]
        poly2 = poly2[::-1]
        normalize(poly1)
        normalize(poly2)
        
        len1 = len(poly1)
        len2 = len(poly2)
        
        # Determine the maximum length to iterate over
        max_len = max(len1, len2)
        
        # Initialize result list with zeros
        result = [0] * max_len

        # Add corresponding coefficients
        for i in range(max_len):
            if i < len1:
                result[i] =int(result[i]+poly1[i])%2
            if i < len2:
                result[i] = int(result[i]+poly2[i])%2
        
        normalize(result)
        
        result = result[::-1]
        
        return result

    
def evaluate_polynomial(coefficients, x):
    result = 0
    degree = len(coefficients) - 1  # degree of the polynomial

    for i, coef in enumerate(coefficients):
        exponent = degree - i
        result += coef * (x ** exponent)

    return result   
    
def check_zvidnist(poly,m):
    for i in range(0,m):
        res = evaluate_polynomial(poly,i) % m
        if res == 0:
            return True #Zvidnyi
    return False # Ne zvidnyi

## UNDER DEV
def is_Primitive(max_ord,poly,a,m):
    res = a
    for i in range(max_ord):
        print(f"i = {i}")
        print(res)
        if len(res)>len(a):
            mlt = [el*res[0] for el in a]
            res = add_polynomias(mlt, res[1:])
        print(res)
        res = multiply_polynomials(res,a,m)
        print(res)
        if len(res) == 1 and res[0] == 1:
            return True
    return False

m = 2
poly = [1,0,1,1]
print(f"Zvidnyst: {check_zvidnist(poly,m)}")
# x3+2x2+2x+2
max_ord = m**(len(poly)-1) - 1
print(f"Max ord: {max_ord}")

a = [ (0-x)%m for x in poly[1:]]
print(f"Alpha: {a}")

#UNDER DEV
print("Primitive") if is_Primitive(max_ord,poly,a,m) else print("Not_Primitive")

    