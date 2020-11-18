# O Princípio da Responsabilidade Única - SOLID

Universidade Federal de São Carlos – UFSCar \
Departamento de Computação \
1001504 - Programação Orientada a Objetos Avançada – Trabalho 1 \
Prof. Dr. Daniel Lucrédio \
Aluno: João Victor Mendes Freire \
RA: 758943 

---

Em computação existem diversos paradigmas de programação, os quais classificam linguagens baseado nas funcionalidades de cada uma. Um dos mais utilizados é a *Orientação à Objetos*, na qual informação (atributos) e subrotinas (métodos) são encapsulados em elementos chamados classes, das quais se instanciam objetos. A execução do programa se da pela comunicação entre objetos distintos.

Por ser um dos mais populares, muitos estudos são realizados buscando encontrar métodos de tornar um código orientado à objetos simples de se entender, flexível e  de fácil manutenção. Surgiram, então, diversos príncipios que guiam como um código deve ser planejado e organizado. Um deles é o padrão *SOLID*, composto por cinco princípios que buscam atingir as qualidades de código mencionadas. Vamos apresentar o primeiro dos cinco, o **S**ingle Responsability Principle (Princípio da Responsabilidade Única) ou SRP, abreviado.

O SRP diz que cada módulo (classe) de um programa deve ter uma, e apenas uma, razão para ser alterada. Ou seja, esse ele sugere que cada componente tenha uma função muito bem definida dentro do software, seja ela apresentar dados para um usuário, acessar um banco de dados ou realizar alguma operação matemática realciona à regra de negócio - mas sem haver intersecção entre funcionalidades num mesmo módulo.

O exemplo a seguir é um trecho de código de uma classe de um trabalho da disciplina Organização e Recuperação da Informação, ministrada no segundo semestre de 2019 no DC-UFSCar. A classe em questão representa os metadados de uma tabela do sistema gerenciador de banco de dados que foi desenvolvido. Esse exemplo não segue o SRP.

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

Primeiramente, o construtor da classe (`Metadata()`) realiza um acesso à disco para recuperar os metadados de determinada tabela e carregar para a memória do programa. Existem, também, diversos métodos de manipulação das informações sobre a tabela nessa classe. Existe um método `save()`, que atualiza para o disco as alterações feitas pelo programa. Por fim, existe um método `print()` que apresenta os metadados ao usuário. Ou seja, a classe cumpre pelo menos três papeis diferentes.

Poderiamos, então, criar a classe `MetadataModel`, para cuidar das operações em disco, e a `MetadataViewer`, para cuidar da apresentação dos dados. Assim, `Metadata` é apenas a abstração do arquivo internamente. Foram alterações pequenas, mas que deixam bem claras a separação dos papéis.

```cpp

   class MetadataModel
    {
        static Metadata build(const std::string& table);
        static void save(const Metadata& m);
        ...
    }

    class MetadataViewer
    {
        public:
        static void print(const Metadata& m);
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

A decisão especulativa de colocar todas as informações em um mesmo módulo se deu completamente por inesperiência e desconhecimento sobre os benefícios da separação de papéis, e não por requisitos mal específicados.

Por fim, é importante adicionar que esse princípio de separação de papéis não deve ser tratada como uma regra obrigatória sempre. A complexidade da aplicação e os custos relacionados à alteração de código já existente devem ser consideradas para tomar a decisão de dividir ou não.

---

## Referências
- Wikipédia - [Programming Paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- Wikipédia - [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
- Martin, R. C. - [Single Responsability Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) 
- Lucrédio, D. - Vídeo Aula: [Qual a Melhor Linguagem Orientada à Objetos](https://www.youtube.com/watch?v=gbgV5jKZfTk&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=1)
- Lucrédio, D. - Vídeo Aula: [Princípios SOLID na programação orientada a objetos - Princípio da Responsabilidade Única](https://www.youtube.com/watch?v=wwg-gWTuB1o&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=2)
- Lucrédio, D. - Vídeo Aula: [Design especulativo - Princípios da programação orientada a objetos](https://www.youtube.com/watch?v=alwkvSaODHc&list=PLaPmgS59eMSFYb42BcmYzVcClCh0t-26L&index=3)

