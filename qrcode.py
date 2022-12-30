import segno

myQr =  segno.make("https://github.com/Sreenika-dev?tab=repositories")
myQr.save("myRepos.png",scale = 15, border=3)
