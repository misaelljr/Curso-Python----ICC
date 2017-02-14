seg = input("Por favor, entre com o número de segundos que deseja converter: ")

tempseg = int(seg)
dias = tempseg // 86400
seg_rest = tempseg % 86400
horas = seg_rest // 3600
seg_restantes = tempseg % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos", "e", seg_restantes_final, "segundos.")
