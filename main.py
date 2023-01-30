import streamlit as st
import pandas as pd

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)


st.title("test")
st.text('🎈남채민: Streamlit 프로토타입 만들기')
st.title("🔑Title을 입력하세요")

st.header('Header(머리글)을 입력하세요')
st.subheader('Subheader(세부 머리글)을 입력하세요')

st.markdown('안녕하세요\n\n'
			'저는 남챔돌입니다')

st.markdown("1, 하나")
st.markdown("2, 둘")
st.markdown("3, 셋")

st.caption('이것은 Caption 입니다')

st.text("텍스트 입력")

st.code("코드 블록 표시")

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

st.dataframe(df_stocks)

st.dataframe(df_index.style.highlight_max(axis=0))

symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])

