import streamlit as st

picture = st.camera_input("사진!")


st.caption("캡션")

name = st.text_input("이름을 입력해 주세요.")
if name != "" :
    #st.write(f"# {name}님 안녕하세요!")
    #st.write(f"## {name}님 안녕하세요!")
    st.write(f"### {name}님 안녕하세요!")
    st.write(f"*{name}님* 안녕하세요!")
    st.write(f"**{name}님** 안녕하세요!")
    #st.balloons()
    st.snow()

st.code("print('hello world!')")
st.write("1+2=3, x+3=2")
st.latex(r'''1 \times 2=3,
              x/3=2''')
st.latex(r'''ax^2+bx+c=0''', help = '이차방정식')

#st.divider()
st.write("---")  # 구분선
#############################################
# 이미지, 비디오 불러오기
st.image("https://png.pngtree.com/thumb_back/fh260/background/20230615/pngtree-an-image-of-the-white-tiger-sitting-down-image_2896109.jpg",
        width= 300, caption="백호")
st.video("https://www.youtube.com/watch?v=JUjpvu3mGGY", start_time=100)
st.divider()

st.title("Interactive Widge")

id = st.text_input("아이디를 입력해 주세요!")
pw = st.text_input("비밀번호를 입력해 주세요!", type= "password")

real_id = "python21"
real_pw = "123456"

if id == real_id and pw == real_pw :
    #st.write("로그인 성공")
    st.success("로그인 성공")
else :
    #st.write("로그인 실패! 아이디 혹은 패스워드를 다시 확인해주세요. ")
    st.warning("로그인 실패! 아이디 혹은 패스워드를 다시 확인해주세요. ")

st.write("...")