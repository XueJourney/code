import qrcode

def generate_qr_code(error_correction, dot_style, dot_opacity, dot_color, center_icon, dot_scale, locator_style, locator_color, image_format):
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=10,
        border=4
    )

    qr.add_data("Hello, World!")
    qr.make(fit=True)

    qr_code_image = qr.make_image(fill_color=dot_color, back_color="white")

    if center_icon:
        center_icon = center_icon.convert("RGBA")
        icon_width, icon_height = center_icon.size

        qr_code_image_width, qr_code_image_height = qr_code_image.size
        center_icon_width = int(qr_code_image_width / 4)
        center_icon_height = int(qr_code_image_height / 4)

        scaled_icon = center_icon.resize((center_icon_width, center_icon_height))

        qr_code_image.paste(scaled_icon, ((qr_code_image_width - center_icon_width) // 2, (qr_code_image_height - center_icon_height) // 2))

    return qr_code_image

def save_qr_code_image(qr_code_image):
    image_path = "static/images/qr_code.png"
    qr_code_image.save(image_path)
    return image_path