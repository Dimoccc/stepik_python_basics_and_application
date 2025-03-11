import requests, re, sys

for line in sys.stdin:
    line = line.strip()
    request = requests.get(line)
    text = request.text


    # text = """<a href="http://www.liveinternet.ru/click" target=_blank><img src="http://pics.rbc.ru/img/ver99/counter_liveinternet.gif" border=0 width=31 height=31 title="liveinternet.ru"></a>
    #         <a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://turist.ru/goods/"><img width=150 height=100 alt="turbo.ru" src="http://turbo.ru/turbo_pics/uniora/90/240/350/a839c3fac974f93478606906dda54e77_150x100.jpg"></a><br>';
    #         <li><a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.nissan-avtogrand.ru/news/news.php?id=40">Суперусловия по покупке автомобилей Nissan 2008 г.в.</a></li>
    #         <li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459494' >В Сеуле дебютирует седан KIA VG</a></li><li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459452' >Российский завод Toyota остановил производство на неделю</a></li><li><a href='http://redir.rbc.ru/cgi-bin/redirect.cgi?http://www.autonews.ru/automarket_news/index.shtml?2009/03/30/1459434' >Сегодня Путин проведет совещание на АвтоВАЗе</a></li>"""
    all_body_link = re.findall(r"<a\s+([\w*|\s*|=|\'|\"|\.|:|//|-]*)", text)

    arr_link = []
    for one_link in all_body_link:
        link = re.findall(r"href=(?:\"|\')(?:https://|http://|ftp://)?(?!\.{2}/)(?P<domen>[\w\d\.-]+)(?:\"|\'|/|:)",
                          one_link)
        if len(link) > 0:
            arr_link.append(link[0])

    list_link = list(set(arr_link))
    list_link.sort()
    for link in list_link:
        print(link)