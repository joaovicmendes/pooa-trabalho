# Princípio da Responsabilidade Única

Universidade Federal de São Carlos – UFSCar \
Departamento de Computação \
1001504 - Programação Orientada a Objetos Avançada – Trabalho 1 \
Prof. Dr. Daniel Lucrédio \
Aluno: João Victor Mendes Freire \
RA: 758943 

---

A *Orientação à Objetos* é um dos mais populares paradigmas de linguagens de programação. Por isso, muitos estudos são realizados buscando encontrar métodos de tornar um código orientado à objetos simples de se entender, flexível e de fácil manutenção. Surgiram, então, diversos príncipios que guiam como um código deve ser planejado e organizado. Um dos principais é o padrão **SOLID**, composto por cinco princípios que buscam atingir as qualidades de código mencionadas. Vamos apresentar o primeiro dos cinco, o **S**ingle Responsability Principle (Princípio da Responsabilidade Única) ou SRP.

O SRP propõe que cada módulo (classe) de um programa deve ter uma, e apenas uma, razão para ser alterada. Ou seja, sugere que cada componente tenha uma função muito bem definida dentro do software, seja ela apresentar dados para um usuário, acessar um banco de dados ou realizar alguma operação matemática realciona à regra de negócio - sem haver intersecção entre funcionalidades num mesmo módulo. *Robert C. Martin*, o criador do termo SPR, afirma que a ideia do termo está amplamente relacionada com as pessoas envolvidas com essas funcionalidades. Ou seja, a regra de negócio é responsabilidade de um Diretor de Operações, por exemplo, enquanto o armazenamento dos dados em um *SGBD* ou no disco é responsabilidade do Diretor de Tecnologia. Assim, esses módulos deveriam estar separados em um código que respeita o Princípio da Responsábilidade Única.

O exemplo a seguir é um trecho de código de um trabalho da disciplina Organização e Recuperação da Informação, ministrada no segundo semestre de 2019 no DC-UFSCar. A classe em questão serve como uma abstração dos metadados de uma tabela do sistema gerenciador de banco de dados que foi desenvolvido.

```cpp
    class Metadata
    {
        public:
        Metadata(const std::string& table);

        void set_table(const std::string& table);
        void set_removed(long ini);
        void set_index(const std::string& field_name, const char index_type);
        void add_field(Field f);

        char which_index_in(const std::string& field) const;
        bool is_there_hash(const std::string& field) const;
        bool is_there_tree(const std::string& field) const;
        bool has_field(const std::string& field) const;
        int number_of_fieds() const;
        long get_removed() const;
        std::string get_table() const;
        std::string type_of_field(const std::string& field) const;
        std::vector<Field> get_fields() const;

        void save();
        void print() const;

        private:
        {...}
    };
```

Observemos as funções que os métodos da classe possuem. O construtor da classe (`Metadata()`) realiza um acesso à disco para recuperar os metadados de determinada tabela e carregar para a memória do programa. Existem, diversos métodos de manipulação das informações sobre a tabela nessa classe (setters do nome da tabela, da presença de um índice ou mesmo a adição que um campo à tabela). Existe um método `save()`, que atualiza para o disco as alterações feitas pelo programa. Por fim, existe um método `print()` que apresenta os metadados ao usuário. Ou seja, a classe cumpre pelo menos três papeis diferentes.

Poderiamos, então, realizar modificações para melhor separar os papéis exercidos por essa classe. Pode-se criar a classe `MetadataModel`, para cuidar das operações em disco, e a `MetadataViewer`, para cuidar da apresentação dos dados. Assim, `Metadata` serve apenas como abstração do arquivo internamente.

```cpp

   class MetadataModel
    {
        static Metadata Build(const std::string& table);
        static void Save(const Metadata& m);
        ...
    }

    class MetadataViewer
    {
        public:
        static void Print(const Metadata& m);
        ...
    }

    class Metadata
    {
        public:
        Metadata(std::string tabela, std::vector<Field> fields, long removed_position, long removed_index);

        void set_table(const std::string& table);
        void set_removed(long ini);
        void set_index(const std::string& field_name, const char index_type);
        void add_field(Field f);

        char which_index_in(const std::string& field) const;
        bool is_there_hash(const std::string& field) const;
        bool is_there_tree(const std::string& field) const;
        bool has_field(const std::string& field) const;
        int number_of_fieds() const;
        long get_removed() const;
        std::string get_table() const;
        std::string type_of_field(const std::string& field) const;
        std::vector<Field> get_fields() const;
    };
```

Para construir a classe `Metadata` poderiamos fazer uma chamada do tipo `Metadata m = MetadaModel::Build(nome_tabela)`. Para a visualização, poderiamos chamar `MetadataViewer::Print(m)`.

Nesse caso, em particular, a decisão de colocar todas as informações em um mesmo módulo se deu por inexperiência e desconhecimento sobre as vantagens da separação de papéis. No entando, é plausivél que isso seja resultado de design especulativo fruto de requisitos mal especificados.

Por fim, é importante dizer que esse princípio não deve ser tratado como uma regra obrigatória. A complexidade da aplicação e os custos relacionados à alteração de código já existente devem ser consideradas para tomar a decisão de dividir ou não.


## Referências
- Wikipédia. [Programming Paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- Wikipédia. [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- Martin, R. C. [Single Responsability Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) 
- Lucrédio, D. Vídeo Aula: [Qual a Melhor Linguagem Orientada à Objetos](https://www.youtube.com/watch?v=gbgV5jKZfTk&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=1)
- Lucrédio, D. Vídeo Aula: [Princípios SOLID na programação orientada a objetos - Princípio da Responsabilidade Única](https://www.youtube.com/watch?v=wwg-gWTuB1o&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=2)
- Lucrédio, D. Vídeo Aula: [Design especulativo - Princípios da programação orientada a objetos](https://www.youtube.com/watch?v=alwkvSaODHc&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=3)
