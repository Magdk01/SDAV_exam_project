from PIL import Image, ImageDraw, ImageFont
import os


def create_placeholder(name, color, size=(400, 300)):
    # Create image with colored background
    img = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(img)

    # Add text in center
    text = name.replace("-", " ").title()

    # Calculate text position (center)
    text_bbox = draw.textbbox((0, 0), text, font=None)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2

    # Draw text
    draw.text((x, y), text, fill="white")

    return img


# Create directory if it doesn't exist
os.makedirs("assets/images", exist_ok=True)

# Define placeholders with different colors
placeholders = {
    "data-quality": "#3498db",  # Blue
    "trade-volumes": "#2ecc71",  # Green
    "network": "#e74c3c",  # Red
    "gdp-development": "#f39c12",  # Orange/Gold
}

# Generate and save placeholders
for name, color in placeholders.items():
    img = create_placeholder(name, color)
    img.save(f"assets/images/{name}-thumb.png")
