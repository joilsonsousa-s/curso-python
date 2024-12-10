clima = "sol"
dinheiro = 400
lugar = ""

if clima == "sol" or (dinheiro > 300 and dinheiro < 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao: " + lugar)