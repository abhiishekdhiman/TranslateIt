from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator  

root = Tk()
root.title("Translateit")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background = "SystemButtonFace")


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text = c1)
    label2.configure(text = c2)
    root.after(1000,label_change)


def translate_now():
    text_ = text1.get(1.0,END)
    t1 = Translator()
    trans_text = t1.translate(text_,src = combo1.get(),dest = combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)


#icon
image_icon = PhotoImage(file = "title.png")
root.iconphoto(False,image_icon)


#arrow
arrow_image = PhotoImage(file = "arrow.png")
image_label = Label(root,image = arrow_image,width = 120,)
image_label.place(x = 475,y = 50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


#first combobox
combo1 = ttk.Combobox(root,values = languageV,font = "Consolas 14",state = "r")
combo1.place(x = 110,y = 20)
combo1.set("ENGLISH")

label1 = Label(root,text = "ENGLISH",font = ('Century Gothic',30,'bold'),bg = "white",width = 18,bd = 5,relief = GROOVE)
label1.place(x = 10,y = 50)


#second combobox
combo2 = ttk.Combobox(root,values = languageV,font = "Consolas 14",state = "r")
combo2.place(x = 730,y = 20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root,text = "ENGLISH",font = ('Century Gothic',30,'bold'),bg = "white",width = 18,bd = 5,relief = GROOVE)
label2.place(x = 620,y = 50)


# first frame
f1 = Frame(root,bg = "Black",bd = 5)
f1.place(x = 10,y = 118,width = 440,height = 210)

text1 = Text(f1,font = "Arial 20",bg = "white",relief = GROOVE,wrap = WORD)
text1.place(x = 0,y = 0,width = 430,height = 200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side = "right",fill = 'y')

scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)


# second frame
f2 = Frame(root,bg = "Black",bd = 5)
f2.place(x = 620,y = 118,width = 440,height = 210)

text2 = Text(f2,font = "Arial 20",bg = "white",relief = GROOVE,wrap = WORD)
text2.place(x = 0,y = 0,width = 430,height = 200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side = "right",fill = 'y')

scrollbar2.configure(command = text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)


#translate button
translate = Button(root,text = "Translate",font = ('Century Gothic', 24),activebackground="white",cursor = "hand2",bd = 1,width = 8,height =1,bg = "black",fg = "white",command = translate_now)
translate.place(x = 455,y = 200)

label_change()
root.mainloop()


# System# 8514oem
# Fixedsys
#  Terminal
#  Modern
#  Roman
#  Script
#  Courier
#  MS Serif
#  MS Sans Serif
#  Small Fonts
#  ROG Fonts
#  Marlett
#  Arial
#  Arabic Transparent
#  Arial Baltic
#  Arial CE
#  Arial CYR
#  Arial Greek
#  Arial TUR
#  Arial Black
#  Bahnschrift Light
#  Bahnschrift SemiLight
#  Bahnschrift
#  Bahnschrift SemiBold
#  Bahnschrift Light SemiCondensed
#  Bahnschrift SemiLight SemiConde
#  Bahnschrift SemiCondensed
#  Bahnschrift SemiBold SemiConden
#  Bahnschrift Light Condensed
#  Bahnschrift SemiLight Condensed
#  Bahnschrift Condensed
#  Bahnschrift SemiBold Condensed
#  Calibri
#  Calibri Light
#  Cambria
#  Cambria Math
#  Candara
#  Candara Light
#  Comic Sans MS
#  Consolas
#  Constantia
#  Corbel
#  Corbel Light
#  Courier New
#  Courier New Baltic
#  Courier New CE
#  Courier New CYR
#  Courier New Greek
#  Courier New TUR
#  Ebrima
#  Franklin Gothic Medium
#  Gabriola
#  Gadugi
#  Georgia
#  Impact
#  Ink Free
#  Javanese Text
#  Leelawadee UI
#  Leelawadee UI Semilight
#  Lucida Console
#  Lucida Sans Unicode
#  Malgun Gothic
#  @Malgun Gothic
#  Malgun Gothic Semilight
#  @Malgun Gothic Semilight
#  Microsoft Himalaya
#  Microsoft JhengHei
#  @Microsoft JhengHei
#  Microsoft JhengHei UI
#  @Microsoft JhengHei UI
#  Microsoft JhengHei Light
#  @Microsoft JhengHei Light
#  Microsoft JhengHei UI Light
#  @Microsoft JhengHei UI Light
#  Microsoft New Tai Lue
#  Microsoft PhagsPa
#  Microsoft Sans Serif
#  Microsoft Tai Le
#  Microsoft YaHei
#  @Microsoft YaHei
#  Microsoft YaHei UI
#  @Microsoft YaHei UI
#  Microsoft YaHei Light
#  @Microsoft YaHei Light
#  Microsoft YaHei UI Light
#  @Microsoft YaHei UI Light
#  Microsoft Yi Baiti
#  MingLiU-ExtB
#  @MingLiU-ExtB
#  PMingLiU-ExtB
#  @PMingLiU-ExtB
#  MingLiU_HKSCS-ExtB
#  @MingLiU_HKSCS-ExtB
#  Mongolian Baiti
#  MS Gothic
#  @MS Gothic
#  MS UI Gothic
#  @MS UI Gothic
#  MS PGothic
#  @MS PGothic
#  MV Boli
#  Myanmar Text
#  Nirmala UI
#  Nirmala UI Semilight
#  Palatino Linotype
#  Sans Serif Collection
#  Segoe Fluent Icons
#  Segoe MDL2 Assets
#  Segoe Print
#  Segoe Script
#  Segoe UI
#  Segoe UI Black
#  Segoe UI Emoji
#  Segoe UI Historic
#  Segoe UI Light
#  Segoe UI Semibold
#  Segoe UI Semilight
#  Segoe UI Symbol
#  Segoe UI Variable Small Light
#  Segoe UI Variable Small Semilig
#  Segoe UI Variable Small
#  Segoe UI Variable Small Semibol
#  Segoe UI Variable Text Light
#  Segoe UI Variable Text Semiligh
#  Segoe UI Variable Text
#  Segoe UI Variable Text Semibold
#  Segoe UI Variable Display Light
#  Segoe UI Variable Display Semil
#  Segoe UI Variable Display
#  Segoe UI Variable Display Semib
#  SimSun
#  @SimSun
#  NSimSun
#  @NSimSun
#  SimSun-ExtB
#  @SimSun-ExtB
#  Sitka Small
#  Sitka Small Semibold
#  Sitka Text
#  Sitka Text Semibold
#  Sitka Subheading
#  Sitka Subheading Semibold
#  Sitka Heading
#  Sitka Heading Semibold
#  Sitka Display
#  Sitka Display Semibold
#  Sitka Banner
#  Sitka Banner Semibold
#  Sylfaen
#  Symbol
#  Tahoma
#  Times New Roman
#  Times New Roman Baltic
#  Times New Roman CE
#  Times New Roman CYR
#  Times New Roman Greek
#  Times New Roman TUR
#  Trebuchet MS
#  Verdana
#  Webdings
#  Wingdings
#  Yu Gothic
#  @Yu Gothic
#  Yu Gothic UI
#  @Yu Gothic UI
#  Yu Gothic UI Semibold
#  @Yu Gothic UI Semibold
#  Yu Gothic Light
#  @Yu Gothic Light
#  Yu Gothic UI Light
#  @Yu Gothic UI Light
#  Yu Gothic Medium
#  @Yu Gothic Medium
#  Yu Gothic UI Semilight
#  @Yu Gothic UI Semilight
#  HoloLens MDL2 Assets
#  Agency FB
#  Algerian
#  Book Antiqua
#  Arial Narrow
#  Arial Rounded MT Bold
#  Baskerville Old Face
#  Bauhaus 93
#  Bell MT
#  Bernard MT Condensed
#  Bodoni MT
#  Bodoni MT Black
#  Bodoni MT Condensed
#  Bodoni MT Poster Compressed
#  Bookman Old Style
#  Bradley Hand ITC
#  Britannic Bold
#  Berlin Sans FB
#  Berlin Sans FB Demi
#  Broadway
#  Brush Script MT
#  Bookshelf Symbol 7
#  Californian FB
#  Calisto MT
#  Castellar
#  Century Schoolbook
#  Centaur
#  Century
#  Chiller
#  Colonna MT
#  Cooper Black
#  Copperplate Gothic Bold
#  Copperplate Gothic Light
#  Curlz MT
#  Dubai
#  Dubai Light
#  Dubai Medium
#  Elephant
#  Engravers MT
#  Eras Bold ITC
#  Eras Demi ITC
#  Eras Light ITC
#  Eras Medium ITC
#  Felix Titling
#  Forte
#  Franklin Gothic Book
#  Franklin Gothic Demi
#  Franklin Gothic Demi Cond
#  Franklin Gothic Heavy
#  Franklin Gothic Medium Cond
#  Freestyle Script
#  French Script MT
#  Footlight MT Light
#  FZShuTi
#  @FZShuTi
#  FZYaoTi
#  @FZYaoTi
#  Garamond
#  Gigi
#  Gill Sans MT
#  Gill Sans MT Condensed
#  Gill Sans Ultra Bold Condensed
#  Gill Sans Ultra Bold
#  Gloucester MT Extra Condensed
#  Gill Sans MT Ext Condensed Bold
#  Century Gothic
#  Goudy Old Style
#  Goudy Stout
#  Harlow Solid Italic
#  Harrington
#  Haettenschweiler
#  High Tower Text
#  Imprint MT Shadow
#  Informal Roman
#  Blackadder ITC
#  Edwardian Script ITC
#  Kristen ITC
#  Jokerman
#  Juice ITC
#  Kunstler Script
#  Wide Latin
#  Lucida Bright
#  Lucida Calligraphy
#  Lucida Fax
#  Lucida Handwriting
#  Lucida Sans
#  Lucida Sans Typewriter
#  Magneto
#  Maiandra GD
#  Matura MT Script Capitals
#  Mistral
#  Modern No. 20
#  Monotype Corsiva
#  MT Extra
#  Niagara Engraved
#  Niagara Solid
#  OCR A Extended
#  Old English Text MT
#  Onyx
#  MS Outlook
#  Palace Script MT
#  Papyrus
#  Parchment
#  Perpetua
#  Perpetua Titling MT
#  Playbill
#  Poor Richard
#  Pristina
#  Rage Italic
#  Ravie
#  MS Reference Sans Serif
#  MS Reference Specialty
#  Rockwell Condensed
#  Rockwell
#  Rockwell Extra Bold
#  Script MT Bold
#  Showcard Gothic
#  LiSu
#  @LiSu
#  YouYuan
#  @YouYuan
#  Snap ITC
#  STCaiyun
#  @STCaiyun
#  Stencil
#  STFangsong
#  @STFangsong
#  STHupo
#  @STHupo
#  STKaiti
#  @STKaiti
#  STLiti
#  @STLiti
#  STSong
#  @STSong
#  STXihei
#  @STXihei
#  STXingkai
#  @STXingkai
#  STXinwei
#  @STXinwei
#  STZhongsong
#  @STZhongsong
#  Tw Cen MT
#  Tw Cen MT Condensed
#  Tw Cen MT Condensed Extra Bold
#  Tempus Sans ITC
#  Viner Hand ITC
#  Vivaldi
#  Vladimir Script
#  Wingdings 2
#  Wingdings 3
#  Heebo
#  Cascadia Code ExtraLight
#  Cascadia Code Light
#  Cascadia Code SemiLight
#  Cascadia Code
#  Cascadia Code SemiBold
#  Cascadia Mono ExtraLight
#  Cascadia Mono Light
#  Cascadia Mono SemiLight
#  Cascadia Mono
#  Cascadia Mono SemiBol