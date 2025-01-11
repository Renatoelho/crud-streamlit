import streamlit as st
import pandas as pd


def carrega_dados(caminho_arquivo):
    try:
        return pd.read_csv(caminho_arquivo, sep=";")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Atividade", "Descrição", "Status"])

def salva_dados(caminho_arquivo, dataframe):
    dataframe.to_csv(caminho_arquivo, index=False, sep=";")

arquivo_csv = "arquivo_dados.csv"

st.markdown("# Gerenciador de Atividades")
st.markdown("**Atualize**, **adicione**, **remova**  ou **desative** suas atividades.")

dados = carrega_dados(arquivo_csv)

with st.container():
    edita_dados = st.data_editor(
        dados,
        use_container_width=True,
        num_rows="dynamic",
        key="editor_dados"
    )

with st.container():
    if st.button("Atualizar Atividades", type="primary"):
        salva_dados(arquivo_csv, edita_dados)
        st.success("Dados atualizados com sucesso!")

st.markdown("---")