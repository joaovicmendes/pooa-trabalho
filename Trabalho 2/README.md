# Programação Orientada a Objetos Avançada (1001542) - Trabalho 2

Universidade Federal de São Carlos – UFSCar \
Departamento de Computação \
1001542 - Programação Orientada a Objetos Avançada - Trabalho 2 \
Prof. Dr. Daniel Lucrédio

### Grupo:
- João Victor Mendes Freire, 758943
- Julia Cinel Chagas, 759314

### Objetivo

O Princípio Aberto-Fechado ou OCP (*Open-Closed Principle*) é o princípio SOLID que propõe que um código deve ser aberto para extensão, ou seja, deve ser fácil adicionar novas funcionalidades, e fechado para modificação, de forma que alterações feitas em um módulo tenham pouco ou nenhum impacto nos demais.

Para este trabalho foi proposta a construção de uma ferramenta para encontrar e baixar títulos de notícias de sites de notícia, respeitando o OCP. Dessa forma, o código deve permitir a inclusão de novos sites e de novos algoritmos como formas diferentes de salvar os dados ou baixar as notícias em si.

### Desenvolvimento do trabalho

As tecnologias utilizadas foram a linguagem `python` na versão 3.8, a biblioteca `BeautifulSoup` para a manipulação do HTML e a biblioteca `request` para recuperar o código fonte do site.

O código foi dividido em três módulos. O módulo `fetch` é responsável por acessar a URL do site e retornar um objeto do tipo `BeautifulSoup` com o código da página. O módulo `processing` realiza a conversão dos elementos HTML para objetos do tipo `Article` e demais processamentos das notícias. Por fim, o módulo `export` salva ou apresenta ao usuário as informações.

### Como utilizar a aplicação

Com o `python 3.8`, `BeautifulSoup` e `request` instalados, de dentro da pasta `src/` basta executar: 
```
    python main.py <nome_do_site> [método de exportação]
```
Em que, o `nome_do_site` é um dentre {g1, uol, estadao, folha} e `método de exportação` é um dentre {stdout, csv}. Caso o método de exportação não seja informado, ele considerará `stdout` como a opção padrão.

### Como ampliar a aplicação

A primeira extensão proposta é a de adicionar novos sites de notícia. Para isso, utilizamos o *design pattern* **Strategy**. Assim, no módulo `processing` temos uma classe abstrata `Retrieve`, com um método `get(page_content)`, que retorna uma lista de objetos do tipo `Article`. 

Para cada site suportado, implementamos uma classe `RetrieveNomeSite` (ex: `RetrieveG1`, `RetrieveUol`), que realiza a extração adequada considerando as particularidades de cada site. Dessa maneira, adicionar um novo site consiste em implementar uma nova versão da classe `Retrieve` e atualizar o dicionário `supported_websites` na função `main`, com o nome do novo site como chave, e uma tupla com o par URL e a nova `Retrieve` como conteúdo apontado.
```python
    supported_websites = {
        'g1':  ('https://g1.globo.com', RetrieveG1()),
        'uol': ('https://noticias.uol.com.br/', RetrieveUol()),
        
        'novo_site': ('https://novo_site.com', RetrieveNovoSite())
    }
```
O restante do código irá utilizar os conteúdos deste dicionário para detectar os sites suportados e acessar as funções corretas.

A segunda extensão proposta é a de adicionar diferentes algoritmos, como baixar os conteúdos da notícia, mostrá-las para o usuário, entre outras. 

De forma análoga, utilizamos também o padrão de projeto **Strategy** no módulo `export`. Nele, temos a classe abstrata `SaveTo`, com as implementações concretas `SaveToCSV` e `SaveToStdOut`. Dependendo do argumento passado para o programa ele instancia a estratégia adequada na classe `Export`. Assim, tal qual adicionar um novo site, basta implementar uma classe `SaveTo` adequada e adicionar ao dicionário `supported_export_methods` para funcionar em conjunto ao sistema.
```python
    supported_export_methods = {
        'stdout': SaveToStdOut(), 
        'csv': SaveToCSV()
        
        'novo_metodo': SaveToNovoMetodo()
    }
```

