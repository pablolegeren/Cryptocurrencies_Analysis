# Technical Analysis of Cryptocurrencies

This repository contains a project developed by Iker Yáñez and Pablo Legerén for the Python for data analysis course of the Official Master in Big Data Science of the University of Navarra.
Final Grade: 10 with High Honors

The objectives of this work were to obtain data on the price of a pair of currencies and subsequently plot their movements.

This project uses the Kraken library to obtain data on the prices of different cryptocurrencies. With this data, candlestick charts are generated and the stochastic indicators %K and %D are calculated. In addition, information is provided on when it would be optimal to sell or buy these stocks. 

Finally, a [Streamlit web application](https://mbdscrypto.streamlit.app/) is created to visualize these charts interactively.


## Project implementation

### 1. Requirements installation

Make sure you have Python and pip installed on your system. Then, install the project dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### 2. Execution

```bash
streamlit run src/main.py
```
