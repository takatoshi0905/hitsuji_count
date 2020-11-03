import time
cnt_hitsuji = 0
is_awake = False
print("こんばんは")
print("眠れないのかい？")
not_sleep = input("はい：y いいえ：n で答えてね")
if not_sleep == "y":
    print("じゃぁ、一緒にヒツジを数えてみようね")
    while is_awake == False:
        for i in range(10):
            cnt_hitsuji += 1
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
                    print("おやすみなさい。素敵な悪夢を見てね ＠・ω・＠ﾉｼ")
                    is_awake = True
            else:
                print(f"ヒツジが{cnt_hitsuji}匹")
                print("（_・@）ﾒｪ…")
                time.sleep(1)
elif not_sleep == "n":
    print("それなら早く寝なさい！！")
else:
    print("は？ 何言ってるの？")
    # yかn以外で押すと怒られる！
