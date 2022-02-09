import time, sys, tkinter

"""
Map
"""

#孔雀街 = {"去御街":road1(userpos), "去闫氏百货":supermarket(userpos), "“大侠请捐款”盒":get_road2_money(usermoney)}
#闫氏百货 = {"去御街":road1(userpos), "去孔雀街":road2(userpos), "王氏膳店":vegetable_store(userlevel, usermoney, userbag), "“侠客红尘”武器店":weapon_store(userlevel, usermoney, userbag), "路边的老爷爷":poor_store(userbag)}
#御街 = {"去孔雀街":road2(userpos), "去闫氏百货":supermarket(userpos), "回帮派":home(userpos, usermoney, userlevel, userbag, userhealthy), "去琢袅林":go_to_south_area(userpos), "去太白山":go_to_north_area(userpos), "去道馆":go_to_daoguan(userpos)}
#道馆 = {"练功":fight(userpos, userbag, usermoney), "学习":learn(userlevel, usermoney), "回收":bagback(userbag)}
#琢袅林 = {"打猎":fight(userpos, userbag, usermoney), "伐木":getwood(userbag), "回御街":road1(userpos)}
#太白山 = {"听讲":learn(userlevel, usermoney, userexp), "茶馆":drink_tea(usermoney, userhealthy), "回御街":road1(userpos)}
"""
Map
"""

def save(userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos):
    fi = open(r"savedata.txt", mode = "r+", encoding = 'utf-8')
    fi.write([userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos])
    fi.close()
    printf("已存档！")

def login(password, username):
    ps = 0
    printf("尊敬的"+username",请输入密码：")
    ps = input()
    for i in range(3):
        if (ps == password):
            printf("欢迎您！")
            return True
        else:
            printf("(⊙o⊙)？不对哦,尊敬的"+username",请再次输入密码：")
            ps = input()
    return False

def create(userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos):
    userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos = 1, 0, 0, input(), input(), 100, ["knife"], home
    printf("您的密码是：" + password);
    save(userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos)
    return userlevel, usermoney, userexp, username, password, userhealthy, userbag, userpos

def printf(word):
    for i in word:
        print(i, end = "", flush = True)
        time.sleep(0.15)
    input(" (回车以继续...)")
def road1(userpos):
    printf("你从 " + userpos + " 动身前往 御街 ...")
    return road1
