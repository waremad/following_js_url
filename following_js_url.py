#
from os import path


def readjs(self):#.jsファイルを読み込む
    with open(self+".js") as f:
        return f.read()

def deln(self):#\nを消す
    self = self.split("\n")
    self = "".join(self)
    return self

def picurl(self):#httpが入るのを抽出
    self = self.split("\"")
    out = []
    for i in self:
        if "http" == i[:4]:
            out.append(i)
    return out

path = input("???.js:")
txt = readjs(path)
ls = picurl(txt)
path_w = 'output.txt'
with open(path_w, mode='w') as f:
        f.write("")

for i in ls:
    with open(path_w, mode='a') as f:
        f.write(i+"\n")