import streamlit as st
import yfinance as yf
import altair as alt
import pandas as pd

def app():
    st.set_page_config(page_title="Bitcoin em Tempo Real", page_icon="🥮")

    st.title("💰 Cotação do Bitcoin (₿)")
    st.write("Veja o valor do **Bitcoin** em tempo real, histórico dos últimos 365 dias e faça conversões para o Real (BRL) e satoshis (sats).")

    # Obter dados do Bitcoin em USD (últimos 365 dias)
    btc = yf.Ticker("BTC-USD")
    hist_btc = btc.history(period="1y")  # Histórico de 1 ano
    preco_btc = hist_btc["Close"].iloc[-1]

    # Obter cotação do dólar em relação ao real
    usdbrl = yf.Ticker("USDBRL=X")
    hist_usdbrl = usdbrl.history(period="5d")
    preco_usd_brl = hist_usdbrl["Close"].iloc[-1]

    # Converter BTC para BRL
    preco_btc_brl = preco_btc * preco_usd_brl

    # Mostrar métricas principais
    st.metric("Preço do Bitcoin (₿)", f"${preco_btc:,.2f} USD")
    st.metric("Cotação do Dólar", f"R$ {preco_usd_brl:,.2f}")
    st.metric("Preço do Bitcoin em Reais", f"R$ {preco_btc_brl:,.2f}")

    st.divider()

    # Gráfico do histórico do BTC em USD
    st.subheader("📈 Histórico do Bitcoin (Últimos 365 dias)")
    df_plot = hist_btc.reset_index()[["Date", "Close"]]
    df_plot.columns = ["Data", "Preço (USD)"]

    chart = (
        alt.Chart(df_plot)
        .mark_line(color="orange")
        .encode(
            x="Data:T",
            y="Preço (USD):Q",
            tooltip=["Data:T", "Preço (USD):Q"]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    st.divider()

    # Escolha da unidade de entrada
    unidade = st.radio("Escolha a fração para conversão:", ["BTC", "Satoshis (sats)"])

    if unidade == "BTC":
        qtd_btc = st.number_input("Digite a quantidade de Bitcoin:", min_value=0.0, step=0.00000001, format="%.8f")
        qtd_sats = qtd_btc * 100_000_000
    else:
        qtd_sats = st.number_input("Digite a quantidade de satoshis:", min_value=0, step=1, format="%d")
        qtd_btc = qtd_sats / 100_000_000

    if qtd_btc > 0:
        valor_usd = qtd_btc * preco_btc
        valor_brl = qtd_btc * preco_btc_brl

        st.success(f"👴 {qtd_btc:.8f} BTC = {qtd_sats:,.0f} sats")
        
        col1, col2 = st.columns(2)
        col1.info(f"💵 USD: ${valor_usd:,.2f}")
        col2.info(f"🇧🇷 BRL: R$ {valor_brl:,.2f}")

if __name__ == "__main__":
    app()
