from bs4 import BeautifulSoup
import time
import datetime
def DayToStr(date):
    return "{}{}{}".format(date.year,str(date.month).zfill(2),str(date.day).zfill(2))


StartTimeLst=["T080000","T090000","T101000","T111000","T133000","T143000","T153000","T163000","T173000","T183000","T193000","T203000"]
EndTimeLst=["T085000","T095000","T110000","T120000","T142000","T152000","T162000","T172000","T182000","T192000","T202000","T212000"]



def GetTime(week,day,num): #返回[开始时间，结束时间]
    startday=datetime.date(2021,3,1)
    theDay=startday+datetime.timedelta(weeks=week-1,days=day-1)
    return [DayToStr(theDay)+StartTimeLst[num-1],
    DayToStr(theDay)+EndTimeLst[num-1]
    ]




   

def MakeEventStr(name,location,starttime,endtime,uid):
    s='BEGIN:VEVENT\n\
SUMMARY:{}\n\
DTSTART:{}\n\
DTEND:{}\n\
UID:{}\n\
DESCRIPTION:\n\
LOCATION:{}\n\
END:VEVENT\n'.format(name,starttime,endtime,uid,location)
    return s



def MKIcs(S):
    with open('Schedule.ics','w',encoding='utf8') as f:
        f.write('BEGIN:VCALENDAR\n\
VERSION:2.0\n\
PRODID:\n\
METHOD:PUBLISH\n\
TZID:Asia/Shanghai\n\
X-WR-CALNAME:课表\n')
        for week in range(1,20):
            time.sleep(1)
            text=S.GetCourse(week)
            text=text.replace('\n','')
            soup=BeautifulSoup(text,'lxml')
            CNlst=soup.table.tbody.find_all('tr') #tr是一行，i+1就是节数
            for CN in range(len(CNlst)):
                DNlst=CNlst[CN].find_all('td')

                for DN in range(len(DNlst)-7,len(DNlst)):
                    courseNameAndInfo=DNlst[DN].text.strip() #td是星期，DN就是星期数

                    if courseNameAndInfo:
                        #分离课程名字、教室
                        pos=courseNameAndInfo.rfind('(')
                        courseName=courseNameAndInfo[:pos]
                        location=courseNameAndInfo[pos+1:-1]


                        starttime,endtime=GetTime(week,DN-len(DNlst)+8,CN+1)

                        uid='{}-{}-{}'.format(week,DN-len(DNlst)+8,CN+1)
                        f.write(MakeEventStr(courseName,location,starttime,endtime,uid))
            
        f.write('END:VCALENDAR')




