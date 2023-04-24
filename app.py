# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd

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

    #


if __name__ == '__main__':
    main()

