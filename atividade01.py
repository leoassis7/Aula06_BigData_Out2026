venda = float(input('Digite o valor do ingresso: '))
print('''
[1] - INTEIRA (sem Desconto)
[2] - Meia entrada (50% de Desconto)
[3] - PROMOÇÃO (30% de Desconto)

''')
opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
         print('--- INTEIRA ---')
         desconto = venda * 0
         valor_da_compra =  venda - desconto
         print(f'O valor do seu desconto é de R$ {desconto}')
         print(f'O valor a pagar é de R$ {valor_da_compra}')

    case 2:
          print('--- MEIA ENTRADA ---')
          desconto = venda * 0.5
          valor_da_compra = venda - desconto
          print(f'O valor do seu desconto é de R$ {desconto}')
          print(f'O valor do seu desconto é de R$ {valor_da_compra}')

    case 3:
          print('--- PROMOÇÃO ---')
          desconto = venda * 0.3
          valor_da_compra = venda - desconto
          print(f'O valor do seu desconto é de R$ {desconto}')
          print(f'O valor do seu desconto é de R$ {valor_da_compra}')

    case _:
          print('Código Incorreto!!! Favor escolher uma das opções corretas!!!')
