# Prova de Conceito: Pyscript + p5.js

Este é um exemplo de prova de conceito que combina o uso do Pyscript com o p5.js para criar animações interativas utilizando o pyodide.


## Instalação

1. Clone este repositório em sua máquina local:

   
2. Navegue até o diretório do projeto:


3. Execute o servidor local para visualizar a animação:

    ```bash
    python -m http.server
    ```

4. Abra o navegador e acesse `http://localhost:8000/musical_bubbles.html` para ver a animação em ação.

## Como funciona

Este projeto utiliza o Pyscript para gerar código JavaScript a partir de código Python. O p5.js é então utilizado para renderizar a animação no navegador.

O arquivo `server.py` serve somente para adicionar o Cross-Origin para permitir edição do código

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Basta seguir as diretrizes de contribuição e enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


## Referência

https://github.com/kwertyops/pyscript-p5js