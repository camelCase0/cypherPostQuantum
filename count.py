def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)

def multiply_polynomials(poly1, poly2):
        # Довжини поліномів
        m = len(poly1)
        n = len(poly2)
        
        # Створення списку для зберігання результатів множення
        result = [0] * (m + n - 1)
        
        # Перемноження коефіцієнтів поліномів
        for i in range(m):
            for j in range(n):
                result[i + j] = ( result[i + j] + poly1[i] * poly2[j])%2# MODULE
        
        while result[0] == 0 and len(result)>=2:
            result=result[1:]
        
        return result

def divide_polynomials(num, den):
        #Create normalized copies of the args
        num = num[::-1]
        den = den[::-1]
        normalize(num)
        normalize(den)

        if len(num) >= len(den):
            #Shift den towards right so it's the same degree as num
            shiftlen = len(num) - len(den)
            den = [0] * shiftlen + den
        else:
            return [0], num

        quot = []
        divisor = float(den[-1])
        for i in range(shiftlen + 1):
            #Get the next coefficient of the quotient.
            mult = int(num[-1] / divisor)%2
            quot = [mult] + quot

            #Subtract mult * den from num, but don't bother if mult == 0
            #Note that when i==0, mult!=0; so quot is automatically normalized.
            if mult != 0:
                d = [mult * u for u in den]
                num = [(u - v)%2 for u, v in zip(num, d)]

            num.pop()
            den.pop(0)
            
        normalize(num)
        normalize(quot)
        
        quot = quot[::-1]
        num = num[::-1]
        
        return quot, num

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

class CryptCalc:
    def __init__(self,fx) -> None:
        self.fx = fx

    def mult_with_mod(self,poly1, poly2):
        result = multiply_polynomials(poly1, poly2)
        print(f"{poly1} * {poly2} = {result}")
        if len(result)>=len(self.fx):
            res, remainder = divide_polynomials(result, self.fx)
            print(f"{result} % {self.fx} = {remainder}")
            result = remainder
        return result

    def add_with_mod(self,poly1,poly2):
        result = add_polynomias(poly1, poly2)
        print(f"{poly1} + {poly2} = {result}")
        if len(result)>=len(self.fx):
            rest, remainder = divide_polynomials(result, self.fx)
            print(f"{result} % {self.fx} = {remainder}")
            result = remainder
        return result

    def multiply_row_on_column(self,row,column):
        print(f"{'='*20} \n {row} * {column}")
        res = []
        for i in range(len(row)):
            print(f"#{i}")
            mlt = self.mult_with_mod(column[i],row[i])
            res = self.add_with_mod(res,mlt)
        print("RESULT:", res)
        return res

    def multiply_matrices(self, matrix1, matrix2):
        # Check dimensions
        rows1 = len(matrix1)
        cols1  =len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        
        print(f"Result size:{rows1},{cols2}")

        result = [[0] * cols2 for _ in range(rows1)]
        print(f"Initial result: {result}")
        
        for x in range(rows1):
            for y in range(cols2):
                print(f"X:{x},Y:{y}")
                row = matrix1[x]
                col = [row[y] for row in matrix2]
                # Str[] into int[]
                row = [[int(char) for char in s] for s in row]
                col = [[int(char) for char in s] for s in col]

                result[x][y] = self.multiply_row_on_column(row,col)
                
        # To str
        result = [["".join(map(str,str_arr)) for str_arr in row] for row in result]
        return result

