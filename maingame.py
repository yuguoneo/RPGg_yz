from functionn.py import *

"""
Map
"""

孔雀街 = {"去御街":road1(userpos), "去闫氏百货":supermarket(userpos), "“大侠请捐款”盒":get_road2_money(usermoney)}
闫氏百货 = {"去御街":road1(userpos), "去孔雀街":road2(userpos), "王氏膳店":vegetable_store(userlevel, usermoney, userbag), "“侠客红尘”武器店":weapon_store(userlevel, usermoney, userbag), "路边的老爷爷":poor_store(userbag)}
御街 = {"去孔雀街":road2(userpos), "去闫氏百货":supermarket(userpos), "回帮派":home(userpos, usermoney, userlevel, userbag, userhealthy), "去琢袅林":go_to_south_area(userpos), "去太白山":go_to_north_area(userpos), "去道馆":go_to_daoguan(userpos)}
道馆 = {"练功":fight(userpos, userbag, usermoney), "学习":learn(userlevel, usermoney), "回收":bagback(userbag)}
琢袅林 = {"打猎":fight(userpos, userbag, usermoney), "伐木":getwood(userbag), "回御街":road1(userpos)}
太白山 = {"听讲":learn(userlevel, usermoney), "茶馆":drink_tea(usermoney, userhealthy), "回御街":road1(userpos)}
"""
Map
"""
