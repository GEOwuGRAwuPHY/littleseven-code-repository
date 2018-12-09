#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import Tkinter

if __name__ == '__main__':
        root = Tkinter.Tk()#root是一个根图形界面对象， 所有的图形界面都在在这个根对象上建立，相当于画画的画板
        cv = Tkinter.Canvas(root,bg = 'white')#canvas是画布的意思，图像都是在画布上画的，相当于画画的纸，bg是背景颜色
        cv.pack()#将cancas挂到root上去
        cv.create_line(10,10,110,110)#画板上画一个长方形
        root.mainloop()#将根对象(画板展示出来)
