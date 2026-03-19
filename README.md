# App de Mobilidade Urbana - Abstract Factory

Aluno: Vitor de Almeida Bernardo
Instituição: FATEC Diadema
Disciplina: Técnicas de Programação II
Professor: Vinicius Heltai Pacheco

## Descrição
Este projeto demonstra a implementação do padrão de projeto **Abstract Factory** em Java. O sistema permite a criação de famílias de veículos (Terrestres e Aéreos) sem que o cliente precise conhecer as classes concretas de cada veículo.

## Como Funciona
1. O sistema utiliza uma interface `TransporteFactory`.
2. As fábricas `TransporteTerrestreFactory` e `TransporteAereoFactory` implementam a lógica de criação.
3. O cliente apenas solicita o tipo de transporte, garantindo o desacoplamento e facilitando a inclusão de novos modais no futuro.
