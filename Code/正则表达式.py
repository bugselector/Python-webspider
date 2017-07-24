import re

#普通字符作为原子
string = "tiaoxiadashide"
pat = "xia"
rst = re.search(pat, string)
print(rst)

#非打印字符作为原子：\n, \t,
string = '''tiaoxiadashide
baidu'''
pat = "\n"
rst = re.search(pat, string)
print(rst)

#通用字符作为原子:
#\w(匹配任意一个字母，数字，下划线)
#\W(除字母，数字，下划线)
#\d(十进制数字)
#\D(除十进制)
#\s(空白字符)
#\S(除空白字符)
string = "tiaoxiadashid e12354"
pat = "\s\w\d\d\d"
rst = re.search(pat, string)
print(rst)

#原子表
#[xyz]:任意一个
string = "tiaoxiadashid e12354"
pat = "xi[^bc]da"
rst = re.search(pat, string)
print(rst)

#元字符
'''
.:除换行符以外任意一个字符
^:匹配字符串开始位置
$:匹配结束位置
*:0/1/多次
?:0/1
+:1/多次
{n}:恰好出现n次
{n,}:至少n次
{n,m}:至少n,至多m
|:模式选择
():模式单元
'''
string = "tiaoxiaaaaadashid e12354"
pat = "xia..s"
pat = "ti.*"
pat = "ti.+"
pat = "ti.?"
pat = "a{2,}"
rst = re.search(pat, string)
print(rst)


#模式修正符
'''
I:忽略大小写*
M:多行匹配*
L:本地化识别匹配
U:Unicode
S：让.匹配包括换行符*
'''
string = "Python"
pat = "pyt"
result = re.search(pat,string,re.I)
print(result)

#贪婪模式和懒惰模式
string = "poythonyfgfgcgfh"
pat1 = "p.*y"
pat2 = "p.*?y"
result = re.search(pat1,string,re.I)
print(result)
result2 = re.search(pat2,string,re.I)
print(result2)

#正则表达式函数
#1、match
string = "poythonyfgfgcgfh"
pat2 = "p.*?y"
result = re.match(pat2,string,re.I)
print(result)
#2、search
#3、全局匹配函数
string = "poythpopnyfpgyfgcgfh"
pat2 = "p.*?y"
result = re.compile(pat2).findall(string)
print(result)

#实例: .com和.cn
string="<a href='http://www.baidu.com'>百度首页</a>"
pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
rst = re.compile(pat).findall(string)
print(rst)
#实例：电话号码
string = "gjmhgmgj0100-2525123ihiikj255-21122013"
pat = "\d{4}-\d{7}|\d{3}-\d{8}"
rst = re.compile(pat).findall(string)
print(rst)




















