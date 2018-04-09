# -*- coding:utf-8 -*-

import sys
user_file = open('login.conf','r+')
user_name = input('请输入用户名')
login_count = 0
exit_flag = True
while exit_flag:
    for exist_user in user_file.readlines():
        exist_user = exist_user.strip().split(':')
        if user_name == exist_user[0]:
            for i in range(1,4):
                exist_pass = input('请输入密码')
                if exist_pass == exist_user[1]:
                    if exist_user[2] == 'lock':
                        print('用户被锁定')
                        exit()
                    else:
                        print("欢迎登陆")
                        exit()
                elif i == 3:
                    print('连续输入错误3次，退出登陆')
                    exit()
                else:
                    print('密码错误请重新输入')
    print('用户名不存在')
    exit_flag = False