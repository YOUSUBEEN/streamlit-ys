# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터 확인')
    st.write(iris)

    # 메뉴 지정
    submenu = st.sidebar.selectbox('하위메뉴', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)
        with st.expander('데이터 타입'):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander("기술 통계량"):
            result2 = iris.describe()
            st.write(result2)
        with st.expander("타깃 빈도 수 확인"):
            st.write(iris['species'].value_counts())
    elif submenu == '그래프분석':
        st.title("그래프분석")
        with st.expander("산점도"):
            fig1 = px.scatter(iris,
                              x='sepal_width',
                              y='sepal_length',
                              color='species',
                              hover_data=['petal_length'])
            st.plotly_chart(fig1)

     # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title("Seaborn")
            fig, ax = plt.subplots()
            sns.boxplot(iris, x = 'species', y = 'sepal_length', ax=ax)
            st.pyplot(fig)
        with col2:
            st.title("Matplotlib")
            fig, ax = plt.subplots()
            ax.hist(iris['sepal_length'], color='blue')
            st.pyplot(fig)


        # Tabs

        tab1, tab2 = st.tabs['탭1' '탭2']
        with tab1:
            st.write('탭1')
        choice = st.selectbox('종 선택', iris['species'].unique())
        st.title('species choice')
        fig1, ax = plt.subplots()
        ax.scatter(x = ['sepal_length'], y = ['sepal_width'])
        st.pyplot(fig1)

        # 종 선택 할 때마다 산점도 그래프가 달라지도록 함
        # plotly 그래프 구현

        with tab2:
            st.write('탭2')

        #캐글 데이터 /공모전 데이터
        #해당 데이터 그래프 1개만 그리기

    elif submenu == '통계분석':
        pass
    else:
        st.warning("뭔가 없어요!")