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

# sample 1

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

# sample 2
# 載入 gm
library(gm)

t <- tuplet("quarter", Tupler(3, unit = "eighth", take = "eighth"))

z1 <- Line(rep(list("G#3", "C#4", "E4"),8), rep(list(t, t, t),8), name = "a1")

z2 <- Line(list(c("C#2", "C#3"), c("B1", "B2")), list(4, 4), to = "a1", as = "staff", name = "b1")

m1 <- Music() + Tempo(48)+ Meter(4, 4) + z1 + z2 + Key(4)

show(m1, c("score", "audio"))
# end
