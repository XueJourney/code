from flask import Flask, render_template, request
from qr_code_generator import qr_code
from utils.logger import log_qr_code_generation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        error_correction = request.form.get('error_correction')
        dot_style = request.form.get('dot_style')
        dot_opacity = request.form.get('dot_opacity')
        dot_color = request.form.get('dot_color')
        center_icon = request.files.get('center_icon')
        dot_scale = request.form.get('dot_scale')
        locator_style = request.form.get('locator_style')
        locator_color = request.form.get('locator_color')
        image_format = request.form.get('image_format')

        qr_code_image = qr_code.generate_qr_code(error_correction, dot_style, dot_opacity, dot_color,
                                                 center_icon, dot_scale, locator_style, locator_color, image_format)

        qr_code_path = qr_code.save_qr_code_image(qr_code_image)

        log_qr_code_generation(request.remote_addr, qr_code_path)

        return render_template('qr_code.html', qr_code_path=qr_code_path)

    return render_template('qr_code.html')

@app.route('/log')
def log():
    with open('logs/qr_code_logs.txt', 'r') as file:
        log_content = file.read()

    return render_template('log.html', log_content=log_content)

if __name__ == '__main__':
    app.run(debug=True)