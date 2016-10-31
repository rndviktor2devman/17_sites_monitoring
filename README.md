# 17_sites_monitoring

__Monitor sites state__

---

Purpose of the script - to monitor state of provided sites list
Script checks if the site is alive(responses with status 200)
and checks if domain expires in 30 days

---
####usage:
type
python3 check_sites_health [path to sites list file]

Mandatory parameter - [path to sites list file]. The file should contain
sites urls, each url in separate line.