try:
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
except ImportError:
    print("❌ 各種ライブラリ がインストールされていません。ターミナルにて、以下のコマンドを実行してください：")
    print("    pip install numpy")
    print("    pip install pandas")
    print("    pip install matplotlib")
    exit(1)


csv_path = 'csv_files/J. League Data Site.csv'

# csvファイルを読み込む
df = pd.read_csv(csv_path)



#出力
#dfの情報の表示。
print(df.info())

#このdfの年代を表示。
print(str(df['Year'].min()) + " ~ " + str(df['Year'].max()))

#出場チーム名を列挙
name_teams = []
for i in df['Home']:
    if i not in name_teams:
        name_teams.append(i)

print(sorted(name_teams))

#2017年のデータを表示。
print(df[df['Year'] == df['Year'].min()])

#2017年の順位推移を線グラフで表示
#X軸は節、Y軸は総得点であること
#各チームに一つ戦グラフを配置したい。
df_2017 = df[df['Year'] == df['Year'].min()]

#新しいdfを生成、行にチームの名前、列に、節、毎節の総得点でまとめること。
#毎節の総得点は、勝利3、同点1、敗北0、試合の得失点を計算する、不数値は0とする。