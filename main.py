from imgmaker import imgmaker
import pyperclip

print("Initializing imgmaker...")
i = imgmaker()

print()
print("Enter the image URL: ")
url = input()

def hex_to_rgb(hex):
  if hex[0]=='#':
    hex=hex[1:]
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)

print("\nEnter a color for the background in HEX: ")
hexColor = input()

def prGreen(skk):
    print("\033[92m {}\033[00m".format(skk))

caption = f"Did you like this design? Want to express your thoughts? Praises ✨ or criticism 💢, let us know in the comments below!\n\nYou can also rate this design out of 1 to 10.\nSave it for inspiration!\n•\n•\nUI Designed by: {url}\n•\n•\n"
pyperclip.copy(caption)

prGreen("\nCaption copied to clipboard! Write the tags manually.")

print("\nConverting HEX to RGB...")
rgb = hex_to_rgb(hexColor)
bgColor = f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, 1)"
print(f"Background color: {bgColor}")
print("")

print("Generating images...\n")
print("   -> Generating type 1 image...")
# Generate type 1 image
i.generate(
    "type-1.html",
    downsample=False,
    output_file="1.png",
    template_params={
      "bgColor": bgColor,
      "image": url
    },
    width=1080,
    height=1080
)

print("   -> Generating type 2 image...")
# Generate type 2 image
i.generate(
    "type-2.html",
    downsample=False,
    output_file="2.png",
    template_params={
      "bgColor": bgColor,
      "image": url
    },
    width=1080,
    height=1080
)

# Generate type 3 image
for x in range(4):
    print(f"   -> Generating type 3({x+1}) image...")
    offset = -1080 * x
    i.generate(
        "type-3.html",
        downsample=False,
        output_file=f"{3+x}.png",
        template_params={
        "bgColor": bgColor,
        "offset": f"{offset}px",
        "image": url
        },
        width=1080,
        height=1080
    )

print("\nImages generated successfully! Exiting...")

i.close()
