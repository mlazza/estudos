
"""
Crie um script para calcular o desconto do INSS, de acordo com o salário informado pelo usuário, conforme a tabela de desconto abaixo: 

Salário Desconto 

Até R$ 1693,72 - 8% 

De R$ 1693,73 a R$ 2822,90 - 9% 

De R$ 2822,91 a R$ 5645,80 - 11% 

Acima de R$ 5645,80 O desconto é de R$ 621,04. 

Crie o arquivo Python e poste para avaliação. Só será avaliado arquivos .py

@acadêmico: Marlon A. Lazzarotti
"""

def calcula_desc(sal):
    
    if sal <= 1693.72:
        return sal * 8 / 100
    elif sal > 1693.72 and sal <= 2822.90:
        return sal * 9 / 100
    elif sal > 2822.90 and sal <= 5645.80:
        return sal * 11 / 100
    elif sal > 5645.80:
        return 621.04
    
    
sal = float(input('Digite o seu salario: '))

desconto = calcula_desc(sal)

print('O desconto aplicado é de R$ {}'.format(desconto))
