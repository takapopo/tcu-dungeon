#ライブラリーのインポート
import random
import math

#--------------------------------------------------------------------
#変数の宣言
currentLv = 0 #現在のレベル
exp = 0 #蓄積経験値

#--------------------------------------------------------------------
#関数の宣言
#現在のレベルと経験値を引数にして合算
def calculateLv (currentLv,exp):
    battle = input("\nバトルに勝ちましたか？\nはい(0)、いいえ（1)\n") #勝利⇨0、敗北⇨1を代入
    expGain = random.randrange(10,16) #10~15の範囲で受け取る経験値を決定
    expToNextLv = round(((currentLv + 1) * (currentLv + 1) * 9) / 2) #次のレベルになるための必要経験値を設定
    if battle == "0": #勝利ルート
        exp = exp + expGain
        print("バトルに勝利した。")
        print(str(expGain) + "の経験値を得た。")

        if int(exp) >= int(expToNextLv):
            print("レベルが" + str(currentLv + 1) + "になった!")
            currentLv += 1
            print("---------------")
            print("現在のレベル：" + str(currentLv))
            print("現在の経験値：" + str(exp))
            print("---------------")
        else:
            print("---------------")
            print("現在のレベル：" + str(currentLv))
            print("現在の経験値：" + str(exp))
            print("---------------")
    else:#敗北ルート
        print("バトルに負けてしまった。次回のバトルに挑もう！")
    return currentLv,exp
    
#--------------------------------------------------------------------
#メイン処理
while currentLv<=100:
    x=calculateLv(currentLv,exp)
    #レベルと経験値の更新
    currentLv=x[0]
    exp=x[1]
