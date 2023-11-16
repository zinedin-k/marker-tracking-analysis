from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os


#############################################################################################################
###################################     AUGMENTATION SCRIPT     #############################################
#############################################################################################################


os.makedirs("expanded_uppercase_dataset", exist_ok=True)

for i in range(65, 91):
    for j in range(500):
        background = Image.new("RGBA", (32, 32), color=(255, 255, 255, 0))
        
        draw = ImageDraw.Draw(background)

        symbol = chr(i)

        font = ImageFont.truetype("arial.ttf", 20)

        draw.text((12, 12), symbol, fill=(0, 0, 0, 255), font=font)

        rotated_symbol = background.rotate(random.randint(0, 360), resample=Image.BICUBIC)
        rotated_symbol = rotated_symbol.filter(ImageFilter.GaussianBlur(radius=random.uniform(0, 1)))

        white_background = Image.new("RGB", rotated_symbol.size, (255, 255, 255))
        white_background.paste(rotated_symbol, mask=rotated_symbol.split()[3])  # Use alpha channel as mask
        
        white_background.save(f"expanded_uppercase_dataset/symbol_{i}-{j}.png")


#############################################################################################################
#################################       ASCII SYMBOLS WITHOUT NUMBERS    ####################################
#############################################################################################################



os.makedirs("symbols_without_numbers_dataset", exist_ok=True)

for i in range(33, 127):
    if 65 <= i <= 90 or 97 <= i <= 122 or 48 <= i <= 57:
        continue
    img = Image.new("RGB", (32, 32), color="white") #   blank image
    draw = ImageDraw.Draw(img)

    symbol = chr(i)

    font = ImageFont.truetype("arial.ttf", 20)

    text_width, text_height = draw.textsize(symbol, font=font)
    position = ((32 - text_width) // 2, (32 - text_height) // 2)

    draw.text(position, symbol, fill="black", font=font)

    img.save(f"symbols_without_numbers_dataset/symbol_{i}.png")


#############################################################################################################
######################################    ASCII SYMBOLS WITH NUMBERS      ###################################
#############################################################################################################



os.makedirs("symbols_with_numbers_dataset", exist_ok=True)

for i in range(33, 127):
    if 65 <= i <= 90 or 97 <= i <= 122:
        continue
    img = Image.new("RGB", (32, 32), color="white")
    draw = ImageDraw.Draw(img)

    symbol = chr(i)

    font = ImageFont.truetype("arial.ttf", 20)

    text_width, text_height = draw.textsize(symbol, font=font)
    position = ((32 - text_width) // 2, (32 - text_height) // 2)

    draw.text(position, symbol, fill="black", font=font)

    img.save(f"symbols_with_numbers_dataset/symbol_{i}.png")


#############################################################################################################
#####################################   LOWERCASE LETTERS a-z   #############################################
#############################################################################################################


os.makedirs("lower_case_dataset", exist_ok=True)

for i in range(97, 123):
    img = Image.new("RGB", (32, 32), color="white")
    draw = ImageDraw.Draw(img)

    symbol = chr(i)

    font = ImageFont.truetype("arial.ttf", 20)

    text_width, text_height = draw.textsize(symbol, font=font)
    position = ((32 - text_width) // 2, (32 - text_height) // 2)

    draw.text(position, symbol, fill="black", font=font)

    img.save(f"lower_case_dataset/symbol_{i}.png")



#############################################################################################################
################################    UPPERCASE LETTERS A-Z   #################################################
#############################################################################################################


    
os.makedirs("upper_case_dataset", exist_ok=True)

for i in range(65, 91):
    img = Image.new("RGB", (32, 32), color="white")
    draw = ImageDraw.Draw(img)

    symbol = chr(i)

    font = ImageFont.truetype("arial.ttf", 20)

    text_width, text_height = draw.textsize(symbol, font=font)
    position = ((32 - text_width) // 2, (32 - text_height) // 2)

    draw.text(position, symbol, fill="black", font=font)

    img.save(f"upper_case_dataset/symbol_{i}.png")
