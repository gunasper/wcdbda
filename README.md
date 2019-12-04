wcdbda
================
**Autor:** Gustavo Nascimento (gunasper@gmail.com)

# O projeto
Este projeto tem como objetivo construir uma estrutura mínima que possibilite a produtização de modelos de Machine Learning. Existem diversas abordagens possíveis para o problema citado, a depender, geralmente, de regras de negócios. A figura abaixo sumariza 4 abordagens possíveis. Neste projeto, opta-se por disponibilizar o modelo usando a estratégia de "webservice". Neste cenário, o modelo será treinado uma única vez e será colocado em produção por meio de uma API.

![Abordagens possíveis](https://github.com/gunasper/wcdbda/blob/master/docs/deploy_ml.png)

É importante ressaltar que a estrutura proposta, bem como as técnicas usadas, tem como objetivo somente demonstrar a produtização de modelos. Ela é suficiente para a construção de um MVP, porém, ao colocar um modelo real em produção, outras considerações devem ser feitas, como, por exemplo:
* disponibilização do modelo treinado em um serviço de armazenamento apropriado (e não por meio do GitHub, como no caso mostrado);
* construção de regras de segurança, autenticação e/ou autorização para o webservice;
* sistemas de log e rastrio de problemas;
* escalabilidade da solução;
* testes automatizados;
* etc.

Para a disponibilização do modelo, as seguintes tecnologias serão usadas:
* Flask: framework de desenvolvimento web em Python;
* Gunicorn: servidor HTTP que fará a ponte entre uma requisição e a aplicação em Flask;
* Scikit-Learn: biblioteca de algoritmos de Machine Learning;
* Heroku: plataforma em nuvem onde a aplicação ficará disponível.

# Arquivos principais

#### Configuração do projeto
* requirements: arquivo contendo as dependências de desenvolvimento para o projeto que precisam estar instaladas no servidor de produção.
* requirements-dev: arquivo contendo as dependências de desenvolvimento para o projeto.

#### Configuração Heroku
* Pipfile: arquivo contendo as dependências que devem ser instaladas no servidor web a fim de permitir que o mesmo possa executar a aplicação.
* Procfile: arquivo contendo instruções sobre como o servidor deve executar a aplicação. Contém basicamente o comando que deve ser executado para inicializar o gunicorn junto a API.

#### Treino do modelo
* build_model.py: script a ser chamado quando desejar treinar o modelo. 

* test_model.py: script para testar rapidamente se o modelo consegue ser carregado. Não é e não deve ser um script de testes automatizados.

* persistence/model_persistence.py: pacote para fazer escrita ou leitura do modelo.

* app.py: api Flask.

Os arquivos acima contém comentários explicando o que fazer e aonde modificar, bem como o comportamento esperado de cada função ou trecho de código. Recomenda-se que os trechos de código sejam preenchidos na ordem em que os arquivos são mencionados.

#### makefile
O comando "make run" irá inicializar a aplicação. Uma outra forma de inicializá-la é executar, em linha de comando, `env FLASK_APP=app.py env FLASK_DEBUG=1 flask run`.

# Deploy Heroku



# Referências
* https://datascienceacademy.com.br/blog/como-publicar-um-modelo-de-machine-learning-em-producao/
* https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html



