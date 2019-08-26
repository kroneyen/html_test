# -*- coding: utf-8 -*-
### list
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 100, 100, 9, [1, 1, 1, 1]]
list_1 = [0 ,0 ,0 ,0 ]
list_2 = [ 'a','b','c']
list_1.extend(my_list)
#list_2.extend(list_1)
list_1.insert(6,list_2)
print(list_1)
list_1.remove([1, 1, 1, 1])

print(list_1 , len(list_1))
idx= list_1.index(['a', 'b', 'c'])
print(idx)
list_1.remove(['a','b','c'])
print(list_1.count(100))
print(list_1)
list_1.sort()
print('sort:',list_1)
list_1.reverse()
print(list_1)
"""
### set
"""
set_1 = set(["Apple", "Banana", "Coconut", "Banana", "Dragon Fruit"])
set_2 = set(['Apple', 'Lemon', 'Banana'])
print(set_1)
##差集(Difference)
print(set_1 - set_2)
print(set_2 - set_1)
##聯集(Union)
print(set_1 | set_2)
##交集(Intersection)
print(set_1 & set_2)
##對稱差集合(Symmetric Difference)
print(set_1 ^ set_2)
"""

### Dictionary  { key:values }
"""
fat1209 = {"my_name":'fat1209',"my_pwd":'05161209',"my_uid":12345}
## all key,values
print(fat1209)
## get key of values
print(fat1209['my_name'])
kkeys = list(fat1209.keys())
##get all keys
print(kkeys)
vvalues = list(fat1209.values())
## get all values
print(vvalues)

### import module
## python3.6  XXXX.py arv
#sys.argv[0]
#sys.argv[1]
"""
### 類別repr(str).rjust(N)
## \0	空字元 \n	換行 \r	歸位 \t tab
## \\	反斜線  \'	單引號 '   \"	雙引號 "

"""
for i in range(1, 10):
  str = ""
  for j in range(1, 10):
          str += repr(j).rjust(2) + " x" + repr(i).rjust(2) + " =" + repr(i*j).rjust(3) + "\t"
  print(str)
"""

### 寫入JSON檔
import json
import codecs  ## 中文用


#dict = {"台灣人口": 23000000, "台灣地理位置": "東南亞"}
dict = {
"dataset":{
    "train": {"type": "mnist", "data_set": "train", "layout_x": "tensor"},
    "test": {"type": "mnist", "data_set": "test", "layout_x": "tensor"}
},
"train":{
    "keep_model_in_mem":0,
    "random_state":0,
    "data_cache":{
        "cache_in_disk":{
            "default":1
        },
        "keep_in_mem":{
            "default":0
        },
        "cache_dir":"/mnt/raid/fengji/gcforest/mnist/fg-tree500-depth100-3folds/datas"
    }
},
"net":{
"outputs": ["pool1/7x7/ets", "pool1/7x7/rf", "pool1/10x10/ets", "pool1/10x10/rf", "pool1/13x13/ets", "pool1/13x13/rf"],
"layers":[
    {
        "type":"FGWinLayer",
        "name":"win1/7x7",
        "bottoms": ["X","y"],
        "tops":["win1/7x7/ets", "win1/7x7/rf"],
        "n_classes": 124,
        "estimators": [
            {"n_folds":3,"type":"ExtraTreesClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10},
            {"n_folds":3,"type":"RandomForestClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10}
        ],
        "stride_x": 2,
        "stride_y": 2,
        "win_x":7,
        "win_y":7
    },
    {
        "type":"FGWinLayer",
        "name":"win1/10x10",
        "bottoms": ["X","y"],
        "tops":["win1/10x10/ets", "win1/10x10/rf"],
        "n_classes": 10,
        "estimators": [
            {"n_folds":3,"type":"ExtraTreesClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10},
            {"n_folds":3,"type":"RandomForestClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10}
        ],
        "stride_x": 2,
        "stride_y": 2,
        "win_x":10,
        "win_y":10
    },
    {
        "type":"FGWinLayer",
        "name":"win1/13x13",
        "bottoms": ["X","y"],
        "tops":["win1/13x13/ets", "win1/13x13/rf"],
        "n_classes": 10,
        "estimators": [
            {"n_folds":3,"type":"ExtraTreesClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10},
            {"n_folds":3,"type":"RandomForestClassifier","n_estimators":500,"max_depth":100,"n_jobs":-1,"min_samples_leaf":10}
        ],
        "stride_x": 2,
        "stride_y": 2,
        "win_x":13,
        "win_y":13
    },
    {
        "type":"FGPoolLayer",
        "name":"pool1",
        "bottoms": ["win1/7x7/ets", "win1/7x7/rf", "win1/10x10/ets", "win1/10x10/rf", "win1/13x13/ets", "win1/13x13/rf"],
        "tops": ["pool1/7x7/ets", "pool1/7x7/rf", "pool1/10x10/ets", "pool1/10x10/rf", "pool1/13x13/ets", "pool1/13x13/rf"],
        "pool_method": "avg",
        "win_x":2,
        "win_y":2
    }
]

}
}

# 開檔改成使用codecs！ udf8  json 寫入

with codecs.open('my_writing_JSON', 'w', "utf8") as wf:  ### r+ read & write
    # ensure_ascii一定要設定成False，否則無法正確寫入中文
    i =1
    for i in range(1):
       str = json.dumps(dict, indent=2 ,ensure_ascii=False)  ##indent 縮排 Python JSON pretty print
       wf.write(str+'\n')
       i = i +1
wf.close()


with codecs.open('my_writing_JSON', 'r', encoding='utf8') as rf :

    json_data = json.loads(rf.read()) ## 讀怎個檔案資料 解碼轉成json
    #print('data:',json_data)
    #print(type(json_data))
    for lay_key1 in  json_data :  ## 取的layer 1 當key : dataset ,train :net
        dict_data1 =json_data[lay_key1] ### key1:values
        #print(lay_key1, ':',json.dumps(dict_data1, indent=2 ,ensure_ascii=False),'\n')
        if lay_key1 == 'net' :
            #print(lay_key1, ':', json.dumps(dict_data1, indent=2, ensure_ascii=False), '\n')
            doct_data_layers = dict_data1['layers']

            for layers_row in  doct_data_layers :
                print(layers_row.keys())
                #print(layers_row.values())
                #print('layers_name :' , layers_row['name'])


        


rf.close()

