# -*- coding:utf-8 -*-
"""
goods_list  商品列表
shopping_list  购物车列表
user_name    用户名称
user_menory   用户钱数
mony_count    所选商品总价
"""

goods_list = [['iphone',500],['华为',300],['小米',250],['荣耀',310],['诺基亚',260],['vivo',350],['小辣椒',180]]
shopping_list = []
user_name = input("请输入您的名字：")
user_menory = int( input("您有多少钱？") )
mony_count = int(0)
exit_flag = True
while exit_flag:
    try:
        if user_menory > mony_count:
            print("Dear %s. 您总共选择了%s元的商品"%(user_name,mony_count))
            print("**************商品列表****************")
            for index,i in enumerate(goods_list):
                print("%s. %s  %s"%(index,i[0],i[1]))
            choine = input("请输入你选择的商品编号,输入q结束购物：")
            if choine.isdigit():
                choine = int(choine)
                """如果商品价格大于余额就充值，充值后继续购物"""
                if goods_list[choine][1] > user_menory:
                    user_rech = int(input("您的余额不足,请输入你充值的钱数："))
                    user_menory += user_rech
                else:
                    shopping_list.append(goods_list[choine])
                    mony_count += goods_list[choine][1]
                    user_menory = user_menory - mony_count
            """"
            输入Q退出，退出的时候显示用户余额、所选商品的总价和商品列表
            """
            elif choine == "q" or choine == "Q":
                print("Dear %s. 您总共选择了%s元的商品" % (user_name, mony_count))
                print("您的余额还有%s元"%(user_menory))
                print("**************购物车列表****************")
                for index, k in enumerate(shopping_list):
                    print("%s. %s  %s" % (index, k[0], k[1]))
                exit_flag = False

    except:
        print("您输入的有误，请重新输入")