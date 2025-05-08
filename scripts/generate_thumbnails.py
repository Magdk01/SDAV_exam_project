from PIL import Image, ImageDraw, ImageFont
import os


def create_placeholder_image(
    title,
    filename,
    size=(600, 400),
    bg_color="#f0f0f0",
    text_color="#333333",
    accent_color="#007bff",
):
    """Create a placeholder image with a title and some visual elements"""
    # Create new image with background
    image = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(image)

    # Add some visual elements
    # Draw a border
    border_width = 10
    draw.rectangle(
        [0, 0, size[0] - 1, size[1] - 1], outline=accent_color, width=border_width
    )

    # Draw some decorative lines
    line_spacing = 40
    for y in range(line_spacing, size[1], line_spacing):
        draw.line([(0, y), (size[0], y)], fill=accent_color, width=1)

    # Add title text
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    # Calculate text position to center it
    text_bbox = draw.textbbox((0, 0), title, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2

    # Draw text with a subtle shadow
    draw.text((text_x + 2, text_y + 2), title, font=font, fill="#00000033")
    draw.text((text_x, text_y), title, font=font, fill=text_color)

    # Save the image
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)
    print(f"Created {filename}")


def main():
    # Define the thumbnails to create with their colors
    thumbnails = [
        {
            "title": "Data Quality\nAnalysis",
            "filename": "assets/images/data-quality-thumb.png",
            "color": "#3498db",  # Blue
        },
        {
            "title": "Trade Volumes\nAnalysis",
            "filename": "assets/images/trade-volumes-thumb.png",
            "color": "#2ecc71",  # Green
        },
        {
            "title": "GDP\nDevelopment",
            "filename": "assets/images/gdp-development-thumb.png",
            "color": "#f39c12",  # Orange/Gold
        },
        {
            "title": "Network\nAnalysis",
            "filename": "assets/images/network-thumb.png",
            "color": "#e74c3c",  # Red
        },
    ]

    # Create each thumbnail
    for thumb in thumbnails:
        create_placeholder_image(
            thumb["title"],
            os.path.join("SDAV_exam_project", thumb["filename"]),
            accent_color=thumb["color"],
        )


if __name__ == "__main__":
    main()
