import qrcode

whatsapp_link = "https://wa.me/918770332797?text=Hi%2C%20Please%20send%20me%20the%20menu."

features = qrcode.QRCode(version=1, box_size=20, border=0)
features.add_data(whatsapp_link)
features.make(fit=True)

Generate_Image = features.make_image(fill_color="Black", back_color="White")
Generate_Image.save("WhatsappQR.png")
