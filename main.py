from PIL import Image, ImageSequence
import os, time


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
frames = []
ascii_frames = []
txt_frames = []


def resize(image, new_w=120):
    global new_h
    w, h = image.size
    ratio = h / w / 0.55
    new_h = int(new_w * ratio)
    img_resized = image.resize((new_h, new_w))
    return img_resized


def greyScale(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def convertAscii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)   


def animation():
    for file in os.listdir("Frames"):
        with open(f"Frames/{file}", "r") as f:
            txt_frames.append(f.readlines())
    for i in range(5):
        for frame in txt_frames:
            print("".join(frame))
            time.sleep(0.024)
            os.system("cls")
    return print("Animation Finished!")


def delete():
    for filename in os.listdir("Frames"):
        file_path = os.path.join("Frames", filename)
        os.unlink(file_path)


def main(new_w=120):
    delete()
    with Image.open("cube2.gif") as img:
        for frame in ImageSequence.Iterator(img):
            frames.append(greyScale(resize(frame)))

        for i in range(0, len(frames)):
            new_frame = convertAscii(greyScale(resize(frames[i])))
            pixel_count = len(new_frame)  
            aframe = "\n".join([new_frame[index:(index+new_w)] for index in range(0, pixel_count, new_w)])
            with open(f"Frames/frame{i}.txt", "w") as f:
                f.write(aframe)
            # im.save(f"Frames/Image{i}.png")
        
        animation()

    return

if __name__ == '__main__':
    main() 