to_invert = int(input("Ingrese la cantidad de dinero a invertir: "))
anual_int = int(input("Ingrese el interés anual: "))
total_years = int(input("Ingrese la cantidad de años: "))

years = 1
gains = 0

while years <= total_years:
    gains = gains + (to_invert * (anual_int / 100))
    to_invert += gains
    print(f"Las ganacias del año {years} son: ${gains}")
    print(f"Este año, en total tiene: ${to_invert}\n")
    years = years + 1