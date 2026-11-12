venda = float(input('Digite o valor da compra: '))
print('''
[1] - PIX (12% de Desconto)
[2] - DÉBITO (8% de Desconto)
[3] - CRÉDITO (5% de Desconto)
[4] - DINHEIRO (15% de Desconto)
''')

desconto = 0
opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('--- PIX ---')
        desconto = venda * 0.12
        valor_da_compra =  venda - desconto
        print(f'O valor do seu desconto é de R$ {desconto}')
        print(f'O valor a pagar é de R$ {valor_da_compra}')

    case 2:
        print('--- DÉBITO ---')
        desconto = venda * 0.08
        valor_da_compra =  venda - desconto
        print(f'O valor do seu desconto é de R$ {desconto}')
        print(f'O valor a pagar é de R$ {valor_da_compra}')
    case 3:
        print('--- CRÉDITO ---')
        desconto = venda * 0.05
        valor_da_compra =  venda - desconto
        print(f'O valor do seu desconto é de R$ {desconto}')
        print(f'O valor a pagar é de R$ {valor_da_compra}')
    case 4:
        print('--- DINHEIRO ---')
        desconto = venda * 0.15
        valor_da_compra =  venda - desconto
        print(f'O valor do seu desconto é de R$ {desconto}')
        print(f'O valor a pagar é de R$ {valor_da_compra}')

    case _:
        
        print('Opção inválida!!')

   

