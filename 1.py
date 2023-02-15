import tkinter as tk

fon1=("宋", "16")

#===========2023-02-06,10点17  今天目标读懂这份888.py 代码.


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):

        '''redraw line numbers'''
        self.delete("all")
        # ====================self.textwidget.index("@0,0") @0,0表示最接近左上角的行信息.
        i = self.textwidget.index("@0,0")  # 找到0行0列的信息. ref: 参考文档:    https://tkdocs.com/shipman/text-index.html
        hang, lie = i.split('.')
        while True:
            dline = self.textwidget.dlineinfo(i)
            hang, lie = i.split('.')  # 计算上面i行的信息.    self.textwidget.get(i)
            debug222 = self.textwidget.get(i)  # 这里面显示滚动之后的左上角第一个字.#这时候我们读入的是1.4
            if dline is None: break  # Return tuple (x,y,width,height,baseline) giving the bounding box        and baseline position of the visible part of the line containing        the character at INDEX.
            if lie == '0':  # ===首列才画行号.
                y = dline[1]
                linenum = hang  # 行信息
                self.create_text(1, y, anchor="nw", text="{0:>2}".format(linenum), font=fon1)  # 创建行号. 2是x索引.
            # i = self.textwidget.index("%s+1line" % i) #然后计算下一行.
            i = self.textwidget.index(str(int(hang) + 1) + '.' + '0')  # 然后计算下一行.







class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args): #发送自定义信号change
        # let the actual widget perform the requested action
        result=1
        try:
            cmd = (self._orig,) + args
            result = self.tk.call(cmd)

            # generate an event if something was added or deleted,
            # or the cursor position changed
            if (args[0] in ("insert", "replace", "delete") or
                args[0:3] == ("mark", "set", "insert") or
                args[0:2] == ("xview", "moveto") or
                args[0:2] == ("xview", "scroll") or
                args[0:2] == ("yview", "moveto") or
                args[0:2] == ("yview", "scroll")
            ):
                self.event_generate("<<Change>>", when="tail")#触发change信号.
        except:
            pass
        # return what the actual widget returned
        return result

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self,font=fon1)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)#竖直方向的滑动杆.
        self.text.configure(yscrollcommand=self.vsb.set)

        self.linenumbers = TextLineNumbers(self, width=30)#创建行号工具
        self.linenumbers.attach(self.text) # 绑定行号工具到text空间.

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)#绑定修改到重新绘制linenumber
        self.text.bind("<Configure>", self._on_change)

        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "onefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\ntwofivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\nthree\n")
        self.text.insert("end", "fivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefivefive\n")

    def _on_change(self, event):
        self.linenumbers.redraw()
# ... and, of course, add this at the end of the file to bootstrap it:

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
