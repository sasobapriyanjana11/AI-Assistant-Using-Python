# my user agent is : Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)

#https://www.google.com/search?q=weather+galle&sca_esv=5a0334d7f5ed8bb6&sxsrf=AHTn8zr4BbVyeJ1S7li-_yody9ZmsgnFPA%3A1738477224062&source=hp&ei=pw6fZ9CVOeaLnesPm9XxuAw&iflsig=ACkRmUkAAAAAZ58cuFFXCGcxK_XIxojFjruPk0spYT_f&oq=weather+sr&gs_lp=Egdnd3Mtd2l6Igp3ZWF0aGVyIHNyKgIIADIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIlS9QrQRYmCRwAXgAkAEAmAGkAaABmgqqAQQwLjEwuAEByAEA-AEBmAILoALLC6gCCsICBxAjGCcY6gLCAgoQIxjwBRgnGOoCwgILEAAYgAQYkQIYigXCAgoQABiABBhDGIoFwgILEAAYgAQYsQMYgwHCAhAQABiABBixAxhDGIMBGIoFwgIOEAAYgAQYsQMYgwEYigXCAg0QABiABBixAxhDGIoFwgIWEC4YgAQYsQMY0QMYQxiDARjHARiKBcICCxAAGIAEGLEDGIoFwgIIEC4YgAQYsQPCAhAQABiABBixAxhDGMkDGIoFwgILEAAYgAQYsQMYkgPCAggQABiABBiSA8ICFRAAGIAEGLEDGEMYyQMYigUYRhiAAsICCxAAGIAEGJIDGIoFmAMg4gMFEgExIEDxBWMGkREjdg35kgcEMS4xMKAHmUA&sclient=gws-wiz

from requests_html import HTMLSession
import spech_to_text

def Weather():
    s  =  HTMLSession()
    query = "Galle"
    url = f'https://www.google.com/search?q=weather+{query}'
    r  = s.get(url , headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})

    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" "+unit+" "+ desc

