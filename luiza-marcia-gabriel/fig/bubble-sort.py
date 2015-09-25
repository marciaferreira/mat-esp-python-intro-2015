# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# criamos a variável carta com os números de 0 a 18 fora de ordem
carta = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
# imprimos lista original com a variável carta
print("lista original:", carta)
# atribuimos a variavel n os valores da variavel carta
n = 20
troca = 0
iteracao = 0
plt.figure()
plt.plot(range(0,n), carta, 'ok')
plt.savefig("bubble-inicio.png")
plt.close()
# atribuimos ao indice i, o intervalo que varia de 0 a 18
for i in range (0, n-1):
# atribuimos ao indice j, o intervalo que varia entre i+1 a 19
    for j in range (i+1, n):
        iteracao = iteracao + 1
        plt.figure()
        plt.plot(range(0,n), carta, 'ok')
        plt.plot(i, carta[i], 'or')
        plt.plot(j, carta[j], 'ob')
        plt.savefig("bubble-it{}.png".format(iteracao))
        plt.close()
# estabelecemos uma comparação: se carta i eh menor que carta j
        if carta[i]<carta[j]:
# se a comparacao for verdadeira entao mantem
            continue
# senao
        else:
            troca = troca+1
# criamos um arquivo temporario que recebe o valor da carta i
            temp=carta[i]
# a carta i recebe o valor da carta j
            carta[i]=carta[j]
# a carta j recebe o valor do arquivo temporario
            carta[j]=temp
            plt.figure()
            plt.plot(range(0,n), carta, 'ok')
            plt.savefig("bubble-troca{}.png".format(troca))
            plt.close()
# imprime o texto lista em ordem crescente com os valores ordenados
print("lista em ordem crescente:", carta)
# imprime os cinco menores valores da lista
print("cinco menores valores:", carta[0:5])
# imprime os cinco maiores valores da lista
print("cinco maiores valores:", carta[n-1:n-6:-1])

plt.figure()
plt.plot(range(0,n), carta, 'ok')
plt.savefig("bubble-fim.png")
plt.close()

