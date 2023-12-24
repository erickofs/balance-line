# Script de ordenação de arquivo em ordem alfabética
# Objetivo: iterar pelo arquivo e colocar todos os registros em ordem alfabética
# Conceito utilizado: Iterable sort

# Import os for file renaming
import os
# Solicitar usuário informar o nome do arquivo fonte (src_file)
src_file = input("Informe o nome do arquivo a ser ordenado: ")
# Abrir arquivo src_file read
in_file = open(src_file, 'r')
# Abir arquivo de output (out_file) write
out_file = open('output.txt', 'w')
# Definir variável para guardar nome de out_file
out_file_name = 'output.txt'
# Definir variável para guardar nome de in_file
in_file_name = 'input.txt'
# Definir linha corrente (cline)
cline = in_file.readline().strip()
# Definir proxima linha (nline)
nline = in_file.readline().strip()
# Crie variavel para contar as iterações e defina 1 (i)
i = 0
# Enquanto houver cline e nline:
while cline and nline:
    # Enquanto nline:
    while nline:
        # Se cline <= nline:
        if cline <= nline:
            # Escreva cline em out_file
            out_file.write(f'{cline}\n')
            # nline se torna cline
            cline = nline
            # Leia próxima nline
            nline = in_file.readline().strip()
        # Se cline > nline e nline não for vazio:
        if cline > nline and nline != '':
            # Adicione +1 a i
            i += 1
            # Escreva nline em out_file
            out_file.write(f'{nline}\n')  
            # Leia próxima nline
            nline = in_file.readline().strip()
    # Escreva cline em out_file
    out_file.write(cline)
# Feche o arquivo output
out_file.close()
# Renomeie o arquivo output como 'in_file'
os.rename(out_file_name, in_file_name)
# Enquanto i > 0:
while i > 0:
    # Redefina i a 0
    i = 0
    # Abrir arquivo 'in_file' read
    in_file = open(in_file_name, 'r')
    # Abrir novo arquivo de output (out_file) write
    out_file = open(out_file_name, 'w')
    # Definir linha corrente (cline)
    cline = in_file.readline().strip()
    # Definir proxima linha (nline)
    nline = in_file.readline().strip()
    # Enquanto houver cline e nline:
    while cline and nline:
        # Enquanto nline:
        while nline:
            # Se cline <= nline:
            if cline <= nline:
                # Escreva cline em out_file
                out_file.write(f'{cline}\n')
                # nline se torna cline
                cline = nline
                # Leia próxima nline
                nline = in_file.readline().strip()
            # Se cline > nline e nline não for vazio:
            if cline > nline and nline != '':
                # Adicione +1 a i
                i += 1
                # Escreva nline em out_file
                out_file.write(f'{nline}\n')  
                # Leia próxima nline
                nline = in_file.readline().strip()
        # Escreva cline em out_file
        out_file.write(cline)
    # Feche o arquivo output
    out_file.close()
    # Feche o arquivo input
    in_file.close()
# Print "Arquivo ordenado com sucesso"
print("Arquivo ordenado com sucesso!")