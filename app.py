import streamlit as st
import pandas as pd

EXCEL_FILE = "探索21社區_維修記錄表.xlsx"

st.set_page_config(page_title="探索21 維修記錄", layout="wide")
st.title("🔧 探索21社區 維修記錄系統")

# 讀取 Excel
@st.cache_data
def load_data():
    return pd.read_excel(EXCEL_FILE)

# 初始化
df = load_data()

# 顯示可編輯表格
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# 儲存按鈕
if st.button("💾 儲存修改"):
    try:
        edited_df.to_excel(EXCEL_FILE, index=False)
        st.success("已成功儲存至 Excel！")
    except Exception as e:
        st.error(f"儲存失敗：{e}")
