import pandas as pd

def excel_read(excel_pass):
    df = pd.read_csv(excel_pass, encoding="shift-jis")
    cam_list = df["会社名"].to_list()
    return cam_list

def excel_write(excel_pass, find_result_list):
    df1 = pd.read_csv(excel_pass, encoding="shift-jis")
    df2 = pd.DataFrame(find_result_list, columns=["タイトル", "概要", "リンク"])
    df_result = pd.concat([df1, df2], axis=1)
    df_result.to_csv(excel_pass, mode="w", index=False)
    

if __name__ == "__main__":
    excel_read()
    excel_write()