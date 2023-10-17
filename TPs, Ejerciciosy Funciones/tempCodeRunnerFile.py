goal_list=[(0,4,2,1,2,3,1,2,3,0),(5,0,3,2,2,0,0,3,1,2),(0,2,0,1,3,0,1,2,4,2),(1,0,2,0,1,2,3,1,1,0),(1,1,2,1,0,2,1,3,0,3),(1,2,3,1,0,0,2,4,3,1),(4,5,0,0,2,4,0,1,2,1),(2,2,1,0,3,1,3,0,1,1),(0,2,1,0,3,4,5,1,0,2),(0,2,3,3,1,0,0,3,1,0)]


#"Goles de cada equipo:"
print("Goles de cada equipo:")
i=1
for team in goal_list:
    print(f"Equipo {i}: {team}")
    i+=1


# Cantidad de triunfos por equipo
# Total de goles realizados y recividos por equipos
print("-----------------------------")
for i in range(10):
    victory=0
    defeat=0
    tie=0
    goals_scored=0
    goals_against=0
    print(f"partidos del equipo: {i+1}")
    for j in range(10):
        #Total de goles realizados y recividos por equipos
        goals_scored+=goal_list[i][j]
        goals_against+=goal_list[j][i]
        # Cantidad de triunfos por equipo
        if(i!=j):
            if(goal_list[i][j]>goal_list[j][i]):
                victory+=1
            elif(goal_list[i][j]<goal_list[j][i]):
                defeat+=1
            else:
                tie+=1
    print(f"Victorias: {victory}\nDerrotas:{defeat}\nEmpates: {tie}")
    print(f"Total de goles marcados: {goals_scored}\nTotal de goles recibidos: {goals_against}\nPuntos: {victory*3 + tie}\n-----------------------------")