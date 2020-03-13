# api = "https://api.bilibili.com/x/v1/dm/list.so?oid=79844930" #cid
# cid = "https://api.bilibili.com/x/player/pagelist?aid="
# url_get_comment_cid = "https://comment.bilibili.com/%d.xml"

import requests
import json
import collections
import sys
import os
from bs4 import BeautifulSoup


def bulid_dm_json(cid):
    data = []
    url = "https://comment.bilibili.com/%s.xml" % str(cid)
    r = requests.get(url)
    r.encoding = 'gbk2312'
    soup = BeautifulSoup(r.text,'xml')
    list_i = soup.find_all('d')
    # t = 0
    for i in list_i:
        # kv = [float(i.attrs['p'].split(',')[0]),int(i.attrs['p'].split(',')[1]),int(i.attrs['p'].split(',')[3]),i.attrs['p'].split(',')[6],i.text]
        kv = [float(i.attrs['p'].split(',')[0]),int(5),int(i.attrs['p'].split(',')[3]),i.attrs['p'].split(',')[6],i.text]
        data.append(kv)
        # t+=1
    dt = {'code':0,'data':data}
    return(json.dumps(dt))
    

def write_json(data,cid):
    # if not os.path.exists("./archive/%s" % aid):
    #     os.makedirs("./archive/%s" % aid)
    #     print('文件夹%s创建成功' % aid,end='')
    with open( "./archive/%s.json" % (cid),"w") as f:
        f.write(data)


def m_write_json(data,cid):
    # if not os.path.exists("./archive/%s" % aid):
    #     os.makedirs("./archive/%s" % aid)
    #     print('文件夹%s创建成功' % aid,end='')
    with open( "./missevan_archive/%s.json" % (cid),"w") as f:
        f.write(data)


def from_md5_write_json(id_md5):
    data = {'code':0,'data':[]}
    data = json.dumps(data)
    if not os.path.exists("./archive_md5/%s.json" % id_md5):
        print('正在创建%s.json' % id_md5)
        with open( "./archive_md5/%s.json" % id_md5,"w") as fs:
            fs.write(data)
            fs.close()

def update_danmu(location,dm_time,dm_type,dm_color,dm_text,user='dplayeru'):
    with open (location,'r+') as f:
        data = f.read()
        data = json.loads(data)
        f.close()
        # print(data)
    new_dm =[dm_time, dm_type, dm_color, user, dm_text]
    temp = data['data']
    temp.append(new_dm)
    njs = {"code":0,"data":temp}
    with open (location,'w+') as f:
        f.write(json.dumps(njs))
        f.close()




def m_bulid_dm_json(sid):
    data = []
    url = "https://www.missevan.com/sound/getdm?soundid=%s" % str(sid)
    r = requests.get(url)
    r.encoding = 'gbk2312'
    soup = BeautifulSoup(r.text,'xml')
    list_i = soup.find_all('d')
    # t = 0
    for i in list_i:
        ps = int(i.attrs['p'].split(',')[1])
        if ps == 4:
            tp = 2
        else:
            tp = 0
        # kv = [float(i.attrs['p'].split(',')[0]),int(i.attrs['p'].split(',')[1]),int(i.attrs['p'].split(',')[3]),i.attrs['p'].split(',')[6],i.text]
        # kv = [float(i.attrs['p'].split(',')[0]),int(5),int(i.attrs['p'].split(',')[3]),i.attrs['p'].split(',')[6],i.text]
        kv = [float(i.attrs['p'].split(',')[0]),int(tp),int('16777215'),i.attrs['p'].split(',')[6],i.text]
        data.append(kv)
        # t+=1
    dt = {'code':0,'data':data}
    return(json.dumps(dt))

# if __name__ == '__main__':
#     import socket
#     import json
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(('0.0.0.0', 9997))
#     print("program start")
#     while True:
#         # 接收数据:
#         data, addr = s.recvfrom(1024)
#         # print ('Received from %s:%s.' % addr)
#         data = data.decode()
#         # print(data)
#         data = json.loads(data)
#         print(data)
#         if data['method'] == 'download':
#             aid = data['aid']  
#             print(aid,aid.isdigit(),end='')
#             # print(aid.isdigit())
#             if aid.isdigit() == True: #如果输入的是av号
#                 # cid_list = from_aid_get_cid(aid)
#                 # for cid in cid_list:
#                 cid = aid
#                 write_json(bulid_dm_json(cid),cid)
#                 # call_server(aid,cid)
        
#         if data['method'] == 'update':
#             send_time = data['time']
#             send_type = data['type']
#             send_content = data['text']
#             send_color = data['color']
#             send_id = data['id']
#             if send_id.isdigit() == True:
#                 # cid = from_aid_get_cid(send_id)[0]
#                 cid = send_id
#                 file_location = './archive/%s.json' %(send_id,cid)
#                 update_danmu(file_location,send_time,send_type,send_color,send_content)
#                 print("update success %s" % file_location)
#             else:
#                 file_location = './archive_md5/%s.json' %(send_id)
#                 update_danmu(file_location,send_time,send_type,send_color,send_content)
#                 print("update success %s" % file_location)
        
#         if data['method'] == 'check':
#             dm_id = data['id']
#             if len(dm_id) >10:
#                 from_md5_write_json(dm_id)
#             else:
#                 if dm_id.isdigit() == True: #如果输入的是av号
#                     cid = dm_id
#                     if not os.path.exists("./archive/%s.json" % cid):
#                         write_json(bulid_dm_json(cid),cid)
#                         print("弹幕cid：%s装载完毕，准备发射" % cid)

#         if data['method'] == 'mcheck':
#             dm_id = data['id']
#             if len(dm_id) >10:
#                 # from_md5_write_json(dm_id)
#                 pass
#             else:
#                 if dm_id.isdigit() == True: #如果输入的是av号
#                     sid = dm_id
#                     if not os.path.exists("./missevan_archive/%s.json" % sid):
#                         m_write_json(m_bulid_dm_json(sid),sid)
#                         print("M站弹幕sid：%s装载完毕，准备发射" % sid)
#     #         # print(dm_id)

        


        
