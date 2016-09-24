# -*- coding:utf-8 -*-
import re
# 数据文件
filename = 'products.csv'
# 读取文件
original = open(filename,'r')
# 替换双引号
temp = original.read().replace('"','')
original.close()

# 写入文件
datas=temp.split('\n')
# 正则匹配
rep = re.compile(r'(.*)/.*')
for i in range(0,len(datas)-1):
	temp1 = datas[i].split(',')
	for j in range(0,len(temp1)):
		try:
			temp1[j]=rep.match(temp1[j]).group(1)
		# 出现没有/的商品 剔除掉
		except:
			pass
	# 商品去重
	temp1=list(set(temp1))
	# 如果只有一件商品设空
	if len(temp1)==1:
		datas[i]=''
	else:
		datas[i]=','.join(temp1)
# 去重
while '' in datas:
	datas.remove('')

# 写入新文件
temp='\n'.join(datas)
newfilename = 'newproducts.csv'
original = open(newfilename,'w')
original.write(temp)
original.close()
