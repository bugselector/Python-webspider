from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
'''
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
brower = webdriver.PhantomJS(desired_capabilities=dcap)
#brower = webdriver.PhantomJS()
brower.get("http://ac.qq.com/ComicView/index/id/520552/cid/1")
a = brower.get_screenshot_as_file("f:/1.jpg")
for i in range(20):
	#brower.execute_script("window.scrollTo(0,docment.body.scrollHeight)")
	js = "window.scrollTo("+str(i*1280)+","+str((i+1)*1280+")"
	brower.execute_script(js)
	time.sleep(1)	
'''