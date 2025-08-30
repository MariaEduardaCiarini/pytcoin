# 💰 Bitcoin em Tempo Real

Este projeto é uma **aplicação web interativa** construída com **Streamlit** que permite acompanhar a cotação do **Bitcoin (BTC)** em tempo real, visualizar o histórico de preços e realizar conversões para **dólar (USD), real (BRL) e satoshis (sats)**.

---

## 🚀 Funcionalidades

- **Cotação em tempo real:**  
  - Mostra o preço atual do Bitcoin em **USD**.  
  - Mostra a cotação do dólar em relação ao **BRL**.  
  - Calcula automaticamente o preço do Bitcoin em **BRL**.

- **Gráfico histórico do Bitcoin:**  
  - Visualização interativa do preço do Bitcoin nos **últimos 365 dias**.  
  - Tooltip com data e valor ao passar o mouse sobre o gráfico.

- **Conversão fracionada:**  
  - Digite valores em **BTC** ou **satoshis (sats)**.  
  - Conversão automática entre BTC ↔ sats.  
  - Mostra o valor equivalente em **USD** e **BRL**.

- **Interface amigável:**  
  - Escolha da unidade de entrada via **radio button**.  
  - Resultados organizados em colunas para facilitar a leitura.  

---

## 📦 Bibliotecas utilizadas

- [streamlit](https://streamlit.io/) → Interface web interativa.  
- [yfinance](https://pypi.org/project/yfinance/) → Coleta de dados do Bitcoin e do dólar.  
- [altair](https://altair-viz.github.io/) → Gráficos interativos.  
- [pandas](https://pandas.pydata.org/) → Manipulação de dados de séries temporais.  

---
