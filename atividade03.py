for i  in range(5):
   venda = float(input('Informe o valor da venda: '))
   if venda > 200:
      desconto =  (venda * 0.10)
      valor_a_pagar = venda - desconto
      print(f'\nO valor de seu desconto será de R$ {desconto}')
      print(f'\nO valor a pagar será de R$ {valor_a_pagar}')

   else:
      desconto = 0
      valor_a_pagar = venda - desconto
      print(f'\nO valor de seu desconto será de R$ {desconto}')
      print(f'\nO valor a pagar será de R$ {valor_a_pagar}')