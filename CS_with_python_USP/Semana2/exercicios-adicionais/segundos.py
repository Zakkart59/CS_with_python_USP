total_segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = total_segs // 86400
segs_restantes = total_segs % 86400
horas = segs_restantes // 3600
segs_restantes = segs_restantes % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias,"dia(s), ",horas, "hora(s), ", minutos, "minuto(s) e", segs_restantes_final, "segundos.")

s = int(input("Por favor, entre com o número de segundos que deseja converter: "))
d = s // 86400
s_rest = s % 86400
h = s_rest // 3600
s_rest = s_rest % 3600
m = s_rest // 60
s_rest = s_rest % 60
print(d,"dia(s),",h,"hora(s),",m,"minuto(s) e",s_rest,"segundo(s).")




