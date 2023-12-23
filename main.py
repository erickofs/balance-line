# Balance line:

# 1. Ler dois arquivos (file1.txt e file2.txt) que estão em ordem alfabética linha por linha.
# 2. Gravar um terceiro arquivo (file3.txt) contendo a soma dos dois arquivos de entrada, mantendo a ordem alfabética.
# 3. Ler linha por linha, não ler nenhum dos dois arquivos todos para a memória, pois podem ser arquivos gigantescos.

# Abrir  arquivos 1 e 2 read
f1 = open('file1.txt')
f2 = open('file2.txt')
# Abrir arquivo 3 write
f3 = open('file3.txt', 'w')
# Ler a primeira linha do arquivo 1 (linha1)
linha1 = f1.readline().strip()
# Ler a primeira linha do arquivo 2 (linha2)
linha2 = f2.readline().strip()
# Enquanto nenhum dos arquivos tiver terminado, fazer:
while linha1 and linha2:
    # Se linha1 <= linha2
    if linha1 <= linha2:
        # Escreva no arquivo de saida linha1
        f3.write(f'{linha1}\n')
        # Leia próxima linha1
        linha1 = f1.readline().strip()
    # Se linha1 >= linha2
    if linha1 >= linha2:
        # Escreva no arquivo de saida linha2
        f3.write(f'{linha2}\n')
        # Leia próxima linha2
        linha2 = f2.readline().strip()
# Enquanto houver linhas no arquivo 1:
while linha1:
    # Escreva no arquivo de saida linha1
    f3.write(f'{linha1}\n')
    # Leia próxima linha1
    linha1 = f1.readline().strip()
# Enquanto houver linhas no arquivo 2:
while linha2:
    # Escreva no arquivo de saida linha2
    f3.write(f'{linha2}\n')
    # Leia próxima linha2
    linha2 = f2.readline().strip()
