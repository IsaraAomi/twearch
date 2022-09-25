import numpy as np
import csv
import pprint
import MeCab
from PIL import Image
from wordcloud import WordCloud


def read_text_from_csv_to_list(file_path):
    """
    - Args:
        - file_path (str)
    - Returns:
        - list (list(list))
    """
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        list = [row[2] for row in reader]  # row[2] is text data
    # pprint.pprint(list)
    return list


def create_word_cloud_from_csv(file_path):
    """
    - Args:
        - file_path (str)
    - Returns:
    """
    list = read_text_from_csv_to_list(file_path)
    text = " ".join(list)
    mecab = MeCab.Tagger("mecabrc")
    nodes = mecab.parseToNode(text)
    s = []
    i = 0
    while nodes:
        if nodes.feature[:2] == '名詞':
            if (len(nodes.surface) > 1):
                s.append(nodes.surface)
        nodes = nodes.next
        i += 1
        # if i > 30:
        #     exit()
    # pprint.pprint(s)
    # exit()

    ## colormap: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
    width  = 1500
    height = 500
    mask_img = np.array(Image.open("../data/twitter_header_cat.png"))
    wc = WordCloud(
        width=width, height=height, background_color="white", colormap="viridis",
        mask=mask_img,
        font_path="../fonts/SourceHanCodeJP-Medium.otf",
        stopwords={"みたい","そう","あと","こと","もの","これ","ため","それ","ところ","よう","co","https","http","RT","C1","そこ","ここ","感じ","さん","わけ","すぎ","どこ","あれ","とき","まま","しない","うち","なん","なんだろう","マジ","めちゃくちゃ","とりあえず","きた","だめ","しよう","以下","もん","わからん","自分","今回","今日","明日","先生","ダメ","amp","the","in","gt","on","t","の","ん","マジで","A","v","x","さ","ついで","K","O","0","B","C","人","的","化","W","次","先","R","E","s","版","Y","P","J","I","v","やつ","はず","かね","以上","ホント","アレ","問題","個人","普通","流石"},
    )
    for i in range(10):
        wc.generate(" ".join(s))
        wc.to_file(f"../data/wordcloud_{width}x{height}_{i}.png")


def main():
    """
    - Args:
    - Returns:
    """
    create_word_cloud_from_csv("../data/list_20220926-003808.csv")


if __name__ == '__main__':
    main()
