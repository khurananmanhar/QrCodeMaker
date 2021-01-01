#pip install qrcode[pil]
import qrcode

#qr = qrcode.make('Hello World')
#qr.save('QR.png')

qr = qrcode.QRCode(
	version = 1,
	box_size = 15,
	border = 7
)

data = 'QrCodeMaker'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qr.png')
