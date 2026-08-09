import streamlit as st

st.title("データリセット")

st.write("保存されているユーザー情報をリセットします")

# 現在の情報を表示
if st.session_state.get('name'):
    st.info("現在保存されている情報:")
    st.write(f"名前: {st.session_state.get('name', '未設定')}")
    st.write(f"学年: {st.session_state.get('grade', '未設定')}")
    st.write(f"趣味: {', '.join(st.session_state.get('hobbies', []))}")
    
    if st.button("すべての情報をリセット", type="primary"):
        st.session_state.name = ""
        st.session_state.grade = ""
        st.session_state.hobbies = []
        st.success("すべての情報をリセットしました！")
        st.rerun()  
else:
    st.warning("リセットする情報がありません")   
