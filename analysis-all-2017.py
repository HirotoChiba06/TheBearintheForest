import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import japanize_matplotlib # 日本語表示が必要な場合はコメントを外してください

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

# 2017年の全チーム名を取得
all_teams_2017 = sorted(list(df['Home'].unique()))
print("2017年の全チームリスト:", all_teams_2017)


# 各試合における得点、失点、および勝ち点を計算する関数
def calculate_match_points(row, team_name):
    points = 0
    if row['Home'] == team_name:
        score_for = row['Score_Home']
        score_against = row['Score_Away']
        result = row['Result_Home']
    else:
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
        '試合節': row['Sec'], # 元の節データも保持
        '得点': score_for,
        '失点': score_against,
        '試合結果': result,
        '獲得勝ち点': points
    })

# グラフの準備
plt.figure(figsize=(15, 8)) # グラフサイズを少し大きくして見やすくする

# 全チームに対してループを回し、累積勝ち点を計算してプロット
for team in all_teams_2017:
    # 対象チームが関与する試合のみ抽出
    team_matches = df[(df['Home'] == team) | (df['Away'] == team)].copy()
    
    # 試合の時系列順に並べ替え
    # ここでは'Sec'（試合節）でソートし、その後にインデックスをリセットすることで、
    # 累積計算が正しい試合順で行われるようにします。
    team_matches = team_matches.sort_values(by='Sec').reset_index(drop=True)

    # 新しいDataFrameを作成し、各試合の情報を格納
    team_match_stats = team_matches.apply(lambda row: calculate_match_points(row, team), axis=1)

    # 総得点（累積勝ち点）を計算
    team_match_stats['累積勝ち点'] = team_match_stats['獲得勝ち点'].cumsum()

    # グラフに行を追加
    # ★変更点：X軸を '試合節' から DataFrameのインデックス (行番号) に変更
    plt.plot(team_match_stats.index, team_match_stats['累積勝ち点'], marker='o', linestyle='-', label=team, alpha=0.7)


# グラフのタイトルとラベルを設定
plt.title('2017 J1 League Standings') # タイトルを日本語に修正
plt.xlabel('phase') # X軸のラベルを「試合数」に修正
plt.ylabel('cumulative score') # Y軸のラベルを「累積勝ち点」に修正

plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # 凡例をグラフの外に配置

# X軸の目盛りを設定

max_matches = 0
for team in all_teams_2017:
    team_matches_count = len(df[(df['Home'] == team) | (df['Away'] == team)])
    if team_matches_count > max_matches:
        max_matches = team_matches_count


plt.xticks(np.arange(max_matches), np.arange(1, max_matches + 1))


plt.tight_layout() # レイアウトを調整して凡例が隠れないようにする
plt.show()