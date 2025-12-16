class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        super().__init__(f"Operador invalido: '{operador}'. Use uno de: + - * /")

def calcular_operacion(expr):
    try:
        num1_str, operador, num2_str = expr.strip().split()
    except ValueError:
        raise ValueError("Formato invalido. Use: '<numero1> <operador> <numero2>'")

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise ValueError("Los valores deben ser numeros (float convertibles).")

    if operador not in {"+", "-", "*", "/"}:
        raise OperadorInvalidoError(operador)

    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    else:
        if num2 == 0:
            raise ZeroDivisionError("Division entre cero: no es posible dividir por 0.")
        return num1 / num2

if __name__ == "__main__":
    expr = input("Ingrese operacion: ")
    try:
        resultado = calcular_operacion(expr)
        print("Resultado:", round(resultado, 2))
    except OperadorInvalidoError as e:
        print("Error:", e)
    except ZeroDivisionError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


