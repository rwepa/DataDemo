# title   : ggplot2-新增數學式-以迴歸分析模型為例
# author  : Ming-Chang Lee
# email   : alan9956@gmail.com
# RWEPA   : http://rwepa.blogspot.tw/
# GitHub  : https://github.com/rwepa
# resource: https://rwepa.blogspot.com/2020/09/ggplot2-equation.html

library(ggplot2)

library(dplyr)

head(iris)

# 計算群組lm
fitted_models <- iris %>%
  group_by(Species) %>% 
  do(model = summary(lm(Petal.Length ~ Petal.Width, data = .)))

# levels:取出Species欄位的所有可能等級
names(fitted_models$model) <- levels(iris$Species)

# 檢視成果
fitted_models

# 查看群組lm結果(全部)
fitted_models$model

# 查看群組lm結果(setosa)
fitted_models$model$setosa

# 方法1:使用文字型態建立註釋(annotation)
mylabel <- c()

for (i in 1:length(fitted_models$model)) {
  mylabel <- c(mylabel, paste0(names(fitted_models$model[i]), ': Petal.Length = ',
                               round(fitted_models$model[[i]]$coefficients[1], 2), " ",
                               ifelse(fitted_models$model[[i]]$coefficients[2] >= 0, '+ ', ''),
                               round(fitted_models$model[[i]]$coefficients[2], 2), ' * Petal.Width,',
                               ' R2 = ', round(fitted_models$model[[i]]$r.squared, 2)))
}

mylabel
## [1] "setosa: Petal.Length = 1.33 + 0.55 * Petal.Width, R2 = 0.11"    
## [2] "versicolor: Petal.Length = 1.78 + 1.87 * Petal.Width, R2 = 0.62"
## [3] "virginica: Petal.Length = 4.24 + 0.65 * Petal.Width, R2 = 0.1"

gg_color_hue <- function(n) {
  hues = seq(15, 375, length = n + 1) # seq(0, 360, ...)
  hcl(h = hues, l = 65, c = 100)[1:n]
}

# 繪製群組迴歸模型
p <- ggplot(iris, aes(Petal.Width, Petal.Length, group=Species)) +
  geom_point(aes(color=Species), size=2) +
  geom_smooth(aes(color=Species), method=lm, se=FALSE) +
  annotate('text', label = mylabel, x = 0.7, y = c(2.5, 2, 1.5), size = 4, hjust = 0, color = gg_color_hue(n = 3)) +
  ggtitle("iris群組線性模型統計圖") +
  theme(plot.title = element_text(hjust = 0.5)) # 設定標題置中排列
p

# 方法2:使用expression建立註釋(annotation),加上 parse = TRUE
mylabel <- c()

for (i in 1:length(fitted_models$model)) {
  mylabel <- c(mylabel, paste0(names(fitted_models$model[i]), ': ', 'Petal.Length == ',
                               round(fitted_models$model[[i]]$coefficients[1], 2), " ",
                               ifelse(fitted_models$model[[i]]$coefficients[2] >= 0, '+ ', ''),
                               round(fitted_models$model[[i]]$coefficients[2], 2), ' * Petal.Width ', '~', 
                               'R^{2} == ', round(fitted_models$model[[i]]$r.squared, 2)))
}

mylabel
## [1] "setosa: Petal.Length == 1.33 + 0.55 * Petal.Width ~R^{2} == 0.11"    
## [2] "versicolor: Petal.Length == 1.78 + 1.87 * Petal.Width ~R^{2} == 0.62"
## [3] "virginica: Petal.Length == 4.24 + 0.65 * Petal.Width ~R^{2} == 0.1" 

p <- ggplot(iris, aes(Petal.Width, Petal.Length, group=Species)) +
  geom_point(aes(color=Species), size=2) +
  geom_smooth(aes(color=Species), method=lm, se=FALSE) +
  annotate('text', label = mylabel, x = 0.7, y = c(2.5, 2, 1.5), size = 4, hjust = 0, color = gg_color_hue(n = 3), parse = TRUE) +
  ggtitle("iris群組線性模型統計圖-使用 parse參數") +
  theme(plot.title = element_text(hjust = 0.5))
p
# end
