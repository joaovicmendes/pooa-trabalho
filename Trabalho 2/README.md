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
