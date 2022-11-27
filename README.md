# Peak Conditions Data Engineering
## O que é o Peak Conditions?
O 'Peak Conditions' é uma API que fornece dados com as condições meteorólogicas de mais de 10.000 montanhas.\
As condições meteorológicas podem variar significativamente desde o início da trilha até o cume.\
A API 'Peak Conditions' coleta dados climáticos relacionados aos picos das montanhas, a fim de ter uma ideia melhor de como serão as condições para caminhantes, alpinistas, montanhistas, cientistas da terra e da conservação ou qualquer outra pessoa que tenha motivos para estar em topo de uma montanha.\
Você pode obter um relatório diário ou uma previsão estendida de 6 dias para mais de 10.000 montanhas ao redor do mundo.



Saiba mais : https://peak-conditions-api.herokuapp.com/

## Este projeto
Este projeto se trata de um projeto pessoal, cujo intuito é desenvolver um pipeline de dados através do consumo da API,este projeto não possuí nenhum fim lucrativo e os dados podem ser acessados abertamente por qualquer pessoa que tenha interesse através deste [link](https://rapidapi.com/SeanRogan/api/peak-conditions).\
[Documentação_da_API](https://peak-conditions-api.herokuapp.com/documentation)

## Mais detalhes
### Datalake
O datalake será construído em cloud utilizando a estrutura da AWS (S3). <img align="center" height="50" width="50" src="https://user-images.githubusercontent.com/63247260/204093780-c383801a-0f86-4e9c-8504-8edfe508189e.png">


### IAC
Todos os recursos serão provisionados utilizando o Terraform para garantir mais agilidade e qualidade na implantação dos recursos.<img align="center" height="50" width="50" src="https://user-images.githubusercontent.com/63247260/204093858-e2e7d68a-0f2e-4bc9-b30d-29ce45020b0f.png">

### Infraestrutura do projeto
<p align=center>
  <img src="https://github.com/guisantos13/peak-conditions-data-engineering/blob/bd3f91c4a842359131c88b37925df146153a8ea2/Infraestrutura_peak_conditions.drawio.png" />
  </p>
<p align=center>




