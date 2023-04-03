from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Get uploaded image
    image = request.files['image']

    # Convert image to PDF
    with io.BytesIO() as file:
        with Image.open(image) as img:
            img.save(file, format='PDF')
        pdf_data = file.getvalue()

    # Save PDF to file
    with open('file.pdf', 'wb') as f:
        f.write(pdf_data)

    # Render page with download link
    return render_template('home.html', pdf_link='/download')

@app.route('/download')
def download():
    # Send PDF file for download
    return send_file('file.pdf', as_attachment=True)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get input values
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = int(100)

    # Calculate result
    result = (x * y) / z

    # Check if a is provided
    a = request.form.get('a')
    if a:
        result += float(a)

    # Render page with result
    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
