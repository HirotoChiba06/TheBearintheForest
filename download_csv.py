import kagglehub
import shutil
import os

# ダウンロード
src_path = kagglehub.dataset_download("yosafatvs/meiji-yasuda-jleague-1-20182019-league-log")

# 1. 現在の作業ディレクトリを基準にする（再現性のため）
base_dir = os.getcwd()
source_dir = os.path.join(base_dir, src_path)  # 例: Kaggle APIでDLした場所
target_dir = os.path.join(base_dir, "csv_files")         # まとめたい場所

# 2. 出力先ディレクトリを作成（存在してもOK）
os.makedirs(target_dir, exist_ok=True)

# 3. CSVファイルをまとめてコピー
for filename in os.listdir(source_dir):
    if filename.endswith(".csv"):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, filename)
        shutil.copy2(src_path, dst_path)

print(f"✅ {target_dir} にCSVファイルをまとめました。")