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
            return {"text": "entrer l'url youtube de la chaine"}

        else:
            self.url = self.f[0]["url"]
            return {"text_save": self.url,
                    "color": "green"}

    def _search(self):
        try:
            if "about" in self.url:
                self.source = requests.get(self.url)

            else:
                self.source = requests.get(f"{self.url}about")

        except:
            return {"text": "url incorrecte",
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

        except:
            return {"text":"url invalide",
                    "color": "red"}

        return {"sub": f"abonnées \n\n{subscriber}",
                "view": f"vues \n\n{view}",
                "update": "actualiser"}

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
            return {"text": "trouvé"}
        
        else:
            return {"text": "supprimer"}

