# Script de ordenação de arquivo em ordem alfabética
# Objetivo: iterar pelo arquivo e colocar todos os registros em ordem alfabética
# Conceito utilizado: Iterable sort

# Import os for file renaming
import os
# Solicitar usuário informar o nome do arquivo fonte (src_file)
# Abrir arquivo src_file read
src_file = open(input('Select source file name'), 'r', encoding='utf-8')
# Abir arquivo de output (out_file) write
out_file = open("out_file.txt", 'w', encoding='utf-8')
# Definir variável para guardar nome de out_file
out_file_name = 'out_file.txt'
# Definir variável para guardar nome de in_file
in_file_name = 'in_file.txt'
# Definir linha corrente (cline)
cline = src_file.readline().strip()
# Definir proxima linha (nline)
nline = src_file.readline().strip()
# Crie variavel para contar as iterações e defina 0 (i)
i = 0
# Enquanto houver cline e nline:
while cline and nline:
    # Se cline <= nline
    if cline <= nline:
        # Escreva cline em out_file
        out_file.write(f'{cline}\n')
        # nline se torna cline
        cline = nline
        # Leia próxima nline
        nline = src_file.readline().strip()
    # Se cline > nline
    if cline > nline:
        # Adicione +1 a i
        i += 1
        # Escreva nline em out_file
        out_file.write(f'{nline}\n')
        # Leia próxima nline
        nline = src_file.readline().strip()
#Enquanto existir cline:
while cline != '' or cline != '\n':
    # Escreva cline em out_file
    out_file.write(f'{cline}\n')
    break
#Enquanto existir nline:
while nline != '' or nline != '\n':
    # Escreva nline em out_file
    out_file.write(f'{nline}')
    break
# Feche o arquivo output
out_file.close()
# Renomeie o arquivo output como 'in_file'
os.rename(out_file_name,in_file_name)
# Enquanto i > 0:
while i > 0:
    # Redefina i a 0
    i = 0
    # Abrir arquivo 'in_file' read
    in_file = open(in_file_name, 'r', encoding='utf-8')
    # Abrir novo arquivo de output (out_file) write
    out_file = open("out_file.txt", 'w', encoding='utf-8')
    # Definir linha corrente (cline)
    cline = in_file.readline().strip()
    # Definir proxima linha (nline)
    nline = in_file.readline().strip()
    # Enquanto houver cline e nline:
    while cline and nline:
        # Se cline <= nline
        if cline <= nline:
            # Escreva cline em out_file
            out_file.write(f'{cline}\n')
            # nline se torna cline
            cline = nline
            # Leia próxima nline
            nline = in_file.readline().strip()
        # Se cline > nline
        if cline > nline:
            # Adicione +1 a i
            i += 1
            # Escreva nline em out_file
            out_file.write(f'{nline}\n')
            # Leia próxima nline
            nline = in_file.readline().strip()
    #Enquanto existir cline:
    while cline != '' or cline != '\n':
        # Escreva cline em out_file
        out_file.write(f'{cline}\n')
        break
    #Enquanto existir nline:
    while nline != '' or nline != '\n':
        # Escreva nline em out_file
        out_file.write(f'{nline}')
        break
    # Feche o arquivo output
    out_file.close()
    # Feche o arquivo input
    in_file.close()
# Print "Arquivo ordenado com sucesso"
print('Sucesso!')

#run 1
# i = 8

#run 2
# i = 6

#run 3
# i = 6

#run 4
# i = 


