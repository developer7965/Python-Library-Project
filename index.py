from tkinter import *
import random

root = Tk()

root.title("Vihaan's Library - Welcome Page")
root.geometry('600x260')
root.config(bg='turquoise')



def member_loginpage():
    member_login = Toplevel()

    member_login.title("Vihaan's Library - Member Login Page")
    member_login.geometry('600x260')
    member_login.config(bg='orange')

    memberlogin_title = Label(member_login,text="Members Login Page",font=('Century',20),bg='blue',fg='violet')
    memberlogin_title.pack(pady=20)

    creds_frame = Frame(member_login,bg='orange')
    creds_frame.pack(pady=12)

    username_ask = Label(creds_frame,text='Name:',font=('Candara',13),bg='green',fg='yellow')
    username_ask.grid(row=0,column=0)

    global username_enter
    username_enter = Entry(creds_frame,font=('Candara',11))
    username_enter.grid(row=0,column=1,padx=5)    

    age_ask = Label(creds_frame,text='Age:',font=('Candara',13),bg='green',fg='yellow')
    age_ask.grid(row=1,column=0,pady=5)

    global age_enter
    age_enter = Entry(creds_frame,font=('Candara',11))
    age_enter.grid(row=1,column=1,padx=5,pady=5)

    login_confirm = Button(member_login,text='Login As Member',font=('Candara',13,'bold'),bg='blue',fg='yellow',command=member_home_page)
    login_confirm.pack(pady=5)
    
    member_login.mainloop()



def member_home_page():
    
    member_homepage = Toplevel()

    member_homepage.title("Vihaan's Online Library - Member Homepage")
    member_homepage.geometry('370x300')
    member_homepage.config(bg='#ffdc00')

    global username
    username = username_enter.get()

    global age
    age = int(age_enter.get())
    
    options_lbl = Label(member_homepage,bg='#ffdc00')
    options_lbl.pack(anchor=N)

    yourprofile_btn = Button(options_lbl,text='Profile',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                             ,command=memberprofile)
    yourprofile_btn.grid(row=0,column=0,padx=2)

    library_btn = Button(options_lbl,text='Library',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                          ,command=library)
    library_btn.grid(row=0,column=1,padx='2')

    popular_books_btn = Button(options_lbl,text='Popular Books',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                               ,command=popularbooks)
    popular_books_btn.grid(row=0,column=2,padx='2')

    

    home_text = Label(member_homepage,
                      text='Hi!\nChoose any of the options above to go to either\nYour Profile, our Booklist or our Popular Books of the Month section!'
                      ,bg='#00ff05',fg='#ff00d5')
    home_text.pack(pady=5)

    member_homepage.mainloop()



def popularbooks():
    pass



def library():
    library = Toplevel()
    
    library.title("Vihaan's Online Library - Library")
    library.geometry('600x600')
    library.config(bg='turquoise')

# aisle 1 - magic & fantasy

    def magicfantasy_aisle():
        magicfantasy_books = Toplevel()

        magicfantasy_books.title("Vihaan's Online Library - Magic & Fantasy Aisle")
        magicfantasy_books.geometry('600x620')
        magicfantasy_books.config()

        magic_book1_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book1.png")

        magic_book2_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book2.png")
        
        magic_book3_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book3.png")

        magic_book4_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book4.png")

        magic_book5_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book5.png")

        magic_book6_img = PhotoImage(file="C:\Coding Work\Python\Python Adv(Ms. Kaur)\Projects\Final Project\Magic Fantasy Aisle\MagicFantasy_Book6.png")

        magic_book1_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book1_cnvs.pack()

        magic_book1_cnvs.create_image(0,0,anchor=NW,image=magic_book1_img)
        magic_book1_cnvs.create_text(196,10,text="Title: Harry Potter & The Sorcerer's Stone",font=("Candara",11))
        magic_book1_cnvs.create_text(132,30,text="Author: J.K. Rowling",font=("Candara",11))


        magic_book2_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book2_cnvs.pack()

        magic_book2_cnvs.create_image(0,0,anchor=NW,image=magic_book2_img)
        magic_book2_cnvs.create_text(150,10,text="Title: Alice in Wonderland",font=("Candara",11))
        magic_book2_cnvs.create_text(136,30,text="Author: Lewis Carroll",font=("Candara",11))


        magic_book3_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book3_cnvs.pack()

        magic_book3_cnvs.create_image(0,0,anchor=NW,image=magic_book3_img)
        magic_book3_cnvs.create_text(197,10,text="Title: The Lion, The Witch & The Wardrobe",font=("Candara",11))
        magic_book3_cnvs.create_text(124,30,text="Author: C.S. Lewis",font=("Candara",11))


        magic_book4_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book4_cnvs.pack()

        magic_book4_cnvs.create_image(0,0,anchor=NW,image=magic_book4_img)
        magic_book4_cnvs.create_text(97,10,text="Peter Pan",font=("Candara",11))
        magic_book4_cnvs.create_text(125,30,text="Author: J.M. Barrie",font=("Candara",11))


        magic_book5_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book5_cnvs.pack()

        magic_book5_cnvs.create_image(0,0,anchor=NW,image=magic_book5_img)
        magic_book5_cnvs.create_text(159,10,text="Title: The Sword in The Stone",font=("Candara",11))
        magic_book5_cnvs.create_text(125,30,text="Author: T.H. White",font=("Candara",11))


        magic_book6_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        magic_book6_cnvs.pack()

        magic_book6_cnvs.create_image(0,0,anchor=NW,image=magic_book6_img)
        magic_book6_cnvs.create_text(117,10,text="Title: The Hobbit",font=("Candara",11))
        magic_book6_cnvs.create_text(133,30,text="Author: J.R.R. Tolkien",font=("Candara",11))

        
        magicfantasy_books.mainloop()

# aisle 2 - history
    def history_aisle():
        history_books = Toplevel()
        
        history_books.title("Vihaan's Online Library - History Aisle")
        history_books.geometry('600x600')
        history_books.config()

        history_book1_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book1.png")

        history_book2_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book2.png")

        #history_book3_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book3.png")

        #history_book4_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book4.png")

        #history_book5_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book5.png")

        #history_book6_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\History Aisle\\History_Book6.png")

        history_book1_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book1_cnvs.pack()

        history_book1_cnvs.create_image(0,0,anchor=NW,image=history_book1_img)
        history_book1_cnvs.create_text(196,10,text="Title: Harry Potter & The Sorcerer's Stone",font=("Candara",11))
        history_book1_cnvs.create_text(132,30,text="Author: J.K. Rowling",font=("Candara",11))


        history_book2_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book2_cnvs.pack()

        history_book2_cnvs.create_image(0,0,anchor=NW,image=history_book2_img)
        history_book2_cnvs.create_text(150,10,text="Title: Alice in Wonderland",font=("Candara",11))
        history_book2_cnvs.create_text(136,30,text="Author: Lewis Carroll",font=("Candara",11))


        history_book3_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book3_cnvs.pack()

        #history_book3_cnvs.create_image(0,0,anchor=NW,image=history_book3_img)
        history_book3_cnvs.create_text(197,10,text="Title: The Lion, The Witch & The Wardrobe",font=("Candara",11))
        history_book3_cnvs.create_text(124,30,text="Author: C.S. Lewis",font=("Candara",11))


        history_book4_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book4_cnvs.pack()

        #history_book4_cnvs.create_image(0,0,anchor=NW,image=history_book4_img)
        history_book4_cnvs.create_text(97,10,text="Peter Pan",font=("Candara",11))
        history_book4_cnvs.create_text(125,30,text="Author: J.M. Barrie",font=("Candara",11))


        history_book5_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book5_cnvs.pack()

        #history_book5_cnvs.create_image(0,0,anchor=NW,image=history_book5_img)
        history_book5_cnvs.create_text(159,10,text="Title: The Sword in The Stone",font=("Candara",11))
        history_book5_cnvs.create_text(125,30,text="Author: T.H. White",font=("Candara",11))


        history_book6_cnvs = Canvas(history_books,width=600,height=100,bg='#d0d0d0')
        history_book6_cnvs.pack()

        #history_book6_cnvs.create_image(0,0,anchor=NW,image=history_book6_img)
        history_book6_cnvs.create_text(117,10,text="Title: The Hobbit",font=("Candara",11))
        history_book6_cnvs.create_text(133,30,text="Author: J.R.R. Tolkien",font=("Candara",11))


        history_books.mainloop()
        

# aisle 3 - mystery
    def mystery_aisle():
        mystery_books = Toplevel()
        
        mystery_books.title("Vihaan's Online Library - Mystery Aisle")
        mystery_books.geometry('600x600')
        mystery_books.config()

        mystery_book1_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book1.png")

        #mystery_book2_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book2.png")

        #mystery_book3_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book3.png")

        #mystery_book4_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book4.png")

        #mystery_book5_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book5.png")

        #mystery_book6_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Mystery Aisle\\Mystery_Book6.png")

        mystery_book1_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book1_cnvs.pack()

        mystery_book1_cnvs.create_image(0,0,anchor=NW,image=mystery_book1_img)
        mystery_book1_cnvs.create_text(189,10,text="Title: Sherlock Holmes: A Story In Scarlet",font=("Candara",11))
        mystery_book1_cnvs.create_text(155,30,text="Author: Arthur Conan Doyle",font=("Candara",11))


        mystery_book2_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book2_cnvs.pack()

        #mystery_book2_cnvs.create_image(0,0,anchor=NW,image=mystery_book2_img)
        mystery_book2_cnvs.create_text(30,10,text="Title: ...",font=("Candara",11))
        mystery_book2_cnvs.create_text(35,30,text="Author: ...",font=("Candara",11))


        mystery_book3_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book3_cnvs.pack()

        #mystery_book3_cnvs.create_image(0,0,anchor=NW,image=mystery_book3_img)
        mystery_book3_cnvs.create_text(30,10,text="Title: ...",font=("Candara",11))
        mystery_book3_cnvs.create_text(35,30,text="Author: ...",font=("Candara",11))


        mystery_book4_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book4_cnvs.pack()

        #mystery_book4_cnvs.create_image(0,0,anchor=NW,image=mystery_book4_img)
        mystery_book4_cnvs.create_text(30,10,text="Title: ...",font=("Candara",11))
        mystery_book4_cnvs.create_text(35,30,text="Author: ...",font=("Candara",11))


        mystery_book5_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book5_cnvs.pack()

        #mystery_book5_cnvs.create_image(0,0,anchor=NW,image=mystery_book5_img)
        mystery_book5_cnvs.create_text(30,10,text="Title: ...",font=("Candara",11))
        mystery_book5_cnvs.create_text(35,30,text="Author: ...",font=("Candara",11))


        mystery_book6_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        mystery_book6_cnvs.pack()

        #mystery_book6_cnvs.create_image(0,0,anchor=NW,image=mystery_book6_img)
        mystery_book6_cnvs.create_text(30,10,text="Title: ...",font=("Candara",11))
        mystery_book6_cnvs.create_text(35,30,text="Author: ...",font=("Candara",11))

        
        mystery_books.mainloop()

# aisle 4 - classics
    def classics_aisle():
        classics_books = Toplevel()
        
        classics_books.title("Vihaan's Online Library - Classics Aisle")
        classics_books.geometry('600x600')
        classics_books.config()

        classics_book1_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book1.png")

        classics_book2_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book2.png")

        classics_book3_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book3.png")

        classics_book4_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book4.png")

        classics_book5_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book5.png")

        classics_book6_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Classics_Book6.png")

        classics_book1_cnvs = Canvas(classics_books,width=600,height=100,bg='#d0d0d0')
        classics_book1_cnvs.pack()

        classics_book1_cnvs.create_image(0,0,anchor=NW,image=classics_book1_img)
        classics_book1_cnvs.create_text(196,10,text="Title: Little Women",font=("Candara",11))
        classics_book1_cnvs.create_text(132,30,text="Author: Louisa May Alcott",font=("Candara",11))


        classics_book2_cnvs = Canvas(classics_books,width=600,height=100,bg='#d0d0d0')
        classics_book2_cnvs.pack()

        classics_book2_cnvs.create_image(0,0,anchor=NW,image=classics_book2_img)
        classics_book2_cnvs.create_text(150,10,text="Title: Adventures of Tom Sawyer",font=("Candara",11))
        classics_book2_cnvs.create_text(136,30,text="Author: Mark Twain",font=("Candara",11))


        classics_book3_cnvs = Canvas(classics_books,width=600,height=100,bg='#d0d0d0')
        classics_book3_cnvs.pack()

        classics_book3_cnvs.create_image(0,0,anchor=NW,image=classics_book3_img)
        classics_book3_cnvs.create_text(197,10,text="Title: Where The Wild Things Are",font=("Candara",11))
        classics_book3_cnvs.create_text(124,30,text="Author: Maurice Sendak",font=("Candara",11))


        classics_book4_cnvs = Canvas(classics_books,width=600,height=100,bg='#d0d0d0')
        classics_book4_cnvs.pack()

        classics_book4_cnvs.create_image(0,0,anchor=NW,image=classics_book4_img)
        classics_book4_cnvs.create_text(97,10,text="A Tale of Two Cities",font=("Candara",11))
        classics_book4_cnvs.create_text(125,30,text="Author: Charles Dickens",font=("Candara",11))


        classics_book5_cnvs = Canvas(xlassics_books,width=600,height=100,bg='#d0d0d0')
        classics_book5_cnvs.pack()

        classics_book5_cnvs.create_image(0,0,anchor=NW,image=classics_book5_img)
        classics_book5_cnvs.create_text(159,10,text="Title: A Christmas carol",font=("Candara",11))
        classics_book5_cnvs.create_text(125,30,text="Author: Charles Dickens",font=("Candara",11))


        classics_book6_cnvs = Canvas(classics_books,width=600,height=100,bg='#d0d0d0')
        classics_book6_cnvs.pack()

        classics_book6_cnvs.create_image(0,0,anchor=NW,image=classics_book6_img)
        classics_book6_cnvs.create_text(117,10,text="Title: Frankenstein",font=("Candara",11))
        classics_book6_cnvs.create_text(133,30,text="Author: Mary Shelley",font=("Candara",11))

        
        classics_books.mainloop()        

# aisle 5 - sci-fi
    def scifi_aisle():
        scifi_books = Toplevel()
        
        scifi_books.title("Vihaan's Online Library - Sci-Fi Aisle")
        scifi_books.geometry('600x600')
        scifi_books.config()

        scifi_book1_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book1.png")

        scifi_book2_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book2.png")

        scifi_book3_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book3.png")

        scifi_book4_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book4.png")

        scifi_book5_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book5.png")

        scifi_book6_img = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Sci-Fi Aisle\\SciFi_Book6.png")

        scifi_book1_cnvs = Canvas(magicfantasy_books,width=600,height=100,bg='#d0d0d0')
        scifi_book1.cnvs.pack()

        scifi_book1_cnvs.create_image(0,0,anchor=NW,image=scifi_book1_img)
        scifi_book1_cnvs.create_text(196,10,text="Title: Harry Potter & The Sorcerer's Stone",font=("Candara",11))
        scifi_book1_cnvs.create_text(132,30,text="Author: J.K. Rowling",font=("Candara",11))


        scifi_book2_cnvs = Canvas(scifi_books,width=600,height=100,bg='#d0d0d0')
        scifi_book2_cnvs.pack()

        scifi_book2_cnvs.create_image(0,0,anchor=NW,image=scifi_book2_img)
        scifi_book2_cnvs.create_text(150,10,text="Title: Alice in Wonderland",font=("Candara",11))
        scifi_book2_cnvs.create_text(136,30,text="Author: Lewis Carroll",font=("Candara",11))


        scifi_book3_cnvs = Canvas(scifi_books,width=600,height=100,bg='#d0d0d0')
        scifi_book3_cnvs.pack()

        scifi_book3_cnvs.create_image(0,0,anchor=NW,image=scifi_book3_img)
        scifi_book3_cnvs.create_text(197,10,text="Title: The Lion, The Witch & The Wardrobe",font=("Candara",11))
        scifi_book3_cnvs.create_text(124,30,text="Author: C.S. Lewis",font=("Candara",11))


        scifi_book4_cnvs = Canvas(mystery_books,width=600,height=100,bg='#d0d0d0')
        scifi_book4_cnvs.pack()

        scifi_book4_cnvs.create_image(0,0,anchor=NW,image=scifi_book4_img)
        scifi_book4_cnvs.create_text(97,10,text="Peter Pan",font=("Candara",11))
        scifi_book4_cnvs.create_text(125,30,text="Author: J.M. Barrie",font=("Candara",11))


        scifi_book5_cnvs = Canvas(scifi_books,width=600,height=100,bg='#d0d0d0')
        scifi_book5_cnvs.pack()

        scifi_book5_cnvs.create_image(0,0,anchor=NW,image=scifi_book5_img)
        scifi_book5_cnvs.create_text(159,10,text="Title: The Sword in The Stone",font=("Candara",11))
        scifi_book5_cnvs.create_text(125,30,text="Author: T.H. White",font=("Candara",11))


        scifi_book6_cnvs = Canvas(scifi_books,width=600,height=100,bg='#d0d0d0')
        scifi_book6_cnvs.pack()

        scifi_book6_cnvs.create_image(0,0,anchor=NW,image=scifi_book6_img)
        scifi_book6_cnvs.create_text(117,10,text="Title: The Hobbit",font=("Candara",11))
        scifi_book6_cnvs.create_text(133,30,text="Author: J.R.R. Tolkien",font=("Candara",11))

        scifi_books.mainloop()        

    aisle_buttons = Label(library,bg='turquoise')
    aisle_buttons.pack(anchor=N)

    magicfantasy_button = Button(aisle_buttons,text='Magic & Fantasy Aisle',bg='#8c14ff',fg='#ff41c8',command=magicfantasy_aisle,anchor='center'
                                 ,font=("Candara",11))
    magicfantasy_button.grid(row=0,column=0,padx=3)

    history_button = Button(aisle_buttons,text='History Aisle',bg='#8c14ff',fg='#ff41c8',command=history_aisle,anchor='center',font=("Candara",11))
    history_button.grid(row=0,column=1,padx=3)

    mystery_button = Button(aisle_buttons,text='Mystery Aisle',bg='#8c14ff',fg='#ff41c8',command=mystery_aisle,anchor='center',font=("Candara",11))
    mystery_button.grid(row=0,column=2,padx=3)

    classics_button = Button(aisle_buttons,text='Classics Aisle',bg='#8c14ff',fg='#ff41c8',command=classics_aisle,anchor='center',font=("Candara",11))
    classics_button.grid(row=0,column=3,padx=3)

    scifi_button = Button(aisle_buttons,text='Sci-Fi Aisle',bg='#8c14ff',fg='#ff41c8',command=scifi_aisle,anchor='center',font=("Candara",11))
    scifi_button.grid(row=0,column=4,padx=3)
    
    library.mainloop()



def memberprofile():
    import random

    member_profile = Toplevel()

    member_profile.title("Vihaan's Online Library - Your Profile")
    member_profile.geometry('600x600')
    member_profile.config(bg='green')

    member_image = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\member_image.png")

    profile_cnvs = Canvas(member_profile,bg='white',height=330,width=400)
    profile_cnvs.pack()
    
    profile_cnvs.create_image(100,100,image=member_image)

    username_show = Label(profile_cnvs,text=f"Username: {username}",fg='indigo',font=('Candara',13))
    username_show.place(x=200,y=20)

    age_show = Label(profile_cnvs,text=f"Age: {age}",fg='indigo',font=('Candara',13))
    age_show.place(x=200,y=50)

    userphotos_list = ["C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\member_image.png", "C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\member_image_boy.png", "C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\member_image_girl.png", "C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\user_img.png"]

    def change_photo():
        member_image.config(file=random.choice(userphotos_list))

    change_photo_btn = Button(profile_cnvs,text="Change User Photo",font=('Candara',13),command=change_photo)
    change_photo_btn.place(x=10,y=193)
    
    borrow1 = "brw1"

    borrow2 = "brw2"

    borrow3 = "brw3"

    borrow4 = 'brw4'

    borrow5 = 'brw5'

    borrowed_books_list = ["Your Borrows:"'1.',borrow1,'2.',borrow2,'3.',borrow3,'4.',borrow4,'5.',borrow5]
    
    chosen_books_show = Label(profile_cnvs,text=borrowed_books_list,bg='blue',fg='yellow')
    chosen_books_show.place(x=2,y=235)

    member_profile.mainloop()
    


def admin_loginpage():

    admin_login = Toplevel()

    admin_login.title("Vihaan's Online Library - Admin Login Page")
    admin_login.geometry('600x600')
    admin_login.config(bg='orange')
    
    adminlogin_title = Label(admin_login,text="Admin Login Page",font=('Century',20),bg='blue',fg='violet')
    adminlogin_title.pack(pady=20)

    admincreds_frame = Frame(admin_login,bg='orange')
    admincreds_frame.pack(pady=12)

    adminname_ask = Label(admincreds_frame,text='Admin Name:',font=('Candara',13),bg='green',fg='yellow')
    adminname_ask.grid(row=0,column=0)

    global adminname_enter
    adminname_enter = Entry(admincreds_frame,font=('Candara',11))
    adminname_enter.grid(row=0,column=1,padx=5)

    admincode_ask = Label(admincreds_frame,text='Admin Code:',font=('Candara',13),bg='green',fg='yellow')
    admincode_ask.grid(row=1,column=0,pady=5)

    admincode_enter = Entry(admincreds_frame,font=('Candara', 11))
    admincode_enter.grid(row=1,column=1,padx=5,pady=5)

    adminage_ask = Label(admincreds_frame,text='Admin Age:',font=('Candara',13),bg='green',fg='yellow')
    adminage_ask.grid(row=2,column=0,pady=5)
    
    global adminage_enter
    adminage_enter = Entry(admincreds_frame,font=('Candara',13))
    adminage_enter.grid(row=2,column=1,padx=5,pady=5)
  
    admin_login_confirm = Button(admin_login,text='Login as Admin',font=('Candara',13,'bold'),bg='blue',fg='yellow',command=admin_homepage)
    admin_login_confirm.pack()

    

    admin_login.mainloop()
    


def admin_homepage():
    
    admin_homepage = Toplevel()

    admin_homepage.title("Vihaan's Online Library - Admin Homepage")
    admin_homepage.geometry('370x300')
    admin_homepage.config(bg='#ffdc00')

    global admin_username
    admin_username = adminname_enter.get()

    global admin_age
    admin_age = adminage_enter.get()
    
    admin_options_lbl = Label(admin_homepage,bg='#ffdc00')
    admin_options_lbl.pack(anchor=N)

    adminprofile_btn = Button(admin_options_lbl,text='Profile',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                             ,command=admin_profile)
    adminprofile_btn.grid(row=0,column=0,padx=2)

    adminbooklist_btn = Button(admin_options_lbl,text='Library',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                          ,command=admin_booklist)
    adminbooklist_btn.grid(row=0,column=1,padx='2')

    admin_popularbooks_btn = Button(admin_options_lbl,text='Popular Books',relief='flat',bg='#ff6eff',fg='#6100fe',font=('Candara',11,'underline'),anchor='center'
                               ,command=admin_popularbooks)
    admin_popularbooks_btn.grid(row=0,column=2,padx='2')

    

    home_text = Label(admin_homepage,
                      text='Hi!\nChoose any of the options above to go to either\nYour Profile, the Booklist (Admin Version) or\nthe Popular Books of the Month (Admin Version) section!'
                      ,bg='#00ff05',fg='#ff00d5',width=52)
    home_text.pack(pady=5)

    admin_homepage.mainloop()


def admin_profile():
    admin_profile = Toplevel()

    admin_profile.title("Vihaan's Online Library - Admin Profile")
    admin_profile.geometry('600x600')
    admin_profile.config(bg='green')

    admin_image = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\admin_img.png")

    adminprofile_cnvs = Canvas(admin_profile,bg='white',height=330,width=400)
    adminprofile_cnvs.pack()
    
    adminprofile_cnvs.create_image(100,100,image=admin_image)

    username_show = Label(adminprofile_cnvs,text=f"Username: {admin_username}",fg='indigo',font=('Candara',13))
    username_show.place(x=200,y=20)

    age_show = Label(adminprofile_cnvs,text=f"Age: {admin_age}",fg='indigo',font=('Candara',13))
    age_show.place(x=200,y=50)

    admin_profile.mainloop()



def admin_booklist():
    pass



def admin_popularbooks():
    pass



title = Label(root,text="Vihaan's Online Library!",font=('Century',20),bg='maroon',fg='silver')
title.pack(pady=20)

welcomelbl = Label(root,text="Hello! I welcome you to Vihaan's Online Library, made using Python!\nPress one of the buttons below to log in as either an admin or a member!"
                   ,bg='#ff00ff',fg='#0000cc',font=('Candara',13),width='82')
welcomelbl.pack()

login_as_prompt = Label(root,text='Login As:',bg='green',fg='yellow',font=('Candara',13))
login_as_prompt.pack(pady=6)

btnframe = Frame(root,bg='turquoise')
btnframe.pack(pady=3)

memberimg = PhotoImage(file="C:\\Coding Work\\Python\\Python Adv(Ms. Kaur)\\Projects\\Final Project\\Other Images\\user_img.png")

memberimg_edited = memberimg.subsample(9,9)

memberimg_show = Label(btnframe,image=memberimg_edited)
memberimg_show.grid(row=0,column=0)

memberbtn = Button(btnframe,text='Member',width=15,bg='#8f00ff',fg='#ffa500',command=member_loginpage,font=('Candara',14))
memberbtn.grid(row=0,column=1,padx=2)

adminbtn = Button(btnframe,text='Admin',width=15,bg='#8f00ff',fg='#ffa500',command=admin_loginpage,font=('Candara',14))
adminbtn.grid(row=0,column=2,padx=2)


root.mainloop()
