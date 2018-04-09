# -*- coding:utf-8 -*-
map = {
    "华南": {
        "广东": ["广州市", "佛山市", "深圳市", "东莞市"],
        "广西": ["南宁市", "柳州市", "桂林市", "北海市"],
        "海南": ["海口市", "三亚市", "三沙市", "儋州市"]
    },
    "华东": {
        "上海": ["黄浦区", "卢湾区", "徐汇区", "长宁区", "普陀区"],
        "安徽": ["合肥市", "芜湖市", "淮南市", "马鞍山市"],
        "江苏": ["南京市", "无锡市", "徐州市", "常州市", "苏州市"]
    },
    "华北": {
        "北京": ["东城区", "西城区", "朝阳区", "丰台区", "石景山区", "海淀区"],
        "山西": ["太原市", "大同市", "阳泉市", "长治市"],
        "河北": ["石家庄市", "唐山市", "秦皇岛市", "邢台市"]
    },
    "华中": {
        "湖北": ["武汉市", "黄石市", "十堰市", "十堰市"],
        "河南": ["郑州市", "开封市", "洛阳市", "平顶山市"],
        "湖南": ["长沙市", "株洲市", "衡阳市", "邵阳市"]
    },
    "西南": {
        "重庆": ["万州区", "涪陵区", "渝中区", "大渡口区"],
        "四川": ["成都市", "自贡市", "攀枝花市", "德阳市"],
        "贵州": ["贵阳市", "六盘水市", "遵义市", "安顺市"],
    },
    "特别行政区": {
        "香港": ["屯门", "弯仔", "北角", "西贡"],
        "澳门": ["花地玛堂区", "圣安多尼堂区", "大堂区", "望德堂区"],
    },
}
exit_flag = False
large_key = map.keys()
while not exit_flag:
    print('***请选择大区***')
    for large_name in large_key:
        print(large_name)
    large_input = input('请输入大区名字，输入Q退出>>').strip()
    if large_input == 'q' or large_input == 'Q':
        break
    elif large_input not in large_key:
        print('您输入的大区不存在')
    else:
        while not exit_flag:
            print('***请选择城市***')
            for city_name in map[large_input].keys():
                print(city_name)
            prov_input = input('请输入省份名字,输入b返回，输入q退出>>').strip()
            if prov_input == 'b' or prov_input == 'B':
                break
            elif prov_input == 'q' or prov_input == 'Q':
                exit_flag = True
            elif prov_input not in map[large_input].keys():
                print('您输入的省份不存在')
            else:
                while not exit_flag:
                    print('请选择区域')
                    for zone_name in map[large_input][prov_input]:
                        print(zone_name)
                    zone_input = input('请输入城市名字,输入b返回，输入q退出').strip()
                    if zone_input == 'b' or zone_input == 'B':
                        break
                    elif zone_input == 'q' or zone_input == 'Q':
                        exit_flag = True
                    elif zone_input not in map[large_input][prov_input]:
                        print('您输入的城市不存在')
                    else:
                        city_input = input('您当前所在地为%s,输入b返回，输入q退出'%(zone_input)).strip()
                        if city_input == 'b' or city_input == 'B':
                            break
                        elif city_input == 'q' or city_input == 'Q':
                            exit_flag = True
