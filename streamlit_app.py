import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt
import japanize_matplotlib as plt
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
        if score >= 4.0:
            return "高い自己肯定感を持っています。素晴らしいです！"
        elif score >= 2.5:
            return "平均的な自己肯定感ですが、さらに高める余地があります。"
        else:
            return "自己肯定感を高めるための工夫が必要です。"
    
    feedback = {cat: get_feedback(score) for cat, score in category_scores.items()}
    feedback["総合スコア"] = get_feedback(overall_score)
    
    return category_scores, overall_score, feedback

def plot_results(scores):
    categories = list(scores.keys())
    values = list(scores.values())
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(categories, values, color=['#ffb6c1', '#f4a9c5', '#d998bf', '#b288c0', '#8b78c1', '#6a67c2'])
    ax.set_xlim(0, 5)
    ax.set_xlabel("スコア（1〜5）")
    ax.set_title("自己肯定感 診断結果")
    
    for i, v in enumerate(values):
        ax.text(v + 0.1, i, f"{v:.2f}", color='black', va='center')
    
    st.pyplot(fig)

questions = [
    "自分の短所も含めて、自分を受け入れられていると感じる。",
    "他人と比較せずに、自分は自分だと思える。",
    "失敗しても、自分を責めすぎない。",
    "新しいことに挑戦することに自信がある。",
    "困難な状況でも、乗り越えられると信じている。",
    "自分の努力が成果につながると考えられる。",
    "約束を守ることができる。",
    "大切な決断をするとき、自分を信じられる。",
    "人からの評価がなくても、自分の価値を感じられる。",
    "自分の存在は大切であると感じる。",
    "他人と比較して落ち込むことが少ない。",
    "他人からの評価に左右されすぎない。",
    "自分の人生は自分で決めることができると思う。",
    "周りの意見よりも、自分の気持ちを大切にできる。",
    "自分で決めたことを後悔することが少ない。",
    "自分のことを大切にしていると感じる。",
    "自分に優しく接することができる。",
    "自分の良いところを認めることができる。"
]

st.set_page_config(page_title="自己肯定感診断", page_icon="🌸", layout="centered")
st.title("🌸 自己肯定感診断 🌸")
st.write("以下の質問に1（全くそう思わない）〜5（非常にそう思う）で回答してください。")

responses = []
for i, question in enumerate(questions):
    responses.append(st.slider(question, 1, 5, 3))

if st.button("✨ 診断する ✨"):
    scores, overall, feedback = self_esteem_diagnosis(responses)
    
    st.subheader("🌟 診断結果 🌟")
    st.write(f"**総合スコア**: {overall:.2f}")
    st.write(f"**総合評価**: {feedback['総合スコア']}")
    
    plot_results(scores)
    
    for cat, score in scores.items():
        st.write(f"**{cat}**: {score:.2f} - {feedback[cat]}")
