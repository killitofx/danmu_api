# danmu_api  

## 部署

1. 进入data文件夹  
`cd data`

2. 创建Docker镜像  
`docker build -t danmuapi .`  

3. 创建容器  
windows下  
`docker run -v d:\WorkSpace\danmuapi\data\:/root/project -d -p 5000:5000 danmuapi`  
linux下  
`docker run -v /root/danmu_api/data:/root/project -d -p 5000:5000 danmuapi`  

## 使用

1. 无bilibili cid，使用大于十位的hash码,将创建一个空的弹幕池
`http://localhost:5000/danmu/bilibili?id=1dff9080d143f87f96000839911563c1`

2. 有bilibili_cid，将从Bilibili下载弹幕
`http://localhost:5000/danmu/bilibili?aid=163388508`

3. 提交弹幕，POST方法提交json  
提交链接 `http://localhost:5000/danmu/bilibili`  
提交内容
`{"token": "tokendemo",
"id": "1dff9080d143f87f96000839911563c1",  
"author": "DIYgod",  
"time": 0,  
"text": "第一",  
"color": 16777215,  
"type": 0}`  
