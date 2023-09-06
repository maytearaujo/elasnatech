nome = input("Informe seu nome: ");
anoAtual = input("Informe o ano atual: ");
anoNascimento = input("Informe o ano nascimento: ");

anoAtual = int(anoAtual);
anoNascimento = int(anoNascimento);
idade = anoAtual - anoNascimento;

print(nome +" você está com " + str(idade) + " anos de idade");

# type informa o tipo da variável