# -*- coding: utf-8 -*-
"""
根据all_region_information_center.csv文件内的数据，绘制各个区域的热点图
整体思路是先找到每个商区的中心点坐标和所有的坐标值，并将这两部分分别写入example_kong.html文件的指定位置
"""
import pandas as pd

df_all=pd.read_csv('all_region_information_center.csv',encoding='utf-8')
list_region=list(set(list(df_all['商区']))) #商区构成的列表
for region in list_region: #遍历商区
    print(region)
    df_region=df_all[df_all['商区']==region] #当前商区的所有数据
    str_region_lnglat=str(df_region['商区中心经度'].median())+','+str(df_region['商区中心纬度'].median()) #当前商区中心
    str_temp_all=''
    for index in df_region.index:
        lng=df_region['经度'][index]  
        lat=df_region['纬度'][index]
        count=50  #表征单个点颜色深浅 最大为100 这里统一取为50
        #将该商区下所有点的经纬度坐标拼接成一个字符串
        str_temp = '{'+'lat:' + str(lat) + ','+'lng:' + str(lng) + ','+'count:' + str(count)+'}'+','+'\n'             
        str_temp_all=str_temp_all+str_temp #合并所有坐标值为单个字符串        
    htmlf=open('example_kong.html','r',encoding="utf-8")  #在example_kong.html文件基础之上用字符串的替换操作将绘制热点图所需数据放置到指定位置
    htmlcont=htmlf.read() #读入html文件
    #htmlcont为字符串
    htmlcont=htmlcont.replace('淑',str_region_lnglat) #用替换的方式得到中心点经纬度坐标 中心点坐标替换'淑'字
    htmlcont=htmlcont.replace('逑',str_temp_all)      #用替换的方式得到所有需要绘制的点的经纬度坐标 所有经纬度坐标替换'逑'字
    file_html=open('./html热力图/%s.html' %(region.split('/')[0]),'w',encoding='utf-8') #保存html文件
    file_html.write(str(htmlcont))
    file_html.close()        