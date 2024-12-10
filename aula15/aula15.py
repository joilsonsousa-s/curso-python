t_carros = ("HRV","Golf","Argo","Focus")
l_carros = list(t_carros)
l_carros[0] = "Ford"
t_carros = tuple(l_carros)

for x in t_carros:
    print(x)