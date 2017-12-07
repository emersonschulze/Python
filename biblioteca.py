def gera_nome(nome_completo):
	tamanho = len(nome_completo)
	posicao = tamanho - 7
	nome = nome_completo[0:7]
	sobrenome = nome_completo[posicao: tamanho]
	return nome + ' ' + sobrenome