
from flask import Flask
from flask import request
from flask_cors import CORS
from m_w_test_danmu import *
app = Flask(__name__)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ

@app.route('/danmu/bilibili', methods=['GET', 'POST'])
def bilibili_danmu():
# 获取弹幕
    if request.method == 'GET':
        cid = request.args.get("aid") 
        md5_id = request.args.get("id") 
        if cid :
            if os.path.exists("./archive/%s" % cid):
                with open('archive/'+ cid + '.json') as f:
                    payload = f.read()
                    f.close()
            else:
                payload = bulid_dm_json(cid)
                print(cid)
                write_json(payload,cid)

        elif len(md5_id) > 10:
            try:
                with open('archive_md5/'+ md5_id + '.json') as f:
                    payload = f.read()
                    f.close()
            except:
                from_md5_write_json(md5_id)
                payload = {'code': 0, 'data':[]}
        else:
            payload = {'code': 0, 'data':[]}
        return payload
# 添加弹幕
    if request.method == 'POST':
        payload = request.get_json(silent=True)
        if len(payload['id']) > 10:
            file_location = './archive_md5/%s.json' %(payload['id'])
        else:
            file_location = './archive/%s.json' %(payload['id'])
        update_danmu(file_location,payload['time'],payload['type'],payload['color'],payload['text'])
        return {'code': 0}

 
 
if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    # app.run('0.0.0.0', debug=True, port=5000,ssl_context=('k.pem', 'k.key'))
    # app.run('0.0.0.0', debug=True, port=5000)
    app.run(debug=True)
