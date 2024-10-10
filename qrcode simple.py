# Method - 1 
import qrcode
features = qrcode.QRCode(version=1, box_size=20, border = 0)
features.add_data("https://drive.google.com/uc?export=download&id=1rvRDgSp8flH74LsiUg1m_LpyWuxwWcXA")
features.make(fit=True)
Generate_Image = features.make_image(fill_color = "Black", back_colour="White")
Generate_Image.save("Download Resume.png")

# Method - 2
# import qrcode
# img =  qrcode.make("https://drive.google.com/uc?export=download&id=1rvRDgSp8flH74LsiUg1m_LpyWuxwWcXA")
# img.save('Resume1.png')
# img.show("Resume1.png")
