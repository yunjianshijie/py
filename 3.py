# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # 打开文本
# text = open("1.ciyun.txt", encoding="utf-8").read()
# # print(text)
# # print(type(text))   # <class 'str'>

# # 生成对象
# wc = WordCloud().generate(text)

# # 显示词云
# plt.imshow(wc, interpolation='bilinear')   # interpolation设置插值，设置颜色、排列等
# plt.axis("off")   # 关闭坐标轴
# plt.show()

# # 将词云图片保存到文件
# wc.to_file("1.wordcloud1.png")

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文本
text = open("1.ciyun.txt", encoding="utf-8").read()
# 生成对象
wc = WordCloud(font_path="SimHei.ttf", width=800, height=600, mode="RGBA", background_color=None).generate(text)
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("2.wordcloud2.png")