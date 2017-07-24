from selenium import webdriver
import time
from lxml import etree
brower = webdriver.PhantomJS()
brower.get("http://www.baidu.com")
brower.get_screenshot_as_file("f:/1.jpg")
brower.find_element_by_xpath('//*[@id="kw"]').clear()
brower.find_element_by_xpath('//*[@id="kw"]').send_keys("爬虫")
brower.find_element_by_xpath('//*[@id="su"]').click()
for i in range(0,5):
    brower.implicitly_wait(5)
    brower.get_screenshot_as_file("f:/2.jpg")
    data = brower.page_source

    print(len(data))
    treedata = etree.HTML(data)
    rst = treedata.xpath('//div[@class="c-tools"]/@data-tools')
    print(rst)
    brower.find_element_by_xpath('//*[@id="page"]/a[10]').click()
brower.quit()