import pandas as pd
import requests

dataframe = pd.read_excel("LLM_Experiment.xlsx", header = None)
for i in range(4, 6):
    prompt = "請依照指示分析下方的文字，先判斷這段文字中是否有提到「違反廢棄物規定」，如果沒有回答(null)，如果有違反，則回答文字中有違反的廢棄物代碼及違反的時間，廢棄物代碼是一個英文字母，一個- 跟四個數字，如R-0201、D-0299，和違反的西元時間，年度及月分，違反的項目可能不只一個，因此可能有多組代碼及時間，請依照前面的指令回答，不要回答多餘的文字。例如輸入的文字為：" + dataframe.iloc[0, 0] + "時，要回答：" + dataframe.iloc[0, 1] + "。要分析的文字：" + dataframe.iloc[i, 0]
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gpt-oss:latest",
            "messages": [
                {
                "role": "user",
                "content": prompt
                }
            ],
            "stream":False
        }
    )
    response = response.json()
    result = response["message"]["content"]
    print("text:", dataframe.iloc[i, 0])
    print("result:", result, "\n")