import re

def convNumRomano(roman):
    '''
    Función que convierte numero a romano
    '''
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ''
    roman = roman
    
    while roman > 0:
        for index, numero in enumerate(numeros):
            if roman - numero >= 0:
                roman -= numero
                result += letras[index]
                break
	return result

def maxLetras(start, end):
    '''
    Función para devolver el total para almacenar en la bd
    '''
    letras_s = ''
    cantidad = 0
    max_value = 0
    
    years = []
    years_l = []
    years_c = []
	
    while start <= end:
        years.append(start)
        letras_s = convNumRomano(start)
        years_l.append(letras_s)
        cantidad = len(letras_s)
        years_c.append(cantidad)
        start += 1
    
    max_value = max(years_c)

    return max_value

def romanoNumero(year):
    '''
    Función para determinar el antes y despues (AD,BC)
    '''
    roman = 0
    if year < 0:
        roman = 754 + year
    else:
        roman = 753 + year
	return roman

def clearNumber(value):
    '''
    Función para limpiar el año dado
    '''
    _spl = re.split('(\d+)',value)
    year = _spl[1]
    era = _spl[2]
    if era == 'AD':
        return int(year)
    else:
        return int('-{}'.format(year))
