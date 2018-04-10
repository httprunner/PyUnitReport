#! -*- coding: UTF-8 -*-


import time
import os,sys
import unittest
from urllib.parse import urljoin 
import json
from pyunitreport import HTMLTestRunner
import sched

try:
    import requests
except ImportError:
    raise ImportError('request import fail!')

class learnCenter(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.api_list = api_list
    
    @classmethod
    def tearDownClass(self):
        # Close connection
        pass
     
    def getoptions(self):
        try:
            verbs = requests.options(urljoin(api_list['api'],api_list['path']))
            return verbs.headers['allow']
        finally:
            ##print(self.url)
            return "{} Un-suport http OPTIONS method ".format(api_list['api'])
            
    
class duoqiye_Function(learnCenter):
    """
          接口功能测试
    """    
    
    def test_FT01_TestApi(self):
        """
                  测试接口:发送test消息
        """
        params_dics = {
                      "topic":"test",
                      "message":"this is a send message test"
                       }
        apiPath = urljoin("http://test.openplatform.weilian.cn","/vr-push/sendMsg")
        headers = {'Content-Type':'application/json; charset=UTF-8'}
        apiT = requests.post(apiPath,headers = headers,data=json.dumps(params_dics),hooks=dict(response=self.getoptions()))
        assert(apiT.status_code == 200)
    

    def test_FT01_GetMessages(self):
        """
                            获取消息队列
        """
        params_dics = {
                    "topic":"userorginfo",
                    "receiveGroup":" lizilian"
                       }
        apiPath = urljoin("http://microservice.weilian.cn","/vr-push/getMsg")
        headers={'Content-Type':'application/json; charset=UTF-8'}
        apiT = requests.post(apiPath,headers = headers,data=json.dumps(params_dics))
        assert(apiT.status_code == 200)

    
class duoqiye_Boundary(learnCenter): 
    """
          接口边界值测试
    """ 
    def test_Bd01_TestApi(self):
        """
                            课程详情页的相关推荐接口:发送消息
       """
        params_dics = {
                      "topic":"test",
                      "message":"this is a send message test"
                       }
        apiPath = urljoin("http://test.openplatform.weilian.cn","/vr-push/sendMsg")
        headers={'Content-Type':'application/json; charset=UTF-8'}
        apiT = requests.post(apiPath,headers = headers,data=json.dumps(params_dics))
        assert(apiT.status_code == 200)
    pass

class duoqiye_ParameterSet(learnCenter): 
    """
          接口参数组合测试
    """ 
    pass

class duoqiye_Abnormal(learnCenter): 
    """
             接口异常测试        
             接口使用方收到调用结果status != “200”后根据业务需要自行决定是否重试调用接口。
    """
    pass


class duoqiye_Security(learnCenter): 
    """
         接口安全测试
    """
    pass

class duoqiye_SyncDatas(learnCenter): 
    """
            接口批处理:默认用户组织部门信息每隔 4H 同步一次；
            
           实时处理数据:实时执行，或异步请求接口；
    """
    def test_SD01_realTimeByGevent(self):
        """
        GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily.
        """
        import grequests
        params_sends = {
                      "topic":"test",
                      "message":"this is a send message test"
                       }
        params_gets = {
                        "topic":"userorginfo",
                        "receiveGroup":" lizilian"
                       }        
        header={'Content-Type':'application/json; charset=UTF-8'}
        reqSet = [ grequests.post(urljoin("http://test.openplatform.weilian.cn","/vr-push/sendMsg"),headers=header,data=json.dumps(params_sends),),
                   grequests.post(urljoin("http://test.openplatform.weilian.cn","/vr-push/getMsg"),headers=header,data=json.dumps(params_gets),),
                 ]
        gResp = grequests.map(reqSet)
        for gri in gResp:
            if gri.status_code:
                assert(gri.status_code == 200)
            else:
                self.assertFalse(True,"None Response Messages")

    def prepared_request(self,httpAction='GET',url='http://www.baidu.com',header="",data=""):
        from requests import Request,Session
        s = Session()
        req = Request(httpAction,
                      url,
                       headers = header,
                       data = json.dumps(data)
                    )
        
        prepped = req.prepare()
        resp = s.send(prepped)
        assert(resp.status_code == 200)

    def test_SD02_scheduleBatchDatas(self,inc = 20):
        """
        Execute batch datas or requests with schedule by time, os, sched packages.
        Default intival inc = 20 s
        """
        
        schedule = sched.scheduler(time.time, time.sleep)       
        params_sends = {
                      "topic":"test",
                      "message":"this is a send message test"
                       }
        params_gets = {
                        "topic":"userorginfo",
                        "receiveGroup":" lizilian"
                       } 
        header = {'Content-Type':'application/json; charset=UTF-8'}

        url_test = urljoin("http://test.openplatform.weilian.cn","/vr-push/sendMsg")
        url_getMess = urljoin("http://test.openplatform.weilian.cn","/vr-push/getMsg")
        
        # Set execute sechdule queue

        schedule.enter(20, 0, self.prepared_request, kwargs={'httpAction':'POST','url':url_test,'header':header,'data':params_sends})        
        schedule.enter(20, 0, self.prepared_request, kwargs={'httpAction':'POST','url':url_getMess,'header':header,'data':params_gets})
        schedule.run()


if __name__ == '__main__':
    api_list = {'api':'http://test.openplatform.weilian.cn',
                'path':'/vr-push/sendMsg',
                'name':'trainapi/recommendTrain.do',
                'action':'get',
                'info':'',
                'req_paras':{},
                'resp_paras':{},
                'test_status':'Fail',
                'report_title':'weiningXXZX_duoqiye',
                'output':r"..\..\..\output\TempReport\ApiReport",
                'report_name':'testsuites_name',
                'failfast':True
                }
        
    output = os.path.join(os.path.abspath(api_list['output']),"{}_{}".format(os.path.splitext(os.path.basename(sys.argv[0]))[0] ,time.strftime("%H%M%S", time.localtime())))

    #runner = unittest.TextTestRunner()
    test0 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_Function)
    test1 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_Boundary)
    test2 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_ParameterSet)
    test3 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_Abnormal)
    test4 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_Security)
    test5 = unittest.TestLoader().loadTestsFromTestCase(duoqiye_SyncDatas)
    suite = unittest.TestSuite([test0,test1,test2,test3,test4,test5])
    print(suite.countTestCases())
    runner = HTMLTestRunner(verbosity=2,output=output,report_name="{}_{}".format(os.path.splitext(os.path.basename(sys.argv[0]))[0] ,time.strftime("%H%M%S", time.localtime())),report_title=api_list['report_title'],failfast=False)
    runner.run(suite)

                    