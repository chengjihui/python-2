#-*-coding:utf-8-*-
#import pymongo
'''
client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']
'''
path = 'walden.txt'
with open(path,'r') as f:
	lines = f.readline()
	for index,line in enumerate(lines):
		data = {
		'index':index,
		'line' :line,
		'words':len(line.split())
		}
		print data
        #sheet_tab.insert_one(data)

#$lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
#for item in sheet_tab.find({'words':{'$lt':5}}):
 #   print(item)