#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 19:19
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :study_reflect.py
#@Software  :PyCharm Community Edition

"""
反射:类的反射可以动态的查看，增加，删除，更改类或者实例的属性。
比如：
    getattr(Context,'normal_user') #获取类属性的值
    setattr(Context,'admin_user','abc') #添加属性
    hasattr(Context,'admin_user')   #判断是否有这个属性
    delattr(Context,'admin_user')   #删除这个属性
"""

class People:
    number_eye = 2

    def __init__(self,name,age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = People('gaoxu',18)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)

    #添加属性
    print(hasattr(People,"number_eye")) #如果有返回True，没有返回False
    print(hasattr(People,"number_leg"))

    setattr(People,"number_leg",2) #给类增加一个属性
    print(hasattr(People,"number_leg")) #判断类属性是否存在
    print(People.number_leg)

    setattr(p,"dance",True)
    print(p.dance) #实例名点名称

    getattr(People,"number_leg") #获取类属性
    getattr(p,"dance") #获取实例属性.

    delattr(p,"dance")
    # getattr(p,"dance")