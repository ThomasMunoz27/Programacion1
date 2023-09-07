to_invert = int(input("Ingrese la cantidad de dinero a invertir: "))
anual_int = int(input("Ingrese el interés anual: "))
total_years = int(input("Ingrese la cantidad de años: "))

years = 1


while years <= total_years:
    gains_t = 0
    parcial_gains = 0
    gains_t = gains_t + (to_invert * (anual_int / 100))
    parcial_gains = parcial_gains + (to_invert * (anual_int / 100))
    to_invert += parcial_gains
    print(f"Las ganacias del año {years} son: ${gains_t}")
    print(f"Este año, en total tiene: ${to_invert}\n")
    years = years + 1
