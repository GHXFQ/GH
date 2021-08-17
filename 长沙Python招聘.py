import requests     # 获取数据的第三方库
import re   # 匹配

url = 'https://www.yuanjisong.com/consultant/allcity/python'


# 请求头：模拟人为
headers = {
    'referer': 'https://www.zhipin.com/job_detail/?query=python&city=101250100&industry=&position=',    # 告诉服务器该网页是从哪个页面链接过来的
    'Cookie': 'acw_tc=2760828015980839511341667e6cded4d8ef98ef55c89d6b0ec75074ef5ed0; PHPSESSID=kjqeu50bf1a3h66rr40hual855; Hm_lvt_cc35662e2ca678d8f472ae5ad8a3ae8a=1597842773,1597929667,1598015239,1598083952; Hm_lpvt_cc35662e2ca678d8f472ae5ad8a3ae8a=1598083952',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'     # User-Agent会告诉网站服务器，访问者是通过什么工具来请求的，如果是爬虫请求，一般会拒绝，如果是用户浏览器，就会应答。
}

# 发送请求 > 访问
res = requests.get(url=url, headers=headers)

# 服务器返回响应：源码数据
con = res.content.decode()  # 获取正文数据

# 匹配需要得数据
price = re.findall(r'<span class="rixin-text.*?">(.*?)</span>', con, re.S)       # 单价
time = re.findall(r'<span class="rixin-text.*?">.*?</span>(.*?)</p>', con, re.S)       # 时间
capability = re.findall(r'<span class="job_list_item_title ">技术能力：</span>(.*?)<!--', con, re.S)     # 技术能力

for i, j, k in zip(capability, price, time):
    print("技术能力：%s\n兼职日薪：%s%s  \n" % (i, j, k))
