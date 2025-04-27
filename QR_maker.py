# Import the qrcode module as qr
import qrcode as qr

# Make image using 'make' ,and give link inside the " --- " and put value inside the 'img'
img = qr.make("https://www.davacademic.in/")

# Save img with the name inside " --- "
img.save("DAV_ACADEMIC_WEBSITE.png")
