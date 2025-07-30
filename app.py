import streamlit as st
import pandas as pd
import os
import glob
from scripts import x01__merge

# --- データディレクトリ ---
DATA_DIR = "data"

# --- UI ---
st.title("CTDデータ ダウンロード")
st.subheader("結合するCSVファイルを選択してください")

# CSVファイル一覧を取得
@st.cache_data
def f01__csv_files():
    csv_files = glob.glob(
        "data/02__Rawdata_cp/*/*/*.Csv")
    return csv_files

csv_files = f01__csv_files()

if not csv_files:
    st.warning("dataフォルダにCSVファイルが見つかりません")
    st.stop()

from collections import defaultdict

# --- ダミーの grid データ（実際は csv_files から作成） ---
grid = defaultdict(dict)
csv_files = [...]  # あなたの csv ファイルのリスト
for path in csv_files:
    label = x01__merge.f02__Path2Label(path)
    ym, sl = "-".join(label.split("-")[:2]), "-".join(label.split("-")[2:])
    grid[sl][ym] = path

all_ym = sorted({ym for sub in grid.values() for ym in sub.keys()})
all_years = [ym.split("-")[0] for ym in all_ym]
all_months = [ym.split("-")[1] for ym in all_ym]
all_sl = sorted(grid.keys())

# --- 全選択・全解除状態保持（Session全体ではなく、一時フラグ） ---
if "select_mode" not in st.session_state:
    st.session_state.select_mode = None  # "select_all" or "dese
