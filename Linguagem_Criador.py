print("Escreva a sua Linguagem de preferência e descubra quem a criou!")
print('''***Linguagens disponiveis:***
***C, C++, C#, PHP, Perl, Ruby, Java, JavaScript, Python***
***escreva o nome da linguagem conforme o enunciado.***''')

linguagem = str(input('Qual a sua Linguagem de Preferência? '))

if linguagem == 'C':
    print('Criada por Dennis Ritchie em 1972.')

elif linguagem == 'C++':
    print('Criada por Bjarne Stroustrup em 1980.')

elif linguagem == 'C#':
    print('Criada por Anders Hejlsberg em 2001.')

elif linguagem == 'PHP':
    print('Criada por Rusmus Lerdorf em 1994.')

elif linguagem == 'Perl':
    print('Criada por Larry Wall em 1987.')

elif linguagem == 'Ruby':
    print('Criada por Yukihiro Matsumoto em 1995.')

elif linguagem == 'Java':
    print('Criada por James Gosling em 1991.')

elif linguagem == 'JavaScript':
    print('Criada por Brendan Eich em 1995.')

elif linguagem == 'Python':
    print('Criada por Guido van Rossum em 1982.')

else:
    print('Opss... Linguagem não reconhecida pela aplicação!')
    