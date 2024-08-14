# Primeiro contato com Python.
Este repositório contém uma aplicação para leitura de dados enviados via porta serial por balanças rodoviárias que utilizam o protocolo de comunicação EPM.

## Execução Config_logger

Ao executar o aplicativo `config_logger.exe` serão apresentadas as seguintes telas:

1. Caso não encontre nenhuma conexão Serial em seu dispositivo:   
![Alt text](documentation\image-1.png)

2. Caso existam portas conectadas o combo box `COM` exibirá todas disponíveis:   
![Alt text](documentation\image-7.png)

3. O campo `Velocidade` exibe as opções de velocidade de transmissão, que devem ser definidas conforme a capacidade de transmissão do seu equipamento.  
![Alt text](documentation\image-3.png)

4. O campo `Escolha o Diretório` permite selecionar o diretório onde deve ser salvo o arquivo `dados.txt`, que contém o valor do peso registrado no marcador.     
![Alt text](documentation\image-4.png)

5. Após a seleção de todos os campos, ao clicar em `Save`, a seguinte tela aparece, confirmando a configuração:   
![Alt text](documentation\image-5.png)

## Execução logger 
Permite a visualização do padrão de `string` para leitura e dos parâmetros de abertura/conexão da porta serial.

1. Considerando o diretório configurado `config_logger.exe`, o `logger` cria um arquivo `dados.txt` com os seguintes dados de exemplo:
![Alt text](documentation\image-6.png)
A linha superior mostra a string contendo os dados `peso, data, hora`, e a linha inferior exibe os parâmetros de abertura/conexão.

## Execução serial_reader
Desenvolvido exclusivamente para o meu cenário atual, onde o sistema `Oracle` executa o `serial_reader`, que gera um arquivo `dados.txt` com uma string formatada contendo apenas o valor do peso. O sistema Oracle lê o valor, possibilitando a geração de registros internos, ticket de pesagem e a liberação de cargas.

## Instalação
Considerando que você já tenha o Python instalados em seu sistema, execute os passos para a execução do app.

1. Clone o repositório para sua máquina local:
```bash
git clone https://github.com/narcelllo/Weight-Serial-2.git
```
2. Navegue até a pasta do projeto e execute:
```bash
pip install -r requirements.txt
```
Todas as dependências serão instaladas com base no arquivo `requirements.txt` existente neste repositório.

## Criar Executável

1. No arquivo `setup.py`, remova o comentário das linhas que se referem ao arquivo do qual deseja criar o executável, como no exemplo abaixo:

![Alt text](documentation\image.png)

2. Execute o comando:
```bash
python setup.py build
```
Será criado uma pasta `build`, contendo o executável do aplicativo selecionado. 

3. Copie a pasta `build` para um diretório de sua preferência e renomeie-a com o nome correspondente ao da linha descomentada. Exemplo: `config_logger`.

4. Siga os mesmos passos para os demais, sempre comentando as linhas já executadas.


