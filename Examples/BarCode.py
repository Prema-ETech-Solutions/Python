# Genrate QR code @pythoncodess
# Import QRCode from pyqrcode
import pyqrcode
# import png 
from pyqrcode import QRCode
S = "Prem Dangle"
# Generate QR code
url = pyqrcode.create( S) 
url.svg("MY_QR.svg", scale = 8)
url.png("MY_QR.png", scale = 6) 