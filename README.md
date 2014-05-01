Fermat
======

Trabalho de Cálculo Numérico

Integrantes:

- GLAUCO ROBERTO MUNSBERG DOS SANTOS
- GUILHERME PORTO BRITTO COUSIN
- GUSTAVO LIMA DE MAGALHAES


Orientações
1)  Data da entrega e apresentação: 07/05/2014 (quarta-feira) Entrega do trabalho escrito e apresentação do programa/pacote; 
2)  O trabalho escrito deve apresentar o problema a ser resolvido, métodos utilizados para a solução do problema, resultados numéricos (tabelas), gráficos (se for o caso), (de 7 a 10 páginas), comparação entre os métodos e a documentação do pacote  desenvolvido (tipo um manual de utilização);
3)  Na  resolução  do  problema,  identificar  o  sistema  de  ponto  flutuante,  a  precisão,  a exatidão,  identificar  o  critério  de  parada,  calcular  a  convergência  (se  for  o  caso)  e  os erros nas aproximações da solução; 
4)  Resolver conforme o caso, por todos os métodos; 
5)  Construir a tabela com todas as iterações, soluções e erros; 
6)  É livre a escolha da linguagem de programação. A apresentação (do programa/pacote e solução  do  problema)  terá  duração  de  10  minutos  (10  minutos  para  apresentação  e  5 minutos para perguntas ao grupo); 
7)  Enviar para pelo Ava a tarefa/trabalho; 

Soluções de Equações Algébricas e Transcedentes- Zeros

5)  (aluno 13, 14, 15)  A concentração de uma bactéria poluente num lago é descrita por 
C = 70e(-1,5t)+2,5e^(-0,075t)
Encontrar o tempo para que a concentração seja reduzida para nove.

Resoluções de Sistemas

5) (aluno 13,14,15)  Uma maneira de se obter a solução da equação de Laplace: 

((d^2)*u)%(d(x^2)) + ((d^2)*u)%(d(y^2)) = 0

d esta subistituindo um caracter especial na equação acima.

Em  uma  região  retangular  consiste  em  se  fazer  uma  discretização  que  transforma  a 
equação em um problema aproximado, consistindo em uma equação de diferenças cuja 
solução, em um caso particular, exige a solução do seguinte sistema linear: 

|	4	-1	0	-1	0	0	|	|x1	|		|100	|
|	-1	-4	-1	0	-1	0	|	|x2	|		|0		|
|	0	-1	4	0	0	-1	|	|x3	|	=	|0		|
|	-1	0	0	4	-1	0	|	|x4	|		|100	|
|	0	-1	0	-1	4	-1	|	|x5	|		|0		|
|	0	0	-1	0	-1	4	|	|x6	|		|0		|
