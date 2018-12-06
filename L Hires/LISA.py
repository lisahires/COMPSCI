import pyautogui as pg
import webbrowser as wb
points = 0
show = pg.prompt("What is your favorite show? ")
if show == "Vampire Diaries":
    pg.alert("That's a really good show!")
    wb.open ("https://www.youtube.com/watch?v=BmVmhjjkN4E")
    points += 20
elif show == "Youtube":
    pg.alert("I love the dolan twins")
    wb.open ("https://www.youtube.com/watch?v=yyh98Hz-YzA")
elif show == "dora the explorer":
    pg.alert ("memes")
    wb.open ("https://www.youtube.com/watch?v=Fm6YSvdnvww")
    points += 10000000000000000000000000000000000000098281818901890
elif show == "Law and Order":
    pg.alert ("SAME")
    wb.open ("http://www.videocally.com/Alex%20spizzirri/musically-account/24552622")
elif show == "Ni hao kilan":
    pg.alert ("dank memes")
    wb.open ("https://www.youtube.com/watch?v=96cbcIUmmRc")
    points += 9999999999999999999999999999999999999999000
elif show == "Stranger Things":
    pg.alert ("supper spooky")
elif show == "Family guy":
    pg.alert ("so funny")
    wb.open ("https://www.youtube.com/watch?v=jyAYOL7KIxc") 
    points += 727373197973889128918799998998
else:
    pg.alert("Your favorite show is " + show)
    points -= 1000000000000

sport = pg.prompt ("What is your fav sport")
if sport == "soccer":
    pg.alert ("good.")
    points += 1000000
elif sport == "horse riding":
    pg.alert ("hype")
    wb.open ("http://www.videocally.com/Alex%20spizzirri/musically-account/24552622")
    points += 66126361878167167127621672
elif sport == "hockey":
    pg.alert ("wow cold")
    points -=  7777777
    wb.open ("http://www.videocally.com/Alex%20spizzirri/musically-account/24552622")
elif sport == "field hockey":
    pg.alert ("wow back pain")
    points -= 9892823923
    wb.open ("http://www.videocally.com/Alex%20spizzirri/musically-account/24552622")
elif sport == "surfing":
    pg.alert ("sharks will bite you")
    points -= 78298239239823
    wb.open ("http://www.videocally.com/Alex%20spizzirri/musically-account/24552622")
elif sport == "Football":
    pg.alert ("fun")
    points += 278979342987297892
else:
    pg.alert ("so great")
    points -= 8238932989898

food = pg.prompt ("What is your favorite food? ")
if food == "I don't eat":
    pg.alert ("Thats not too good")
    points += 89181298198198129
    wb.open ("https://www.youtube.com/watch?v=2jUbdyWH8I8")
elif food ==  "french fries":
    pg.alert ("Thats a lot of sodium!")
    points += 9891278789197108281291297121231278
    wb.open ("https://www.youtube.com/watch?v=xqiRtYBrEjs")
elif food == "fish":
    pg.alert ("can't relate")
    points -= 91889910800912980123089189108913
elif food == "fruit":
    pg.alert ("can't relate")
    points -= 9812398298129812397842389278942398
    wb.open ("https://www.youtube.com/watch?v=BTs5FS66IUI")
elif food == "chocolate":
    pg.alert ("good job")
    points += 982781278929728797823971129872238729810931208132081303
elif food == "veggies":
    pg.alert ("oof")
    points -= 92901010920120190109190120910912
    wb.open ("https://www.youtube.com/watch?v=uKWcIaJtS6Q")
else:
    pg.alert ("wow so healthy")
    points -= 1111111

singer = pg.prompt ("who is your favorite singer")
if singer == "post malone":
    pg.alert ("SAME")
    points += 9282932908390909389380190812398013980931280912309013912
    wb.open ("https://www.youtube.com/watch?v=2fIWfLIBFj0&list=PL-1x4S2lU9bQnWYHGZEBtSbKO7_nf_XTn")
elif singer == "travis scott":
    wb.open ("https://www.youtube.com/watch?v=NtQqup0RUjg&list=PLS-rtCRab9YV-Hdylrw0JmQeewqXbP5Vp")
    points += 9129898718171281228312309238928344237629827982871296312389129319
elif singer == "myself":
    wb.open ("https://www.youtube.com/watch?v=uvMASEoYPuo")
    points -= 89209130938091820918201
elif singer == "taylor swift":
    pg.alert ("ew no")
    points -= 91281820209819100180192801201910921808101091291220912
else:
    pg.alert ("that's a good singer!")
    points -= 8728898


school = pg.prompt("Whats your favorite place on earth")
if school == "school":
    pg.alert ("go yeet yourself")
    points -= 889898888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    wb.open ("https://www.google.com/search?q=go+yeet+yourself&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjXw9W9jsXeAhVCU98KHTqRDPcQ_AUIEygB&biw=1152&bih=403#imgrc=6omKifNWW_HJpM:")
elif school == "Greenwich":
    pg.alert ("Can't relate")
    points -= 898778128998892198289128991298129812829821982198219812899821
elif school == "Caribbean":
    pg.alert ("Same")
    points += 29801208128182380390109210921092901290219021900920909090912092190210219
elif school == "Alaska":
    pg.alert ("really cold")
    points -=911891290901209190129012091212
elif school == "russia":
    pg.alert ("yikes")
    points +=98818381983127891937898317178923713897138913897219837
elif school == "Connecticut":
    pg.alert ("can't relate")
    points -=871879189737891378918937813798123
else:
    pg.alert ("ok")
    points +=9812891298120912

    
pg.alert ("Your points is" + str(points))
