import os
import re
import json
import google.generativeai as genai
import streamlit as st
import streamlit.components.v1 as components

# Configurar o título da página
st.set_page_config(page_title="💎Obisidian Canvas Generator")

def extract_json(text):
    """
    Extrai o conteúdo JSON puro, removendo eventuais delimitadores de bloco de código markdown.
    """
    pattern = r"```(?:json)?\s*([\s\S]+?)\s*```"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return text

# Ler as instruções do sistema a partir do arquivo .streamlit/system_instruction.txt
instructions_path = os.path.join(".streamlit", "system_instruction.txt")
try:
    with open(instructions_path, "r", encoding="utf-8") as file:
        system_instructions = file.read()
except Exception as e:
    st.error(f"Erro ao ler o arquivo de instruções do sistema: {e}")
    system_instructions = ""

# Configurar a API Key do Gemini e inicializar a biblioteca
os.environ["GEMINI_API_KEY"] = st.secrets["gemini_api_key"]
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Obter a lista de modelos disponíveis a partir da API do Gemini
try:
    models_generator = genai.list_models()  # Função fornecida pela API para listar modelos
    models_list = list(models_generator)  # Converter o gerador em uma lista
    available_models = [m.name for m in models_list]  # Extrair os nomes dos modelos
    
    # Definir o modelo padrão
    default_model = "models/gemini-2.0-pro-exp"
    if default_model in available_models:
        default_index = available_models.index(default_model)
    else:
        default_index = 0  # Caso o modelo padrão não esteja disponível, selecionar o primeiro da lista
except Exception as e:
    st.sidebar.error(f"Erro ao listar modelos: {e}")
    available_models = ["learnlm-1.5-pro-experimental"]
    default_index = 0

# Sidebar: Configurações do Modelo e Instruções
with st.sidebar:
    st.header("Configurações do Modelo")
    model_name = st.selectbox("Modelo", options=available_models, index=default_index)
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
    top_p = st.slider("Top p", min_value=0.0, max_value=1.0, value=0.95, step=0.05)
    top_k = st.slider("Top k", min_value=1, max_value=100, value=64, step=1)
    max_output_tokens = st.slider("Max Output Tokens", min_value=1000, max_value=8192, value=8192, step=100)
    response_mime_type = st.selectbox("Response MIME Type", options=["text/plain", "application/json"], index=0)

    st.markdown("---")
    st.header("Instruções")
    st.markdown("- **Texto de Entrada:** Insira o texto que será usado para gerar o canvas.")
    st.markdown("- **Gerar Canvas:** Clique para processar o texto e gerar o JSON.")
    st.markdown("- **Copiar JSON:** Utilize o botão para copiar o JSON para a área de transferência.")
    st.markdown("- **Baixar JSON:** Faça o download do arquivo `.canvas` com o JSON gerado.")
    st.markdown("- Copie o arquivo baixado para a pasta de notas do Obsidian para importar o canvas.")

# ================== Interface Principal ==================
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/2023_Obsidian_logo.svg" width="64" />
    </div>
    """,
    unsafe_allow_html=True,
)
st.title("Gerador de Canvas para Obsidian")

input_text = st.text_area("Insira o texto para gerar o Canvas:", height=200)

if st.button("Gerar Canvas"):
    if not input_text:
        st.error("Por favor, insira um texto.")
    else:
        # Construir a configuração de geração com base nas opções da sidebar
        generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens,
            "response_mime_type": response_mime_type,
        }
        
        # Criar o modelo utilizando os parâmetros personalizados e as instruções do sistema
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            system_instruction=system_instructions
        )
        
        with st.spinner("Gerando Canvas..."):
            try:
                chat_session = model.start_chat(history=[{"role": "user", "parts": [input_text]}])
                response = chat_session.send_message("Gerar canvas para Obsidian com base no texto fornecido.")
                
                # Extrair o JSON puro (sem delimitadores markdown)
                json_content = extract_json(response.text)
                
                st.markdown("### Resultado (JSON)")
                
                # Criar nome de arquivo baseado no texto de entrada
                safe_filename = re.sub(r"[^a-zA-Z0-9_-]", "_", input_text[:30])  # Limitar tamanho e remover caracteres inválidos
                file_name = f"{safe_filename}.canvas"
                
                # Botão para download do JSON puro
                st.download_button(
                    label="Baixar JSON",
                    data=json_content,
                    file_name=file_name,
                    mime="application/json",
                )
                
                # Exibir o JSON formatado com destaque de sintaxe
                st.code(json_content, language="json")
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
