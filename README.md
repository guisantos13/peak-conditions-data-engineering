# e-Bird Data Engineering
## O que é o e-Bird?
eBird é um banco de dados on-line de observações de aves fornecendo aos cientistas, pesquisadores e naturalistas amadores dados em tempo real sobre a distribuição e a abundância de aves.\

O eBird é o maior projeto de ciência cidadã relacionado à biodiversidade do mundo, com mais de 100 milhões de avistamentos de pássaros contribuídos a cada ano por eBirders em todo o mundo. Uma empresa colaborativa com centenas de organizações parceiras, milhares de especialistas regionais e centenas de milhares de usuários, o eBird é gerenciado pelo Cornell Lab of Ornithology.\

Saiba mais : https://ebird.org/about

## Este projeto
Este projeto se trata de um projeto pessoal, cujo intuito é desenvolver um pipeline de dados através do consumo da API do e-Bird, este projeto não possuí nenhum fim lucrativo e os dados podem ser acessados abertamente por qualquer pessoa que tenha interesse através deste [link](https://science.ebird.org/pt-BR/use-ebird-data).\
[Documentação_da_API](https://documenter.getpostman.com/view/664302/S1ENwy59)

## Mais detalhes
### Datalake
O datalake será construído em cloud utilizando a estrutura da AWS (S3). <img align="center" height="50" width="50" src="https://user-images.githubusercontent.com/63247260/204093780-c383801a-0f86-4e9c-8504-8edfe508189e.png">


### IAC
Todos os recursos serão provisionados utilizando o Terraform para garantir mais agilidade e qualidade na implantação dos recursos.<img align="center" height="50" width="50" src="https://user-images.githubusercontent.com/63247260/204093858-e2e7d68a-0f2e-4bc9-b30d-29ce45020b0f.png">

### Infraestrutura do projeto
<p align=center>
  <img src="https://github.com/guisantos13/eBird-data-engineering/blob/e4e689852fcc56b8488ed99aeb68959171db8030/Infraestrutura-eBird.drawio.png" />
  </p>
<p align=center>




