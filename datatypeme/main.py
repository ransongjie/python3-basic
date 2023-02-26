
if __name__=="__main__":
    #不可变数据类型
    ##Number（数字）
    ###int（整数）
    aint=10
    print(aint)
    ###float（浮点数）
    afloat=10.1
    print(afloat)
    ###bool（布尔）
    abool=True
    print(abool)
    ###complex（复数）
    acomplex=complex(10,1)
    print(acomplex)

    ##String（字符串）
    astr="xcrj"
    print(astr)

    ##Tuple（元组），元组中的元素不能修改，类型可以不同
    atuple=(10,10.1,complex(10,1),True,"aa")
    print(atuple)

    #可变数据类型
    ##List（列表）：有序可重复
    alist=[10,10.1,complex(10,1),True,"aa"]
    print(alist)
    #增加
    alist.append("bb")
    print(alist)
    #删除
    alist.pop()#弹出末尾元素
    print(alist)
    #修改
    alist[-1]="bb"#根据索引修改
    print(alist)
    #查询
    print(alist[-1])#根据索引查询
    #遍历
    for a in alist:
        print(a)

    ##Set（集合）：无序不可重复
    aset={10,10.1,complex(10,1),True,"aa"}
    print(aset)
    #增加
    aset.add("bb")
    print(aset)
    #删除
    aset.remove("bb")
    print(aset)
    #修改
    #查询
    #遍历
    for a in aset:
        print(a)

    ##Dictionary（字典）：key-value
    adict={"xcrj1":1,"xcrj2":2,"xcrj3":3}
    print(adict)
    #增加
    adict["xcrj4"]=4
    print(adict)
    #删除
    adict.pop("xcrj4")
    print(adict)
    #修改
    adict["xcrj3"]=4
    print(adict)
    #查询
    print(adict["xcrj1"])
    #遍历
    for (k,v) in adict.items():
        print(k,": ",v)
    
    for k in adict.keys():
        print(k,": ",adict[k])

    for v in adict.values():
        print(v)