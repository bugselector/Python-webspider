# crawl-comments
使用urllib库，正则表达式，IP代理，用户代理，并将爬取数据写入mysql数据库。

由于fiddler软件配置的复杂性，本文利用单纯的浏览器进行抓包分析。不过，还是最好把fiddler软件配置好。本文中，利用搜狗浏览器（其他也可以）的开发者工具（F12键）来实现对腾讯视频《楚乔传》最新短评的爬取。
用到的工具：1、搜狗浏览器（用来抓包分析）。
                      2、新建一个Word文件，用来保存相关的数据，进行分析。

抓取网站：https://v.qq.com/tv/p/topic/cqzzt/index.html。

实现目标：爬取最新短评下的所有评论。

一、分析

（1）打开页面，按“F12”，再对网页进行刷新。便能够发现许多加载出的页面，选择JS（动态成的页面），进行查找。有了上一次的经验，找不了多久，应该就会发现。

（2）再把其他的点开查看，刚好是最新评论下的内容。而且，数一下条数，刚好与最新评论下显示出来的相同。于是再结合上一笔记已经发现的规律，可以发现很多问题了。把这个链接保存到文档中，并做好标记。
https://coral.qq.com/article/1966037100/comment?commentid=0&reqnum=10&tag=&callback=jQuery112409468861236485373_1498521559355&_=1498521559356

精简之后：
https://coral.qq.com/article/1966037100/comment?commentid=0&reqnum=10&callback=jQuery

是不是有看到“reqnum”了，对的，就是代表显示的评论总数。当我们修改它时，会返回不同的评论。（具体请看笔记：http://bbs.fishc.com/thread-89708-1-1.html）。但是，最终发现，“reqnum”最多只能返回50条，在增大也是返回50条。那么多评论，显然不可能只有50条。于是，点击“加载更多”观察情况。

（3）最终我们发现：

把链接复制下来：
https://coral.qq.com/article/1966037100/comment?commentid=6285142538073027582&reqnum=20&tag=&callback=jQuery112409468861236485373_1498521559355&_=1498521559357

精简之后：
https://coral.qq.com/article/1966037100/comment?commentid=6285142538073027582&reqnum=20&callback=jQuery

我们改变“reqnum”字段的值，发现也最多只有50条。

（4）再来“加载更多”试试：

再次变“reqnum”字段的值，发现也最多只有50条。但是，我们发现一个问题:commentid字段的值发生了改变，于是，我们猜测：是不是一个commentid对应50条评论。于是，我们去找，发现正是如此。

（5）于是，到了这个地方，就大功告成了。提取评论的内容只需简单的正则表达式即可。关键在于提取commentid。于是，我们打算这样做：
爬取第一条评论链接，获取commentid的值，再依次爬取这些页面，获得评论和commentid的值，依次爬取。这样的话，几乎可以爬取所有的最新评论。
来试试吧。

二、实践才是王道


我们从第一个评论页面开始爬取，即这个链接：
https://coral.qq.com/article/1966037100/comment?commentid=0&reqnum=10&callback=jQuery

为了尽可能多的爬取，我们将reqnum设置为50（最大为50条）。在我编写爬虫时时这个结果，以后的话就按分析结果来做。于是，爬取链接可以为：
https://coral.qq.com/article/1966037100/comment?commentid=评论ID号&reqnum=50&callback=jQuery

提取评论内容的正则：
pat1 = '"content":"(.*?)",'

提取id号的正则：
pat2 = '{"id":"(.*?)",'

完整代码:就在这里
