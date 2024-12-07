# EAN-8 Barcode Generator API

This project is a Flask API that generates EAN-8 barcodes in PNG format.

## Requirements

- Python 3.x
- Flask
- python-barcode
- Pillow

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bymcs/ean8-barcode.git
    cd ean8-barcode
    ```

2. Install the required packages using pip:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python main.py
    ```

2. Access the API at:
    - `http://localhost:2222/ean8/<code>`
    - `http://<your-ip>:2222/ean8/<code>`
    - `http://localhost:2222/ean8/base64/<code>`
    - `http://<your-ip>:2222/ean8/base64/<code>`

## Example

To get the PNG image of the EAN-8 barcode, use the following command:
```sh
curl http://localhost:2222/ean8/22293992
