#encoding:utf-8
#!/usr/bin/python
from bs4 import BeautifulSoup
import re
import requests
import csv
import operator
import pyecharts
import collections
from pyecharts.charts import Pie,Map,WordCloud,Bar
from pyecharts.globals import SymbolType
from pyecharts import options as opts
from collections import Counter

def get_html_weather(url):
    req = requests.get(url)
    print(req.encoding)
    html = req.text.encode('iso-8859-1')
    html_utf = html.decode('iso-8859-1').encode('utf-8')

    soup = BeautifulSoup(html,"html.parser")
    text_list = []
    trs = soup.find_all('tr')
    for tr in trs:
        tdlist = []
        for td in tr:
            if td.string is None:
                td_final = re.sub("[\n]","",td.text)
                if td_final == '':
                    continue
                else:
                    tdlist.append(td_final)
            else:
                td_final2 = re.sub("[\n]", "", td.string)
                if td_final2 == '':
                    continue
                else:
                    tdlist.append(td_final2)
        if len(tdlist) == 9:
            tdlist = tdlist[1:8]
        elif len(tdlist) == 8:
            tdlist = tdlist[:7]
        elif len(tdlist) == 6:
            tdlist.insert(0,'')
        elif len(tdlist) == 5:
            tdlist = tdlist[1:]
        text_list.append(tdlist)
    print(text_list)


    csvfile1 = open('weather1.csv','a',encoding= 'utf-8', newline='')
    csvfile2 = open('weather2.csv', 'a', encoding='utf-8', newline='')
    '''
    csvfile3 = open('weather3.csv', 'a', encoding='utf-8')
    csvfile4 = open('weather4.csv', 'a', encoding='utf-8')
    csvfile5 = open('weather5.csv', 'a', encoding='utf-8')
    csvfile6 = open('weather6.csv', 'a', encoding='utf-8')
    csvfile7 = open('weather7.csv', 'a', encoding='utf-8')
    '''
    writer1 = csv.writer(csvfile1)
    writer2 = csv.writer(csvfile2)
    '''
    writer3 = csv.writer(csvfile3)
    writer4 = csv.writer(csvfile4)
    writer5 = csv.writer(csvfile5)
    writer6 = csv.writer(csvfile6)
    writer7 = csv.writer(csvfile7)
    '''
    t=int(len(text_list)/7)
    for i in range(t):
        if i==0 or i==1:
            continue
        else:
            if operator.eq(text_list[i],text_list[0]) or operator.eq(text_list[i],text_list[1]):
                continue
            else:
                writer1.writerow(text_list[i])
    for i in range(t,t*2):
        if i== (t-1) or i == t:
            continue
        else:
            if operator.eq(text_list[i],text_list[t-1]) or operator.eq(text_list[i],text_list[t]):
                continue
            else:
                writer2.writerow(text_list[i])
    '''
    for i in range(t*2,t*3):
        writer3.writerow(text_list[i])
    for i in range(t*3,t*4):
        writer4.writerow(text_list[i])
    for i in range(t*4,t*5):
        writer5.writerow(text_list[i])
    for i in range(t*5,t*6):
        writer6.writerow(text_list[i])
    for i in range(t*6,t):
        writer7.writerow(text_list[i])
    '''




    print('ok')

def get_colum(num) -> dict:
    with open('weather1.csv','r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [columns[num] for columns in reader]
        dic = collections.Counter(column)

        if '' in dic:
            dic.pop('')
        return dic

def get_city_temp() -> dict:
    with open('weather1.csv','r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [columns[0] for columns in reader]
        csvfile.close()
    with open('weather1.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        column2 = [columns[6] for columns in reader]

    dic = dict(zip(column,column2))
    print(dic)

    return dic





def analysis_weather():
    dic = get_colum(4)
    weather_count_list = [list(z) for z in zip(dic.keys(),dic.values())]
    print(weather_count_list)
    pie = (
        Pie()
            .add("",weather_count_list)
            .set_colors(['red','blue','green','white','yellow','black','pink','peach','gray'])

    )
    pie.render('weather.html')

def analysis_weather_zhu():
    dic = get_colum(4)

    bar = (
        Bar()
        .add_xaxis(list(dic.keys()))
        .add_yaxis("天气情况分析",list(dic.values()))
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(name='城市数量'),
            xaxis_opts=opts.AxisOpts(name='天气情况'),

        )
    )
    bar.render('weather_bar.html')
def weather_area():
    dic = get_city_temp()
    area_list = [list(z) for z in zip(dic.keys(),dic.values())]
    print(area_list)
    map=(
        Map()
        .add("华东地区夜间最低温度分析",area_list,"china")
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=200)
        )
    )
    map.render('area.html')
def word():
    dic = get_colum(4)
    word_count_list = [list(z) for z in zip(dic.keys(),dic.values())]
    print(word_count_list)

    word_cloud=(
        WordCloud()
        .add("",word_count_list,word_size_range=[20,100],shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title="天气情况"))
    )
    word_cloud.render('word_cloud.html')


if __name__ == "__main__":
    '''
    url2 = 'http://www.weather.com.cn/textFC/hd.shtml#4'
    get_html_weather(url2)
    '''
    #analysis_weather()
    #weather_area()
    word()
    #analysis_weather_zhu()

