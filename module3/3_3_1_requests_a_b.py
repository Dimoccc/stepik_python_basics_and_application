import requests, re

a = input().replace('stepic.org', 'stepik.org')
b = input().replace('stepic.org', 'stepik.org')

all_links = []

site =requests.get(a).text
print('site = ',site)
links = re.findall("href=[\"\'](.*?)[\"\']", site)
print('links = ', links)
for link in links:
    html = requests.get(link.replace('stepic.org', 'stepik.org')).text
    print('html = ', html)
    cycle_sites = re.findall("href=[\"\'](.*?)[\"\']", html)
    print('cycle_sites = ', cycle_sites)
    cycle_sites = list(map(lambda x: x.replace('stepic.org', 'stepik.org'), cycle_sites))
    print('cycle_sites = ', cycle_sites)
    all_links.extend(cycle_sites)
    print('call_links = ', all_links)

if b in all_links:
    print("Yes")
else:
    print("No")