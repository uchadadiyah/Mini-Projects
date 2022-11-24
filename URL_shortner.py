import pyshortoners

url = input("Enter the Url:")

def shortenurl(url):
    s = pyshortoners.shortener()
    print(s.tinyurl.short(url))

shortenurl(url)    
