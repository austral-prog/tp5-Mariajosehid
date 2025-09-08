def number_to_month(month):
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    return meses.get(month, "error")

if __name__ == "__main__":
    try:
        n = int(input("Ingresa un número de mes (1-12): "))
    except ValueError:
        print("error")
    else:
        print(number_to_month(n))
