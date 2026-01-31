from PIL import Image

# Load the images
image1 = Image.open("costumes/costume1.gif")
image2 = Image.open("costumes/costume2.gif")

# Save as animated GIF
image1.save(
    "costumes/animated.gif",
    save_all=True,
    append_images=[image2],
    duration=200,  # milliseconds per frame
    loop=0         # 0 = infinite loop
)
