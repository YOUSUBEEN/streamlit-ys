# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd
from utils import p_lans
from PIL import Image

# Data VIZ
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # title
    st.title("Hello World")
    # text
    st.text("This is so {}".format("good"))

    # Header
    st.header("This is header")

    # Subheader
    st.subheader("This is subHeader")

    # Markdown
    st.markdown("## This is Markdown")

    # 색상이 들어간 text feature
    st.success('성공')
    st.warning('경고')
    st.info('정보와 관련된 탭')
    st.error("에러 메시지")
    st.exception("예외처리")

    # st.write()
    st.write('일반텍스트')
    st.write(1+2)
    st.write(dir(str))

    st.title(":sunglasses:")

    # Help
    st.help(range)
    st.help(st.title)

    # 데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title("IRIS 테이블")
    st.dataframe(iris, 500, 100) # Height, Width

    st.title("table()")
    st.table(iris)

    st.title('write()')
    st.write(iris)

    myCode = """
    def hello():
        print("hi")
    """

    st.code(myCode, language="Python")

    # 위젯, button 기능활용

    name = "usb"
    if st.button("Submit"):
        st.write(f'name: {name.upper()}')
        
    # RadiButton
    s_state = st.radio('Status', ('활성화', '비활성화'))
    if s_state == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # Check Box
    if st.checkbox("show/hide"):
        st.text("무언가를 보여줘!")

     # Select Box
    choice = st.selectbox('프로그래밍 언어', p_lans)
    st.write(f'{choice} 언어를 선택함')

    # multiple selection
    lans = ("영어", "일본어", "중국어", "독일어")
    myChoice = st.multiselect("언어 선택", lans, default="중국어")
    st.write("선택", myChoice)

    # Slider
    age = st.slider('나이', 1, 120)
    st.write(age)

    # 이미지 가져오기
    img = Image.open('data/image_03.jpg')
    st.image(img)

    url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MjJfNDgg%2FMDAxNjU1ODg0NTU4ODEy.UQdlVJLBIUV40ks6oDYRJokv_m00D6Vjq-f7NntrPHYg.DouDmK41kbb1NWwFHCTWqw7kRmxx4HLaYLzfis3lYb4g.JPEG.niceguy00%2FSeul_%25BE%25BE%25B3%25D721_%25B5%25B5%25C7%25F604.jpg'
    st.image(url)

    # 비디오 출력
    with open("data/secret_of_success.mp4", 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time =1)

    # 오디오 출력
    with open("data/song.mp3", 'rb') as rb:
        audio_file = rb.read()
        st.audio(audio_file, format = 'audio/mp3')




    # choice = st.selectbox('프로그래밍 언어', iris['species'].unique())
    # st.title(choice)
    #
    #
    # result = iris[iris['species'] == choice].reset_index(drop = True)
    # st.dataframe(result)
    #
    # col1, col2, col3 = st.columns([0.3, 0.4, 0.4], gap = 'large')
    #
    # with col1:
    #     iris = pd.read_csv("data/iris.csv")
    #     st.dataframe(iris.head())
    #
    # with col2:
    #     fig = px.scatter(data_frame = iris,
    #                      x = 'sepal_length',
    #                      y = 'sepal_width')
    #     st.plotly_chart(fig)
    #
    # with col3:
    #     fig2, ax = plt.subplots()
    #     ax.scatter(x = iris['sepal_length'], y = iris['sepal_width'])
    #     st.pyplot(fig2)

    ####################

    fig = px.scatter(data_frame=iris,
                     x='sepal_length',
                     y='sepal_width')
    st.plotly_chart(fig)

    choice = st.selectbox('프로그래밍 언어', iris['species'].unique())
    # st.title(choice)

    result = iris[iris['species'] == choice].reset_index(drop=True)
    # st.dataframe(result)

    col1, col2 = st.columns([0.5, 0.5], gap='large')
    with col1:
        fig2, ax = plt.subplots()
        # ax.scatter(x=iris['petal_length'], y=iris['sepal_width'])
        sns.scatterplot(result, x = 'petal_length', y = 'sepal_width')
        st.pyplot(fig2)

    with col2:
        fig3, ax = plt.subplots()
        ax.scatter(x = result['sepal_length'], y = result['sepal_width'])
        st.pyplot(fig3)


if __name__ == '__main__':
    main()