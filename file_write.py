# -*- coding: cp936 -*-
content='''woshiyiduankaai
dewenzi
nizhidaoma
'''
#w读写（如果文件不存在直接创建文件）;r只读（默认）;a:追加(不存在就新建)
file1=open('demo.txt','a')

file1.write(content)

file1.close()
