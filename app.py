from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Function to generate WhatsApp or URL QR code
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        message = request.form['message']
        qr_type = request.form['qr_type']
        
        if qr_type == 'whatsapp':
            # WhatsApp URL format
            data = f"https://wa.me/{phone_number}?text={message}"
        else:
            # Custom URL
            data = message

        # Generate QR code
        img = generate_qr(data)

        # Save to an in-memory buffer
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)

        return send_file(buf, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)