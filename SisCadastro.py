#mateus de mello blasczah     ru: 4178278
cadastro = {'codigo':[], 'nome':[], 'fabricante':[], 'valor':[]} #declaracao do dictionary com as keys
cont = 0 #declaracao da variavel para contar os codigos do cadastro

def cadastrarProduto():
    global cadastro, cont
    print('-----------------------------------------------\n'
          '                 CADASTRO                      \n'
          '-----------------------------------------------')
    print('CÓDIGO DO PRODUTO {}' .format(cont))
    nome = input('NOME DO PRODUTO: ')
    fabricante = input('FABRICANTE DO PRODUTO: ')
    valor = input('VALOR DO PRODUTO: ')
    cadastro['codigo'].append(cont)
    cadastro['nome'].append(nome)
    cadastro['fabricante'].append(fabricante)
    cadastro['valor'].append(valor)
    cont += 1
    print('\nCADASTRO CONCLUÍDO.\n')

def consultarProduto():                     #funcao de consulta
    global cadastro, cont
    print('-----------------------------------------------\n'
          '              CONSULTAR PROODUTO               \n'
          '-----------------------------------------------')
    print('1 - CONSULTAR TODOS OS PRODUTOS.')
    print('2 - CONSULTAR PRODUTOS POR CÓDIGO.')
    print('3 - CONSULTAR PRODUTOS POR FABRICANTE.')
    print('4 - RETORNAR AO MENU.')

    try:                                    #leitura do tipo de consulta
        q = int(input('>> '))
    except ValueError:
        print('ERRO, DIGITE NOVAMENTE.')

    if q == 1:                              #consulta todos
        for i in range(0, cont):
                try:
                    print('-----------------------------------------------')
                    print('CODIGO:', cadastro['codigo'][i])
                    print('NOME: ', cadastro['nome'][i])
                    print('FABRICANTE: ', cadastro['fabricante'][i])
                    print('VALOR: ', cadastro['valor'][i])
                except IndexError:
                    print('')
    elif q == 2:                            #consulta por codigo
        try:
            cc = int(input('CÓDIGO DO PRODUTO >> '))
        except ValueError:
            print('ERRO, DIGITE NOVAMENTE.')
        if cc >= 0 and cc <= cont:
            print('-----------------------------------------------')
            print('CODIGO:', cadastro['codigo'][cc])
            print('NOME: ', cadastro['nome'][cc])
            print('FABRICANTE: ', cadastro['fabricante'][cc])
            print('VALOR: ', cadastro['valor'][cc])
        else:
            print('-----------------------------------------------')
            print('CADASTRO NÃO EXISTE, VOLTANDO AO MENU.')
    elif q == 3:                            #consulta por fabricante
        consulta = str(input('NOME DO FABRICANTE >> '))
        for c in range(0, cont):
            if consulta in cadastro['fabricante'][c]:
                print('-----------------------------------------------')
                print('CODIGO:', cadastro['codigo'][c])
                print('NOME: ', cadastro['nome'][c])
                print('FABRICANTE: ', cadastro['fabricante'][c])
                print('VALOR: ', cadastro['valor'][c])
    elif q == 4:                            #retorno ao menu
        return
    else:                                   # erro e retorno ao menu
        print('OPÇÃO DE CONSULTA DESCONHECIDA, RETORNANDO AO MENU.')

def removerProduto():                       #funcao de remover produto
    try:
        cod = int(input('DIGITE O CÓDIGO DO PRODUTO QUE SERA REMOVIDO.\n>>'))
    except ValueError:
        print('ERRO, DIGITE NOVAMENTE.')
    if cod >= 0 and cod <= cont:            #remove o produto
        del cadastro['codigo'][cod]
        del cadastro['nome'][cod]
        del cadastro['fabricante'][cod]
        del cadastro['valor'][cod]
    else:
        print('CADASTRO NÃO EXISTE, RETORNANDO AO MENU.')

while True:                             #inicio do programa
    print('CONTROLE DE ESTOQUE | MERCEARIA MATEUS BLASCZAH')
    print('-----------------------------------------------')
    print('1 - CADASTRAR PRODUTO.')
    print('2 - CONSULTAR PRODUTO(S).')
    print('3 - REMOVER PRODUTO.')
    print('4 - SAIR.')
    try:                                #leitura do comando
        q = int(input('>> '))
    except ValueError:
        print('Erro, digite novamente.')
        continue
    if q == 4:                          #escolhas do menu
        break
    elif q == 1:
        cadastrarProduto()              #chamado da funcao de cadastro
    elif q == 2:
        consultarProduto()              #chamado da funcao de consulta
    elif q == 3:
        removerProduto()                #chamado da funcao de remoção
    else:
        print('INVÁLIDO, DIGITE NOVAMENTE.')
    print('-----------------------------------------------')