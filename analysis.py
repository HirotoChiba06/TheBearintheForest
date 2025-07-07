try:
    import pandas as pd
except ImportError:
    print("❌ pandas がインストールされていません。下部のターミナルにて、以下のコマンドを実行してください：")
    print("    pip install pandas")
    exit(1)

csv_path = 'csv_files/J. League Data Site.csv'

# csvファイルを読み込む
df = pd.read_csv(csv_path)



#出力
#dfの情報の表示。
print(df.info())
#このdfの年代を表示。
print(str(df["Year"].min()) + " ~ " + str(df["Year"].max()))