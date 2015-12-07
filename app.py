#coding: utf-8

from selenium import webdriver
import sys


def inputData(_from,_to,_w,_time):
    driver = webdriver.PhantomJS()
    driver.get("http://transit.yahoo.co.jp/")
    driver.find_element_by_name("from").send_keys(_from)
    driver.find_element_by_name("to").send_keys(_to)
    if _w=="d":
        driver.find_element_by_id("tsDep").click()
    elif _w=="a":
        driver.find_element_by_id("tsArr").click()
    if "/" in _time:
        time=_time.split("/")

        year=time[0]
        month=time[1]
        day=time[2]

        hour=time[3]
        minute=time[4]

        driver.find_element_by_name("y").send_keys(year)
        driver.find_element_by_name("m").send_keys(month)
        driver.find_element_by_name("d").send_keys(day)
        driver.find_element_by_name("hh").send_keys(hour)
        driver.find_element_by_id("mm").send_keys(minute)
    driver.find_element_by_id("searchModuleSubmit").submit()

    #resultPage

    planTime=driver.find_element_by_css_selector(".routeSummary .time span").text
    stationList=driver.find_elements_by_css_selector("#route01 .station dl dt a")
    pastTime=driver.find_elements_by_css_selector("#route01 .station .time li")
    trainList=driver.find_elements_by_css_selector("#route01 .routeDetail .fareSection .transport div")

    time=planTime.split(u"→")
    departureTime=time[0][:5]
    arrivalTime=time[1][:5]

    for i in range(len(trainList)):
        trainList[i]=trainList[i].text[10:]

    print planTime
    for i in range(len(stationList)):
        if i==0:
            print pastTime[i].text+" "+stationList[i].text
            print "↓"
            print "("+trainList[i]+")"
            print "↓"
        elif i==len(stationList)-1:
            print pastTime[len(pastTime)-1].text+" "+stationList[i].text
        else:
            print pastTime[i+(i-1)].text+" "+pastTime[i+(i-1)+1].text+" "+stationList[i].text
            print "↓"
            print "("+trainList[i]+")"
            print "↓"


if __name__=="__main__":
    param=sys.argv
    tfrom=param[1].decode("utf-8")
    to=param[2].decode("utf-8")
    mode=param[3].decode("utf-8")
    time=param[4].decode("utf-8")
    inputData(tfrom,to,mode,time)
