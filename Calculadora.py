choice = 0;
contador = 1;
valor = 0;
despesa = 0;
salario = 0;
porcentagem = 0;
print("Bem vindo(a)! Este é um software que calcula a porcentagem do seu salário que está sendo utilizada em suas despesas")
choice = int(input("Você deseja calcular as despesas ou já tem o valor?: \n1-Desejo calcular\n2-Já sei o valor"))

if choice == 1:
    print("Digite os valores das Despesas e quando desejar parar, digite 0.")
    while choice == 1:
        print(contador,"°")
        valor = float(input("Despesa :"));
        despesa = despesa + valor;
        if valor == 0:
            choice = 0;
        else:
            contador = contador + 1
    salario = float(input("Digite aqui a sua renda líquida: "))
    porcentagem = ((100 * despesa)/salario)
    print("Suas despesas representam",porcentagem,"%","de seu salário!")

if choice == 2:
    despesa = float(input("Qual o valor total da despesa?: "))
    salario = float(input("Digite aqui a sua renda líquida: "))
    porcentagem = ((100 * despesa)/salario)
    print("Suas despesas representam",porcentagem,"%","de seu salário!")
