try:
    import pandas as pd
except ImportError:
    print("❌ pandas がインストールされていません。下部のターミナルにて、以下のコマンドを実行してください：")
    print("    pip install pandas")
    exit(1)

csv_path = 'csv_files/J. League Data Site.csv'

# csvファイルを読み込む
data = pd.read_csv(csv_path)

# 出力
print(data. head())