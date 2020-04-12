# Descrição 
1. Ler uma imagem em escala de cinzas
2. Ampliar a imagem para que ela tenha dois pixels a mais na direção horizontal  e dois pixels a mais na direção vertical. Esses pixels adicionais terão valor de intensidade iguais a zero.
3. Usar uma máscara de derivada (abordagem central) e aplicá-la a cada pixel da imagem ampliada que não seja um pixel de borda. O resultado da aplicação da máscara sobre um pixel é copiado no pixel correspondente de uma imagem nova.
4. Exibir a imagem original e a imagem nova.

# Caso use linux:
	> Abra um terminal na pasta do arquivo do código
	> Digite no terminal: python3 Tarefa_1-MN2-Márcio_e_Claudemir.py nome_da_imagem.extensão
	>	Por exemplo: python3 Tarefa_1-MN2-Márcio_e_Claudemir.py imagem.jpeg
	> A imagem original e a das bordas serão exibidas

# Caso use windows:
	> Execute o código fonte em alguma IDE que ele pedirá o nome da imagem
	> A imagem original e a das bordas serão exibidas

### OBS1: A IMAGEM DEVE ESTAR NA MESMA PASTA QUE O CÓDIGO-FONTE 
### OBS2: NA PASTA DO CÓDIGO FONTE SERÁ SALVA A IMAGEM DAS BORDAS
