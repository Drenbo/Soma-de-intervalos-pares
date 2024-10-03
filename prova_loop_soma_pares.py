valor_um = int(input("Digite seu primeiro valor que começará a contagem: "))
valor_dois = int(input("Digite seu segundo valor que termnará a contagem: "))
valores_par = []

for i in range(valor_um, valor_dois + 1):
    while i < valor_dois + 1:
        if i % 2 == 0:
            valores_par.append(i)
            print(i)
            i += 1
            continue
        elif i % 2 != 0:
            print(i)
            i += 1
            continue
    else:
        break
    
if sum(valores_par) > 0:
    print(f"A soma dos valores pares na contagem é {sum(valores_par)}")
else:
    print(f"Não existem valores pares no intervalo, portanto a soma é {sum(valores_par)}")