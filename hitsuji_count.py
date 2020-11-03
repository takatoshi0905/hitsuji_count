# ヒツジのカウントにタイムラグをつけたいのでtimeモジュールをインポート
import time

# ヒツジの数を格納する変数
cnt_hitsuji = 0

# 眠気フラグ
is_awake = False

# 実行時のOPコメント
print("こんばんは")
print("眠れないのかい？")
not_sleep = input("はい：y いいえ：n で答えてね")

# 眠れない場合はヒツジを一緒に数える
if not_sleep == "y":
    print("じゃぁ、一緒にヒツジを数えてみようね")
    while is_awake == False:
        for i in range(10):
            cnt_hitsuji += 1
            # 10匹ごとに再度カウントするかを尋ねる
            if cnt_hitsuji % 10 == 0:
                print(f"ヒツジが{cnt_hitsuji}匹")
                print("（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…　（_・@）ﾒｪ…")
                time.sleep(2)
                print("")
                print("…もう、眠れそうかい？")
                not_sleep = input("はい：y いいえ：n で答えてね")
                if not_sleep != "y":
                    print("じゃぁ、もう10匹ずつ数えてみようね")
                    print("")
                    time.sleep(1)
                else:
                    print("おやすみなさい")
                    time.sleep(1)
                    print("🐏 🐏 🐏 素敵な悪夢を見てね 🐏　🐏　🐏")
                    is_awake = True
            else:
                print(f"ヒツジが{cnt_hitsuji}匹")
                print("（_・@）ﾒｪ…")
                time.sleep(1)
# 眠れる場合は寝ることを促すメッセージを出力
elif not_sleep == "n":
    print("それなら早く寝なさい！！")
# yもしくはn以外のコマンドを入力した場合は塩対応する
else:
    print("は？ 何言ってるの？")