from flask import Flask, send_file
import barcode
from barcode.writer import ImageWriter
import io

app = Flask(__name__)

@app.route('/ean8/<code>', methods=['GET'])
def generate_barcode(code):
    if len(code) != 8 or not code.isdigit():
        return "Invalid EAN-8 code", 400

    ean = barcode.get('ean8', code, writer=ImageWriter())
    buffer = io.BytesIO()
    ean.write(buffer)
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222)