from numpy import random
import json
from PIL import Image, ImageDraw

#Read the two images
base = Image.open('base.png').convert("RGBA")
# base.show()
background_weights = (0.3, 0.3, 0.2, 0.2)
background_options = ["WHITE", "GREEN", "BLUE", "YELLOW"]

eyeColor = {
    "Maroon" : (128,0,0),
    "Teal":	(0,128,128),
    "Navy": (0,0,128)
}
eyeColor_weights = (0.2, 0.5, 0.3)

baseEyeSize = [(297, 109, 360, 165), (415, 122, 470, 173)]
eyeSize = {
    "Big" : [(baseEyeSize[0][0],baseEyeSize[0][1], baseEyeSize[0][2] + 50, baseEyeSize[0][3] + 50 ), (baseEyeSize[1][0],baseEyeSize[1][1], baseEyeSize[1][2] + 50, baseEyeSize[1][3] + 50 )],
    "Normal" : baseEyeSize,
    "Small" : [(baseEyeSize[0][0]+25,baseEyeSize[0][1]+25, baseEyeSize[0][2], baseEyeSize[0][3]), (baseEyeSize[1][0]+25,baseEyeSize[1][1]+25, baseEyeSize[1][2] , baseEyeSize[1][3]  )]
}
eyeSize_weights = (0.1, 0.8, 0.2)

mouth = {
    "straight": (315, 238, 440, 240),
    "smile" : ((335, 222),(357,242), (396,246), (423, 241), (443,224)),
    "unhappy": ((332, 248), (354,228), (388, 222), (410, 232), (427, 246))
}
mouth_weights = (0.5, 0.25, 0.25)
for i in range(1, 11):
    backgroundChoice = random.choice(background_options, 1, background_weights)[0]
    eyeColorChoice = random.choice(list(eyeColor.keys()), 1, eyeColor_weights)[0]
    eyeSizeChoice = random.choice(list(eyeSize.keys()), 1, eyeSize_weights)[0]
    mouthChoice = random.choice(list(mouth.keys()), 1, mouth_weights)[0]
    new_image = Image.new("RGBA", base.size, backgroundChoice)
    new_image.paste(base, mask=base)
    draw = ImageDraw.Draw(new_image)
    draw.ellipse(eyeSize[eyeSizeChoice][0], fill=eyeColorChoice, outline=(0, 0, 0))
    draw.ellipse(eyeSize[eyeSizeChoice][1], fill=eyeColorChoice, outline=(0, 0, 0))
    if mouthChoice == "straight":
        draw.line(mouth[mouthChoice], fill=(0, 0, 0), width=6)
    else:
        draw.polygon(mouth[mouthChoice], fill=(0, 0, 0), width=6)
    # new_image = background.resize(base.size)
    # new_image.paste(base,(0,0), base)
    new_image.save(f"./generatedImage/{i}.png","png")
new_image.show()