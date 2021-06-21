# 参考サイト ↓
# https://office54.net/python/tkinter/textbox-get-insert

import tkinter as tk
from tkinter import *
import csv
import os

# ボタンを押したときの処理.
def memo_temp():
    #IDを体温計測ファイルから読取
    index=int(textID.get())#ID異常値判定
    if(index<1 or 1001<index):
        s="IDが不正です。(ID範囲：1~1000)"
        labelResult['text']=s
        return

    else:
        #体温を判定
        temp=float(texttemp.get())
        #体温異常値判定
        if(temp<35 or 40<temp):
            s="体温を再入力してください。体温範囲：35~40℃"
            labelResult['text']=s
            return
        else:
            if(37.5<temp):
                s="高熱が出ています。"
            elif(temp<35.5):
                s="体温が低いです。"
            else:
                s="きょうもがんばりましょう！"
        #体温計測ファイル読み取り
        filename="taion.csv"
        #csvファイルの有無を確認。なければ作る
        if (os.path.exists(filename)):
            with open(filename, "r") as f:
                read_csv=csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                #val=f.read()
                temp_files=[row for row in read_csv]
                #print(temp_files)
        else:
            temp_files=[]


        #ID(index)がリストより大きいか判定して小さければ行を追加する
        if(index<len(temp_files)):
            id_temp=temp_files[index-1]
        else:
            for i in range(0, index-len(temp_files)):
                temp_files.append([])
            id_temp=temp_files[index-1]
        #体温をリストに追加
        id_temp.append(float(temp))
        #平均体温の計算str形式にしないと表示できない
        average=str(sum(id_temp)/len(id_temp))
        #print(average)
        print(temp_files)
        labelResult['text']=s+"\n 平均体温: "+ average + "℃"
        #ファイルの書き込み
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(temp_files)


# ウィンドウを作成
win = tk.Tk()  # からっぽのウィンドウ。ここに情報を入れていく
win.title("体温記録表")  # ウィンドウのタイトルを指定
#win.geometry("500x250")  # サイズを指定
win.geometry("250x250")  # サイズを指定

#画像読み込み（任意）png, pgm, ppm, gif形式のみ
image = tk.PhotoImage(file="pic.png")
#test_canvas = tk.Canvas(bg="black", width=100, height=100)
#test_canvas.grid(row=0, column=0)
#im = ImageTk.PhotoImage(image=image)
#test_canvas.create_image(10, 10, anchor='nw', image=image)
img=tk.Label(image=image)
img.pack()

# 部品を作成
labelID = tk.Label(win, text='ID:')  # ウィンドウ内に配置するラベルの内容
labelID.pack()  # ウィンドウの中に上から順に配置する命令

textID = tk.Entry(win)  # テキストボックスを作る
textID.insert(tk.END, '1')  # デフォルトの文字を入れておく
textID.pack()  # 配置

labeltemp = tk.Label(win, text='体温(℃):')  # ID同様
labeltemp.pack()

texttemp = tk.Entry(win)
texttemp.insert(tk.END, '36.5')
texttemp.pack()

labelResult = tk.Label(win, text='---')  # ID同様
labelResult.pack()  # memo_temp関数でlabelResult['text'] = sと指定されているのはこの部分。 86行目で作ったtext='---'のtext部分を上書きしている

calcButton = tk.Button(win, text='記録')  # Buttonウィジェットではcommandを指定できる
calcButton["command"] = memo_temp  # 関数memo_tempを呼び出している
# 上記2行はcalcButton = tk.Button(win, text='記録',command=memo_temp)とまとめてかくこともできる
calcButton.pack()

# ウィンドウを動かす
win.mainloop()