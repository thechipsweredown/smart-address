class A:
    def __init__(self,a):
        self._a = a
    def set_a(self,a):
        self._a = a
def change(b):
    b.set_a(10)

b = A(1)
g = { 1 : b}
k = g[1]
change(k)
print(g[1]._a)