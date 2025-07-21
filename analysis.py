try:
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
except ImportError:
    print("❌ 各種ライブラリ がインストールされていません。ターミナルにて、以下のコマンドを実行してください：")
    print("pip3 install numpy")
    print("pip3 install pandas")
    print("pip3 install matplotlib")
    exit(1)


csv_path = 'csv_files/J. League Data Site.csv'

# csvファイルを読み込む
df = pd.read_csv(csv_path)



#出力
#dfの情報の表示。
print(df.info())

#このdfの年代を表示。
print(str(df['Year'].min()) + " ~ " + str(df['Year'].max()))

#各チームに一つ戦グラフを配置したい。
df_2017 = df[df['Year'] == df['Year'].min()]

#出場チーム名を列挙
name_teams_2017 = []
for i in df_2017['Home']:
    if i not in name_teams_2017:
        name_teams_2017.append(i)

print(sorted(name_teams_2017))
print(len(name_teams_2017))

#2017年のデータを表示。
print(df[df['Year'] == df['Year'].min()])