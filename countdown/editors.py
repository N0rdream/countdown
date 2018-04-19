from PIL import Image, ImageFont, ImageDraw


def get_coordinates(x_coordinate, y_coordinate, width):
    return x_coordinate - (width - 4) / 2, y_coordinate


def create_cover(
        countdown, cover_orginal_path, cover_final_path, 
        font_path, color_rgb, color_size, x_coords, y_coords):
    img = Image.open(cover_orginal_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, color_size)
    widths = [draw.textsize(num, font=font)[0] for num in countdown]
    coords = [get_coordinates(*c) for c in zip(x_coords, y_coords, widths)]
    for coord, num in zip(coords, countdown):
        draw.text(coord, num, color_rgb, font=font)
    img.save(cover_final_path, subsampling = 0, quality=100)