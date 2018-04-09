# -*- coding:utf-8 -*-

# account_file = "user.conf"
# f = open(account_file,"r+")
# raw_data = f.readlines()
# accounts = {}
# #把账户数据从文件里读书来，变成dict,这样后面就好查询了
# for line in raw_data:
#     line = line.strip()
#     if not  line.startswith("#"):
#         items = line.split(";")
#         accounts[items[0]] = items
# print(accounts["shanshan"][1])
#


# def test(*args):
#     print(args)
#     user_name = tuple(args)
#     print(user_name[0])
#     print(user_name[1])
#     print(user_name[2])
#
#
#
# test("username","1","password")

# accounts = {}
# f = open("user.conf", "r+")
# for i in f.readlines():
#     i = i.strip().split(";")
#     accounts[i[0]] = i
# print(accounts)
# print(accounts["shanshan"][0])
userName = "shanshan"
accounts = {}
f = open("user.conf", "r+")

for i in f.readlines():
    i = i.strip().split(";")
    accounts[i[0]] = i
    user_list = list(accounts[userName])

print(user_list)
for index,user in enumerate(user_list):
    print(enumerate(user_list))
    if index > 1 :
        print(index,user[1])