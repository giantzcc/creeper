# -*- coding: utf-8 -*-

import json
import os
import shutil
import urllib

class OnePieceDao(object):
    def __init__(self,path):
        self.__basePath=path
        if not os.path.exists(path):
            os.mkdir(path)
        dirs = os.listdir(self.__basePath)
        self.nums = [int(x) for x in dirs if x.isdigit()]

    #   获取已下载的最新的期号
    def getLatestNum(self):
        return max(self.nums)

    #   下载的数量超过16话删除最早的
    def deletePrevious(self, num=16):
        while len(self.nums)>16:
            index=min(self.nums)
            shutil.rmtree(os.path.join(self.__basePath, str(index)))
            self.nums.remove(index)

    #   为更新的话创建新目录
    def create(self, num):
        os.mkdir(os.path.join(self.__basePath,str(num)))
        self.nums.append(num)

    #   将所有url对应的图片下载并保存到指定的文件夹中
    def save(self, urls, num):
        dpath=os.path.join(self.__basePath, str(num))
        for url in urls:
            try:
                urllib.request.urlretrieve(url,os.path.join(dpath,os.path.split(url)[1]))
            except Exception as e:
                print('cannot load picture from %s'%url)

    #   每一话的基本信息以json方式保存在指定文件夹中
    def saveInfo(self,item):
        info=json.dumps(item, default=lambda p:p.__dict__, ensure_ascii=False)
        path=os.path.join(self.__basePath, str(item.episode))
        if not os.path.exists(path):
            self.create(item.episode)
        else:
            return False
        path = os.path.join(path, 'info.json')
        with open(path, 'wb') as f:
            f.write(info.encode('utf-8'))
        return True

    #   在每一话的基本信息里添加图片的顺序信息
    def savePicOrderInfo(self,num,orderinfo):
         dpath = os.path.join(self.__basePath, str(num))
         dpath = os.path.join(dpath, 'info.json')
         info=''
         with open(dpath,'rb') as f:
             info = f.read().decode(encoding='utf-8')
         obj = json.loads(info)
         obj['orderinfo']=orderinfo
         info = json.dumps(obj, default=lambda p: p.__dict__, ensure_ascii=False)
         with open(dpath, 'wb') as f:
             f.write(info.encode('utf-8'))

