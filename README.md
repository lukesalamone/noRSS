# noRSS
![logo](https://raw.githubusercontent.com/lukesalamone/noRSS/master/logo.png)

These scripts allow you to closely monitor web pages for changes. This is useful for a wide variety of applications where RSS feeds are unavailable or insufficient for your needs. noRSS provides a simple solution, which additionally preserves the privacy of your email address.

## Configuration
1. Edit line 7 of `script.py` to the url of the webpage you would like to monitor:  
  * Example: `url = "http://google.com/"`
2. Edit line 19 of `script.py` so that it correctly targets the element you would like to monitor. Webpages may contain random information which is not relevant to your monitoring, so this allows you to limit the scope to pertinent information only.  
  * Example: `elem = soup.p`  
  * To monitor the whole page, use `elem = soup.prittify()`
  * For more information, see the [official documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree).  
3. Edit line 3 of `email.php` to contain your email address.  
  * Example: `$to = "example@example.com";`  
4. You may need to add the email address found on line 6 of `email.php` to your address book. Change it to whatever you like.
5. Add `script.py` as a cron job.
  * For more information about adding cron jobs, [click here](http://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/).
