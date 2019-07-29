*Read in [English](README.en.md)*

# Docker Toy Application

Aplicativo feito com python para testar funcionalidades do docker, a ideia é ter diferentes containers comunicando informações. Dois containers simularão sensores que criam valores aleatórios de temperatura e umidade, ambos publicando seus valores em um contêiner de rabbitmq. Outro container será inscrito no rabbitmq e salvará as publicações. Um aplicativo de usuário pode solicitar publicações em um determinado ID, que é gerado junto com todos os valores que os sensores publicam.

## Usando

É possivel testar a aplicação rodando o comando ```bash docker-compose up ``` na pasta raiz. Ou inicializar cada container individualmente em sua pasta especifica. Depois de iniciar os contêineres, a pasta raiz tem um arquivo user.py, que é o aplicativo usado para consultar os valores pelo id. 

## Contribuindo

Pull requests são bem-vindos. Para mudanças importantes, por favor, abra um issue primeiro para discutir o que você gostaria de mudar.