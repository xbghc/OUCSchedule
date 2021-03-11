import requests
import execjs
from PIL import Image
from pylab import *
import base64
import MKIcs

login_url = 'http://jwgl.ouc.edu.cn/cas/login.action'
class OucSchedule:
    def __init__(self):
        self.session=requests.Session()
        self.session.headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "Cache-Control":"no-cache",
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'jwgl.ouc.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
   

    def Login(self,username,password):

        def InpYzm():
            res=self.session.get('http://jwgl.ouc.edu.cn/cas/login.action')

            time.sleep(1)

            res = self.session.get(url="http://jwgl.ouc.edu.cn/cas/genValidateCode",params={
            "datetime":"{} GMT 0800 (GMT 08:00)".format(time.asctime(time.localtime(time.time())))
            })


            with open('yzm.jpg','wb') as f:
                f.write(res.content)
            img=Image.open('./yzm.jpg')
            plt.imshow(img)
            axis('off')
            plt.show()
            self.yzm=input('请输入验证码')
        InpYzm()

        txt_mm_length=len(password)


        with open('functions.js','r',encoding='utf8') as f:
            ctx=execjs.compile(f.read())
            text_mm_expression=ctx.call('checkpwd',password)
            username=ctx.call('un',username,self.session.cookies['JSESSIONID'])
            password=ctx.call('pw',password,self.yzm)
        

        p_username="_u"+self.yzm
        p_password="_p"+self.yzm






        datas = {
            p_username: username,
            p_password: password,
            'randnumber': self.yzm,
            'isPasswordPolicy': '1',
            'txt_mm_expression': text_mm_expression, #密码规则
            'txt_mm_length': txt_mm_length,  #密码长度
            'txt_mm_userzh': '0'
        }
        res = self.session.post('http://jwgl.ouc.edu.cn/cas/logon.action', data=datas)

        res=self.session.get('http://jwgl.ouc.edu.cn/frame/Main_index.jsp')
        self.session.headers['Referer']="http://jwgl.ouc.edu.cn/frame/Main_index.jsp"

        res=self.session.post('http://jwgl.ouc.edu.cn/frame/Main_tools.jsp')
        self.session.headers['Referer']='http://jwgl.ouc.edu.cn/frame/Main_tools.jsp'


        res=self.session.get('http://jwgl.ouc.edu.cn/frame/Desk.new.jsp')
        self.session.headers['Referer']="http://jwgl.ouc.edu.cn/frame/Desk.new.jsp"


        self.session.post('http://jwgl.ouc.edu.cn/cms/bbsSchoolNoticeJson.action',data={'recordsPerPage':'12'})
        self.session.post('http://jwgl.ouc.edu.cn/docmanager/bbsFileInfoJson.action')
        res=self.session.post('http://jwgl.ouc.edu.cn/frame/desk/showLessonScheduleDetailJson.action')



    def GetCourse(self,week):

        res=self.session.post('http://jwgl.ouc.edu.cn/frame/desk/showLessonScheduleDetailJson.action',data={'jxz':week})

        return res.text

    def MkIcsfile(self):
        MKIcs.MKIcs(self)


S=OucSchedule()
S.Login('username','password')
S.MkIcsfile()


