import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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
sample = pd.read_csv(csv_path)

# dfの情報の表示。
print(sample.info())

# 2017年のデータに絞る (ここでは'Year'カラムの最小値が2017と仮定)
df = sample[sample['Year'] == sample['Year'].min()]

name_teams_2017 = []
for i in df['Home']:
    if i not in name_teams_2017:
        name_teams_2017.append(i)

print("2017年のチームリスト:", sorted(name_teams_2017))



# 分析対象チームを指定
target_team = str(input())




# 対象チームが関与する試合のみ抽出
team_matches = df[(df['Home'] == target_team) | (df['Away'] == target_team)].copy()

# 試合の時系列順に並べ替え (必要であれば、試合日などのカラムでソート)
# ここでは'Sec' (節) でソートされている
team_matches = team_matches.sort_values(by='Sec').reset_index(drop=True)

# 各試合における得点、失点、および勝ち点を計算する関数
def calculate_match_points(row, team_name):
    points = 0
    if row['Home'] == team_name:
        # ホームの場合
        score_for = row['Score_Home']
        score_against = row['Score_Away']
        result = row['Result_Home']
    else:
        # アウェイの場合
        score_for = row['Score_Away']
        score_against = row['Score_Home']
        result = row['Result_Away']

    # 勝ち点を計算
    if result == 'WIN':
        points = 3
    elif result == 'DRAW': # 'DROW'ではなく'DRAW'と仮定
        points = 1
    else: # LOSE
        points = 0
    
    return pd.Series({
        '試合節': row['Sec'],
        '得点': score_for,
        '失点': score_against,
        '試合結果': result,
        '獲得勝ち点': points
    })

# 新しいDataFrameを作成し、各試合の情報を格納
# applyとlambdaを使って、各行に関数を適用
team_match_stats = team_matches.apply(lambda row: calculate_match_points(row, target_team), axis=1)

# 総得点（累積勝ち点）を計算
team_match_stats['累積勝ち点'] = team_match_stats['獲得勝ち点'].cumsum()



plt.figure(figsize=(10, 6))
plt.plot(team_match_stats['試合節'], team_match_stats['累積勝ち点'], marker='o', linestyle='-')
plt.title(f'Cumulative points won at each game of {target_team}')
plt.xlabel('phase')
plt.ylabel('cumulative score')
plt.grid(True)

num_matches = len(team_match_stats)
plt.xticks(np.arange(num_matches), np.arange(1, num_matches + 1))

plt.show()