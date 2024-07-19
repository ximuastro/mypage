import streamlit as st
import random

def main():
    candidates = {1: "し", 2: "か", 3: "の", 4: "こ", 5: "た", 6: "ん"}
    word = candidates[1]
    
    results = []  # 結果を収集するリスト
    
    while True:
        results.append(word)  # 現在の単語をリストに追加
        
        if word == candidates[1]:  # し
            branch = random.choice([1, 2])
            if branch == 1:
                word = candidates[2]  # 「か」へ
            elif branch == 2:
                word = candidates[5]  # 「た」へ 

        elif word == candidates[2]:  # か
            word = candidates[3]  # 「の」へ 

        elif word == candidates[3]:  # の
            word = candidates[4]  # 「こ」へ

        elif word == candidates[4]:  # こ
            branch = random.choice([1, 2, 3, 4])
            if branch in [1, 2]:
                word = candidates[3]  # 「の」へ 
            elif branch == 3:
                word = candidates[4]  # 「こ」へ 
            elif branch == 4:
                word = candidates[1]  # 「し」へ 

        elif word == candidates[5]:  # た
            word = candidates[6]  # 「ん」へ 

        elif word == candidates[6]:  # ん
            branch = random.choice([1, 2])
            if branch == 1:
                word = candidates[5]  # 「た」へ 
            elif branch == 2:  # 終了
                break 
    
    # 結果をまとめて出力
    return ''.join(results)


# ボタン
if st.button('しかのこのこのここしたんたん！'):
    result = main()
    st.write(result)
