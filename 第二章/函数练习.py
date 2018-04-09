# -*- coding:utf-8 -*-

#user_file   用户配置文件
#user_name_input 用户输入的名字
#user_pass_input 用户输入的密码
#user_age_input  用户输入的年龄
#user_job_input  用户输入的职业


import os
user_file = "user.conf"

def user_add(user_name,user_pass,user_age,user_job):
    user_lock = "unlock"
    user_list = user_name + ";" + user_pass + ";" + user_age + ";" + user_job + ";" + user_lock

    ##写入文件，并将游标重置到文件头
    global user_file
    f = open(user_file, "a+")

    f.write("\n" + user_list)
    f.flush()
    f.seek(0)

    try:
        ##遍历文件，判断用户名是否存在，如果存在了就返回True
        for i in f.readlines():
            i = i.strip().split(";")
            if i[0] == user_name:
                return True
    finally:
        f.close()

def user_del(user_name):
    global user_file
    ##定义临时文件名
    new_f_tmp = os.path.basename(user_file) + ".tmp"

    ##打开两个文件
    f = open(user_file,"r")
    new_f = open(new_f_tmp,"w+")

    ##遍历源文件,将不需要删除的内容写入新文件
    for i in f.readlines():
        i = i.strip().split(";")
        if i[0] != user_name:
            new_f.write(i)

    f.close()
    new_f.close()

    ##重命名文件
    os.remove(user_file)
    os.rename(new_f_tmp,user_file)

def user_change(args):

    global user_file
    accounts = {}
    f = open(user_file,"r+")

    for i in f.readlines():
        i = i.strip().split(";")
        accounts[i[0]] = i
        print()
    # for i in f.readlines():
    #     i = i.strip().split(",")
    #     if username == i[0]:






user_name_input = input("请输入名字：")
user_pass_input = input("请输入密码：")
user_age_input = input("请输入年龄：")
user_job_input = input("请输入职业")

if user_add(user_name_input,user_pass_input,user_age_input,user_job_input):
    print("注册成功")
else:
    print("注册失败")
