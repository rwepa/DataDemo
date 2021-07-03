# title   : gm-音樂創作
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# GitHub  : https://github.com/rwepa

# 感謝 Alpha Lee 提供音樂簡譜:
# Youtube : https://youtu.be/Jx2YmiNm-6o
# Piano   : Moonlight Sonata Op.27 No.2 (Beethoven)

# 載入 gm

library(gm)

# sample 1 - 內建範例

# 建立 Music 對象

m <-

  # 初始化 Music 對象

  Music() +

  # 加上 4/4 拍號

  Meter(4, 4) +

  # 加上一條包含四個音的聲部

  Line(list("C5", "D5", "E5", "F5"), list(1, 1, 1, 1))

# 轉化成樂譜和音訊

show(m, c("score", "audio"))

# sample 2 -  Alpha Lee  提供

t <- tuplet("quarter", Tupler(3, unit = "eighth", take = "eighth"))

z1 <- Line(list("G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","G#3", "C#4", "E4","A3", "C#4", "E4","A3", "C#4", "E4","A3", "D4", "F#4","A3", "D4", "F#4","G#3", "B#3", "F#4", "G#3", "C#4", "E4", "G#3", "C#4", "D#4", "F#3", "B#3", "D#4","E3", "G#3", "C#4",c("C#4", "E4")),list(t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t,t, t, t, t, t, t, t, t, t,3), name = "a")

z2 <- Line(list(c("C#2", "C#3"), c("B1", "B2"),c("A1", "A2"), c("F#1", "F#2"),c("G#1", "G#2"),c("G#1", "G#2"),c("C#2", "G#2", "C#3")), list(4, 4, 2, 2, 2, 2, 4), to = "a", as = "staff", name = "b")

m1 <- Music() + Tempo(48)+ Meter(4, 4) + z1 + z2 + Key(4) 

m1 <- m1 + Clef("G", to = "a") + Clef("F", to = "b") 

show(m1, c("score", "audio"))

# end
