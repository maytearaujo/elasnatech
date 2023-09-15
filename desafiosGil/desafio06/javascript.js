var n = parseInt(prompt('Digite um número'));

if(n >= 0 && n <= 100 && ( n% 2 == 0)){
    alert(n + ' Atende aos critérios: \n - Número positivo\n - Número menor que 100\n - Número Par\n\n \u2665\u2665\u2665');
}else{
    alert(n + ' Está fora dos critérios estabelecidos');
}