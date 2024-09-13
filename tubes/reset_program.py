import pandas as pd
input_data = {}
input_data["Apps"] = []
input_data["Seeds"] = []
initial_pw = {}
initial_pw["Init_pw"] = ["12345"]
df = pd.DataFrame(data=input_data)
pw_df = pd.DataFrame(data=initial_pw)
pw_df.astype(object)
df.astype(object)
print(df)
df.to_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/seeds.csv",index=False)
pw_df.to_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/init_pw.csv",index=False)