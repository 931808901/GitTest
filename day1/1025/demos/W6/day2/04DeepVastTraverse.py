'''
深度遍历和广度遍历
'''

zuzong = {"name": "1", "son": [
    {"name": "2-1", "son": [
        {"name": "2-1-1", "son": [
            {"name": "2-1-1-1"},
            {"name": "2-1-1-2"},
            {"name": "2-1-1-3"},
        ]},
        {"name": "2-1-2"},
        {"name": "2-1-3"},
    ]},
    {"name": "2-2", "son": [
        {"name": "2-2-1"},
        {"name": "2-2-2"},
        {"name": "2-2-3"},
    ]},
    {"name": "2-3", "son": [
        {"name": "2-3-1"},
        {"name": "2-3-2"},
        {"name": "2-3-3"},
    ]},
]}


# 深度遍历家族树（递归）
def showFamilyTreeDeep(obj):
    # 打自己的名字
    print("\t" * len(obj["name"]), obj["name"])

    # 递归终止条件
    try:
        obj["son"]
    except KeyError:
        return

    # 打儿子的名字
    for son in obj["son"]:
        # 对每个儿子递归打印家族树
        showFamilyTreeDeep(son)


# 广度遍历家族树（队列：从头部取，向尾部放）
def showFamilyTreeVast():

    # 向宗祠里添加第一代先祖
    persons = []
    persons.append(zuzong)

    # 不停地从宗祠里揪人爬邮箱
    # 揪到无人为止
    while len(persons) > 0:

        # 揪出第一个人，爬邮箱，宗祠里再无该人
        p = persons.pop(0)
        print("\t" * len(p["name"]), p["name"])

        # 如果此人无后（p["son"]报KeyError），就继续揪下一个人
        try:
            # 英勇地向宗祠添加下一代香火
            for son in p["son"]:
                persons.append(son)
        except KeyError:
            pass


showFamilyTreeDeep(zuzong)
showFamilyTreeVast()
