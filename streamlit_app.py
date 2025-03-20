import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sys

# 環境チェック
if "streamlit" not in sys.modules:
    st.error("エラー: Streamlitがインストールされていません。ローカル環境で `pip install streamlit` を実行してください。")
    sys.exit()
if "numpy" not in sys.modules:
    st.error("エラー: NumPyがインストールされていません。ローカル環境で `pip install numpy` を実行してください。")
    sys.exit()
if "matplotlib" not in sys.modules:
    st.error("エラー: Matplotlibがインストールされていません。ローカル環境で `pip install matplotlib` を実行してください。")
    sys.exit()

def self_esteem_diagnosis(responses):
    """
    自己肯定感診断スコアを算出
    responses: 各質問の回答（1〜5のリスト）
    """
    categories = {
        "自己受容": [0, 1, 2],
        "自己効力感": [3, 4, 5],
        "自己信頼": [6, 7, 8],
        "自己尊重": [9, 10, 11],
        "自己決定": [12, 13, 14],
        "自己愛": [15, 16, 17]
    }
    
    # 各カテゴリのスコア算出
    category_scores = {cat: np.mean([responses[i] for i in idx]) for cat, idx in categories.items()}
    overall_score = np.mean(responses)
    
    # 評価メッセージ
    def get_feedback(score):
