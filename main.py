import pandas as pd

# 读取 txt 文件（本质是 CSV）
df = pd.read_csv("crash_w_broad_st.txt")

print("字段名：")
print(df.columns)

print("\n前 5 行：")
print(df.head())

print("\n事故总数：", len(df))
