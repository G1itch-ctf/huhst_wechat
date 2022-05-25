import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

def create(team,savepath):
    try:
        backimg="./1.png"
        font = r"msyhl.ttc"
        textColor = {'R': 255, 'G': 255, 'B': 255}
        backImg = Image.open(backimg)
        print(1)
        if "\n" in team:
            team="请放过开发吧,我不是专业的"
        if len(team)>17 and len(team)<40:
            fontsize=40-int(len(team)*0.75)
        elif len(team)>40 and len(team)<100:
            fontsize=10
        elif len(team) <=17:
            fontsize=40
        else:
            fontsize=40
            team="名字过长就不行哦"
    
        font = ImageFont.truetype(font, fontsize)
        draw = ImageDraw.Draw(backImg)
        draw.ink = textColor.get('R', 0) + textColor.get('G', 0) * 256 + textColor.get('B', 0) * 256 * 256
        textWidth, textHeight = font.getsize(team)
        draw.text([360 - textWidth / 2, 500], team, font=font)
        backImg.save(savepath, "png")
        print(savepath)

    except Exception as e:
        print(repr(e))



if __name__ == '__main__':
    backImg = r"/root/xiaosai/1.png"
    content="我们什么都不会队."
    savepath="./images/2.png"
    create(content,savepath)
