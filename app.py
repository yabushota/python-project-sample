import numpy as np
import pandas as pd

def main():
    # NumPy: 平均値と標準偏差の計算
    data = np.array([10, 20, 30, 40, 50])
    print("NumPy array:", data)
    print("Mean:", np.mean(data))
    print("Standard Deviation:", np.std(data))

    # pandas: データフレームの作成と基本集計
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [88, 92, 85]
    })

    print("\nPandas DataFrame:")
    print(df)

    print("\nScoreの平均:", df["Score"].mean())

if __name__ == "__main__":
    main()
