from qiniu import Auth, put_file, etag
import qiniu.config
import sys
import datetime
import time
import configparser
if len(sys.argv)==1:
	print("no file")
	exit(0)


config = configparser.ConfigParser()
config.read('qiniu.properties')

#七牛的访问key等
access_key=config.get("qiniu","access_key")
secret_key=config.get("qiniu","secret_key")

host=config.get("qiniu","host")

q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'dd-bb'

#要上传文件的本地路径
localfile = sys.argv[1]

#上传后保存的文件名
t=time.time()
key = 'upload_%s.%s'% (int(round(t*1000)),localfile.split(".")[-1])
# print (key)

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 0)



ret, info = put_file(token, key, localfile, version='v2') 
# print (info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
print(host+ret['key'])
