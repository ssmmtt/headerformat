#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import pyperclip
import json


def convert():
    headers = text1.get('0.0', 'end')
    if ': ' in headers:
        print(headers)
        lines = headers.split('\n')
        print(lines)
        h = {}
        for line in lines:
            if line:
                l = line.split(': ')
                print(l)
                h[l[0]] = l[1]
        js = json.dumps(h, indent=4, separators=(',', ': '))
        print(js)
        text1.delete('0.0', 'end')
        text1.insert('end', js)
        pyperclip.copy(js)

        top = Toplevel(root)
        top.iconbitmap("./icon.ico")
        top.title('提示')
        scnWidth, scnHeight = top.maxsize()
        tmpcnf = '%dx%d+%d+%d' % (308, 101, (scnWidth - 308) / 2, (scnHeight - 101) / 2)
        top.geometry(tmpcnf)
        Message(top, text='已复制到剪切板！', padx=20, pady=50).pack()
        top.after(1500, top.destroy)


if __name__ == '__main__':
    root = Tk()
    root.title("Chrome请求头转换")

    # 设置主窗体大小
    winWidth = 600
    winHeight = 395
    # 获取屏幕分辨率
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # 计算主窗口在屏幕上的坐标
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)

    # 设置主窗口大小
    root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口宽高固定
    root.resizable(0, 0)
    # 设置窗口图标
    root.iconbitmap("./icon.ico")

    text1 = Text(root, width=100, height=28, undo=True)
    text1.pack(fill=BOTH)

    button1 = Button(root, text="转换并复制", bg="Goldenrod", command=convert)
    button1.pack(fill=BOTH)
    root.mainloop()
