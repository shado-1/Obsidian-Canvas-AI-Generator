Aqui está o modelo de um arquivo `README.md` para o código fornecido:

```markdown
# Obsidian Canvas Generator

Este é um gerador de Canvas para o Obsidian, desenvolvido em Python utilizando Streamlit, para criar arquivos `.canvas` a partir de textos fornecidos pelo usuário. Ele integra a API do Gemini para gerar conteúdo estruturado em formato JSON, que pode ser utilizado diretamente no Obsidian.

## Funcionalidades

- **Gerar Canvas:** Insira um texto e clique para gerar um arquivo JSON estruturado para o Obsidian.
- **Download de JSON:** Faça o download do arquivo `.canvas` gerado.
- **Copiar JSON:** Copie o JSON diretamente para a área de transferência.
- **Configurações Personalizadas:** Ajuste a temperatura, top-p, top-k, e o número máximo de tokens de saída, permitindo o controle sobre a geração do modelo.

## Requisitos

- Python 3.7+
- Streamlit
- `google-generativeai` (Biblioteca oficial do Google Gemini)
- Uma chave de API do Gemini válida

## Instalação

### 1. Instalar dependências

Primeiro, clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Configurar a chave da API do Gemini

- A chave da API do Gemini deve ser configurada como uma variável de ambiente `GEMINI_API_KEY`. Adicione a chave no arquivo `secrets.toml`:

```toml
[gemini]
gemini_api_key = "SUA_CHAVE_AQUI"
```

Ou, altere diretamente o código para passar a chave manualmente.

### 3. Arquivo de instruções do sistema

O sistema depende de um arquivo de instruções armazenado em `.streamlit/system_instruction.txt`. Caso não tenha esse arquivo, crie-o ou adicione instruções personalizadas.

## Como Usar

### 1. Configurar o modelo

No menu lateral, selecione as opções de configuração do modelo:
- **Modelo:** Escolha um modelo da lista disponível.
- **Temperature:** Controla a aleatoriedade da geração.
- **Top p:** Controla a seleção de palavras com base na probabilidade cumulativa.
- **Top k:** Controla o número de palavras candidatas a serem consideradas.
- **Max Output Tokens:** Número máximo de tokens para a resposta.
- **Response MIME Type:** Tipo de resposta esperada (JSON ou texto simples).

### 2. Inserir o texto

Digite ou cole o texto no campo "Insira o texto para gerar o Canvas:".

### 3. Gerar o Canvas

Clique no botão **Gerar Canvas** para processar o texto e gerar o conteúdo em formato JSON. O resultado será exibido abaixo com a opção de:
- **Baixar JSON:** Clique para fazer o download do arquivo `.canvas` gerado.
- **Copiar JSON:** Clique para copiar o conteúdo JSON para a área de transferência.

### 4. Importar no Obsidian

Após baixar o arquivo `.canvas`, mova-o para a pasta de notas do Obsidian para importar o canvas gerado.

## Exemplo de Uso

1. Insira o texto a ser usado para gerar o Canvas.
2. Clique em **Gerar Canvas**.
3. Baixe o arquivo `.canvas` gerado ou copie o JSON para uso futuro.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch (`git checkout -b minha-nova-feature`).
3. Faça suas alterações.
4. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
5. Envie para o seu fork (`git push origin minha-nova-feature`).
6. Abra um pull request.

## Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- **Streamlit:** Para a criação da interface de usuário.
- **Google Gemini API:** Para a geração de conteúdo com IA.

---

Se você tiver problemas ou sugestões, abra uma issue ou envie um pull request!
```

Este `README.md` fornece um guia completo sobre como configurar e usar o gerador de canvas para o Obsidian.