from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
with open("test.txt", encoding="utf-8") as f:
    s = f.read()

# jieba.load_userdict('custom_dict.txt')

# 中文分词
text = ' '.join(jieba.lcut(s))

# 生成对象
mask = np.array(Image.open('tree.png'))

stopwords = ["的", "是", "了", "在", "也", "和", "就", "都", "这", "与", "能", "地", "以"]
wc = WordCloud(font_path="/usr/share/fonts/sarasa-gothic/Sarasa-ExtraLightItalic.ttc",
               mask=mask,
               width=1000,
               height=1000,
               max_words=200,
               min_font_size= 1,
               background_color="white",
               stopwords=stopwords).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file("test.png")
