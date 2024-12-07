from flask import Flask, send_file, abort, jsonify
import barcode
from barcode.writer import ImageWriter
import io
import base64

app = Flask(__name__)

def generate_ean8_barcode(code):
    if len(code) != 8 or not code.isdigit():
        abort(400, description="Invalid EAN-8 code")

    ean = barcode.get('ean8', code, writer=ImageWriter())
    buffer = io.BytesIO()
    ean.write(buffer)
    buffer.seek(0)
    return buffer


@app.route('/ean8/<code>', methods=['GET'])
def generate_barcode(code):
    buffer = generate_ean8_barcode(code)
    return send_file(buffer, mimetype='image/png')

@app.route('/ean8/base64/<code>', methods=['GET'])
def generate_barcode_base64(code):
    buffer = generate_ean8_barcode(code)
    base64_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return base64_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222)