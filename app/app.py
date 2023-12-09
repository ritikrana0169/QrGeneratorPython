from flask import Flask, render_template, request, redirect, url_for
import qrcode
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # Create a QR code using the data
    data = f"Name: {name}\nEmail: {email}\nPhone: {phone}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save('images/'+
             name+'.png')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
