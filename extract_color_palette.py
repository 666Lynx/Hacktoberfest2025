from PIL import Image

def extract_palette(image_path, n_colors=5, resize_width=200):
    
    # Open and resize image for faster processing
    img = Image.open(image_path).convert('RGB')
    w_percent = resize_width / float(img.size[0])
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((resize_width, h_size))
    
    
    colors = img.getcolors(maxcolors=resize_width * h_size)
    
    if not colors:
        raise ValueError("Too many colors in image — try resizing smaller.")
    
    # Sort by pixel count (most common colors first)
    colors.sort(reverse=True, key=lambda c: c[0])
    
    # Extract top n_colors
    dominant_colors = [color for count, color in colors[:n_colors]]
    return dominant_colors

def rgb_to_hex(color):
    """Convert an RGB color to HEX."""
    return '#{:02x}{:02x}{:02x}'.format(*color)

def save_palette(colors, output_path="palette.png", block_size=100):
    """Create and save a palette image from a list of colors."""
    palette_width = block_size * len(colors)
    palette_height = block_size
    
    palette_img = Image.new('RGB', (palette_width, palette_height))
    
    for i, color in enumerate(colors):
        block = Image.new('RGB', (block_size, palette_height), color)
        palette_img.paste(block, (i * block_size, 0))
    
    palette_img.save(output_path)
    print(f"✅ Saved palette as: {output_path}")

def main():
    image_path = "sukuna-dope-amoled-5120x2880-16950.png"  # Replace the path to your image path
    num_colors = 6                 # Number of colors to extract

    print("Extracting color palette...")
    colors = extract_palette(image_path, num_colors)

    print("\nExtracted Colors:")
    for i, color in enumerate(colors, 1):
        print(f"{i}: RGB {color} | HEX {rgb_to_hex(color)}")

    save_palette(colors, "simple_palette.png")

if __name__ == "__main__":
    main()
