from segno import helpers
qrcontact = helpers.make_mecard(name="Sreenika Myakala", email="sreeenikamyakala@gmail.com", phone="+918919088693")
qrcontact.designator
'3-L'
qrcontact.save("qrscontact.png", scale = 12, dark = "blue", light = "white")