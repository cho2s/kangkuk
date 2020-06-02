
# sudo apt-get install zbar-tools
import pyzbar.pyzbar as pyzbar
import cv2
import matplotlib.pyplot as plt
import pprint
import time

IMG_FILE = 'dojang_test5.jpg'

# Output format
result = \
    {
        'BODY_NO': '',
        'DOM': '',
        'COAT_TIME': '',
        'COLOR1': '',
        'COLOR2': '',
        'MODEL': '',
        'INSP_TIME': '',
        'COUNT': ''
    }


def meta_extractor(decoded):
    sep_cnt = str.count(decoded, '%')
    if sep_cnt < 7:
        print('Detection ERROR. Not enough information found')
        return ''

    return decoded.split('%')

# Load Image
img = cv2.imread(IMG_FILE)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
start_time = time.time()

# Find QRcode and decode
decoded = pyzbar.decode(gray)

# Extract meta information
for d in decoded:
    if d.type == 'QRCODE':
        dec_ = meta_extractor(d.data.decode('utf-8'))

        if dec_ != '':
            (result['BODY_NO'],
             result['DOM'],
             result['COAT_TIME'],
             result['COLOR1'],
             result['COLOR2'],
             result['MODEL'],
             result['INSP_TIME'],
             result['COUNT']) = dec_

        pprint.pprint(result)

print(time.time() - start_time)