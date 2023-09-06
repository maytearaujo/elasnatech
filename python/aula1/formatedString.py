nome = input("Informe seu nome: ");
sobrenome = input("Informe seu sobrenome: ");
profissao = input("Informe sua profissao: ");
idade = input("Informe sua idade: ");
sonho = input("Informe um sonho:");

texto = 'O(A) ' + nome + ' ' + sobrenome + ' é um(a) excelente ' + '[' + profissao + ']';

print(texto);

textoFormatado = f'O(A) {nome} {sobrenome} é um(a) excelente [{profissao}]';

print(textoFormatado);

textoFormatado2 = f'O(A) {nome} {sobrenome} está com {idade} anos de idade e é um(a) excelente {profissao} e tem o sonho de {sonho}';
print(textoFormatado2);



