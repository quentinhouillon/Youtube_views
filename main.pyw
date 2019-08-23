from tkinter import *
from json import dump, load
from os import chdir, getcwd, startfile

from module.clss import *

def youtube():
    chdir(getcwd())

    with open("file\\theme.json", "r") as theme:
        th = load(theme)

    with open("file\\run.json", "r") as run:
        value = load(run)
        value[0]["value_entry"] = ""

    #VARIABLES
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]

    window = Tk()
    ft = "consolas"
    v = Views()
    var_entry = StringVar()

    #CALLBACK
    def save_entry():
        with open("file\\run.json", "w") as f:
            entry_val = entry.get().strip()
            value[0]["url_entry"] = entry_val
            dump(value, f, indent=4)

    def restart():
        window.destroy()
        youtube()

    def find():
        entry = Entry(main, bg=color1, fg=color2, textvariable=var_entry,
                      insertbackground=color2, font=ft)

        v.delete_url()
        restart()


    def show_entry():
        gu = v.get_url()

        try:
            lbl_entry.config(text=gu["text"])
            entry.pack(fill="x", anchor="n")
            save_url.pack(side="left", anchor="s")

        except:
            run()
            lbl_lnk.config(text=gu["text_save"], fg=gu["color"])

    def run():
        try:
            save_entry()
            ds = v.display_search()

            lbl_error.config(text="")
            lbl_entry.config(text="")
            subscribers.config(text=ds["sub"])
            views.config(text=ds["view"])
            find_url.pack(side="left", anchor="s")
            enter.config(text=ds["update"], command=v.display_search)
            lbl_lnk.config(text=value[0]["url_entry"], fg="blue")

            entry.destroy()
            save_url.destroy()

        except:
            lbl_error.config(text=ds["text"], fg=ds["color"])

    def run_entry(event):
        run()

    def save():
        entry = Entry(main, bg=color1, fg=color2, textvariable=var_entry,
                    insertbackground=color2, font=ft)

        # v = Views()    
        
        run()
        su = v.save_url()
        lbl_lnk.config(text=su["text_save"], fg=su["color"])

    def delete():
        entry = Entry(main, bg=color1, fg=color2, textvariable=var_entry,
                    insertbackground=color2, font=ft)

        # v = Views()    
        v.delete_url()

    #WINDOW
    window.title("youtube - views")
    window.iconbitmap("img\\youtube.ico")
    window.geometry("555x250")
    window.resizable(False, False)
    window.configure(bg=color1)
    window.focus_force()

    #FRAME
    main = Frame(window, bg=color1)
    footer = Frame(window, bg=color3)

    #LABEL
    show_img = Label(main, bg=color1)
    lbl_entry = Label(main, bg=color1, fg=color2, font=ft)
    lbl_error = Label(main, bg=color1, fg="red", font=ft)
    lbl_lnk = Label(window, bg=color1, font=ft)

    subscribers = Label(main, bg=color1, fg=color2, font=ft, padx=10, pady=5)
    views = Label(main, bg=color1, fg=color2, font=ft, padx=10, pady=5)

    #BUTTON
    save_url = Button(footer, text="sauver l'url", bg="blue", fg=color2, padx=15,
                    command=save)

    find_url = Button(footer, text="trouver une url", bg="brown", fg=color2, padx=15,
                    command=find)

    enter = Button(footer, text="entrer", bg="green", fg=color2, padx=15,
                command=run)

    #ENTRY
    entry = Entry(main, bg=color1, fg=color2, textvariable=var_entry,
                insertbackground=color2, font=ft)
    entry.focus()
    entry.bind("<Return>", run_entry)

    #PACK
    subscribers.pack(fill="x", side="left")
    show_img.pack(anchor="center")
    views.pack(fill="x", side="right")
    lbl_entry.pack(fill="x", anchor="n")
    lbl_error.pack(fill="x", anchor="center")
    main.pack(fill="x", expand="true")

    lbl_lnk.pack(fill="x")

    enter.pack(side="right", anchor="s")
    footer.pack(fill="x", side="bottom")

    show_entry()
    window.mainloop()

if __name__ == "__main__":
    youtube()
