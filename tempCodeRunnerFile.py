ano_actual, ano_cualquiera = int(input("Ingrese el año actual: ")), int(input("Ingrese un año cualquiera: "))

if ano_actual < ano_cualquiera:
    ano_diff = ano_cualquiera - ano_actual
    print(f"Faltan {ano_diff} para llegar a {ano_cualquiera}")
else:
    ano_diff = ano_actual - ano_cualquiera
    print(f"Han pasado {ano_diff} años desde {ano_cualquiera}")