from bs4 import BeautifulSoup
from json import load, dump
from PIL import Image, ImageTk
import requests

class Views:
    def __init__(self):
        with open("file\\run.json", "r") as file:
            self.f = load(file)

        self.get_url()
        
    def get_url(self):
        if not self.f[0]["url"]:
            with open("file\\run.json", "r") as file:
                self.f = load(file)

            self.url = self.f[0]["url_entry"]
            return {"text": "enter youtube/about(a propos) url"}

        else:
            self.url = self.f[0]["url"]
            return {"text_save": self.url,
                    "color": "green"}

    def _get_img(self):
        url = requests.get(self.url)
        soup = BeautifulSoup(url.text, "lxml")
        soup = soup.find('div', id='appbar-content').find('img').get('src')
        self.d_image = requests.get(soup)

    def display_img(self):
        self._get_img()

        with open("img\\avatar.png", "wb") as file:
            file.write(self.d_image.content)

        im = Image.open("img\\avatar.png")
        im.save("img\\tk_avatar.png")

        avatar = ImageTk.PhotoImage(file="img\\avatar.png")

    def _search(self):
        try:
            self.source = requests.get(self.url)

        except:
            return {"text": "url not found",
                    "color": "red"}

    def display_search(self):
        self.get_url()
        self._search()
        try:
            soup = BeautifulSoup(self.source.text, "lxml")
            data = soup.find("div", class_="style-scope ytd-c4-tabbed-header-renderer")
            data = soup.find_all("span", class_="about-stat")

            subscriber = data[0].text
            view = data[1].text
            print("ca a marché")

        except:
            return {"text":"url invalid",
                    "color": "red"}

        return {"sub": f"subscribers \n\n{subscriber}",
                "view": f"views \n\n{view}",
                "update": "update"}

    def save_url(self):
        self.f[0]["url"] = self.f[0]["url_entry"]

        with open("file\\run.json", "w") as file:
            dump(self.f, file, indent=4)
        
        return {"text_save": self.url,
                    "color": "green"}
    
    def delete_url(self):
        with open("file\\run.json", "w") as file:
            self.f[0]["url"] = ""
            self.f[0]["url_entry"] = ""
            dump(self.f, file, indent=4)
    
    def btn(self):
        if len(self.f[0]["url"]) == 0:
            return {"text": "find"}
        
        else:
            return {"text": "delete"}
