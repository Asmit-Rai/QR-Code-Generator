import qrcode
from PIL import Image
qr = qrcode.QRCode(version =1 , error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4,)
string1 = input("Enter Your Message to Convert into Qr Code:")
qr.add_data(string1)
qr.make(fit=True)
imag = qr.make_image(fill_color="red",back_color="blue")
imag.save("wscube_web.png")


