
import qrcode
import argparse

# Get parameters
p = argparse.ArgumentParser()
p.add_argument('--body-no',   type=str, default='F2FA123456', help='Body Number')
p.add_argument('--dom',       type=str, default='내수', help='내수 or 해외')
p.add_argument('--coat-time', type=str, default='1 20-03-02 10:00', help='상도 투입 일시')
p.add_argument('--color1',    type=str, default='YT', help='Color1')
p.add_argument('--color2',    type=str, default='투톤YT', help='Color2')
p.add_argument('--model',     type=str, default='F2', help='Vehicle Type')
p.add_argument('--insp-time', type=str, default='20-02-02 12:20', help='검사일시')
p.add_argument('--count',     type=str, default='02', help='투입 횟수')

# Load parameters
args = p.parse_args()

# QR Code Configuration
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

# Generate data
data = '%'.join([args.body_no, args.dom, args.coat_time, args.color1, args.color2, args.model, args.insp_time, args.count])
print(data)

# Generate QR Code
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save QR Code to png file
img.save('test.png')
