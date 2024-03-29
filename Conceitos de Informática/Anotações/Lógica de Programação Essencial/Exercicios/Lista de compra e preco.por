programa
{
	// Finalidade do programa: Calcular o preço final de uma lista de compras.
	
	funcao inicio()
	{
		inteiro q, v // q é quantidade de produtos e v é uma variável feita para fazer comparação nos loopns
		cadeia confirmacao
		cadeia produto[100]
		cadeia moeda
		real preco [100]
		real s // s é a soma de preços no final
		s = 0
		v = 0
		
		escreva ("Quantos produtos deseja comprar: ")
		leia (q)
		
		se (q > 100){
			escreva ("Não é possivel comprar mais de 100 produtos!") // a lista só pode ir até 100 pois o vetor é [100]
		}
		senao{
			escreva ("Quais são os produtos: \n")
			faca {
				leia (produto[v]) // no vetor será colocado os produtos 
				v = v + 1
			
			} enquanto (v < q)
		
			v = 0
			escreva ("Sua lista é:")
			
			faca {
				escreva (produto[v] + ", ") // todos os produtos serão escritos na tela
				v = v + 1
			
			} enquanto (v < q)
			
			escreva ("Confirma? sim ou nao \n")
			leia (confirmacao) // confirmação se a lista está completa
			
			se (confirmacao == "sim") { // se a lista tiver completa

				escreva ("Qual são os preços dos produtos? (use .) \n")
				v = 0
				
				faca {
					leia (preco [v]) // no vetor será colocado os preços dos propdutos
					s = s + preco [v] // Soma dos preços de todos os produtos
					v = v + 1
			
				} enquanto (v < q)

				escreva ("Qual é sua moeda? ") // definição da moeda em que os preços estão
				leia (moeda) 
				escreva ("O total é: " + s + " " + moeda) // total dos preços na tela e fim do programa
				
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 254; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */