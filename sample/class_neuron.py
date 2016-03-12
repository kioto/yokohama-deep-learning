class Neuron:
    def __init__(self):
        self.b = 0
        self.W = []
        self.f = None

    def func(self, xx):
        return self.f(self.W, self.b, xx)

def bar(ww, b, xx):
    '''適当に計算してベクトルを返す
    '''
    res = []
    for i in range(len(xx)):
        res.append(xx[i] * ww[i] + b)
    return res

n = Neuron()
n.b = 10
n.W = [2, 4, 6, 5]
n.f = bar

x = [1, 2, 3, 4]
print(n.func(x))

# 課題
# これをfor文を使わずにnumpyで書く

