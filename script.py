from StringIO import StringIO
from bs4 import BeautifulSoup
import pycurl
import md5
import subprocess

url = "URL-TO-MONITOR"

# open stored hash
with open('hash', 'r') as myFile:
    oldHash = myFile.read().replace('\n', '')

# curl url
storage = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()
html = storage.getvalue()

soup = BeautifulSoup(html, 'html.parser')
elem = soup.table # Modify this line!
html = str(elem)

# hash the page content
newHash = md5.new(html).hexdigest()

# open stored hash
with open('hash', 'r') as myFile:
    oldHash = myFile.read().replace('\n', '')

if len(oldHash) != 0:
	# send notification if changed
	if newHash != oldHash:
		# execute php email script
		subprocess.call("php email.php " + url, shell=True)
	
# save newHash to file
hashFile = open("hash", "w")
hashFile.write(newHash)
hashFile.close()
