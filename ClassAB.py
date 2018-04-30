# class derive
class A(object):
	def show(self):
		print 'base show'
class B(A):
	def show(self):
		print 'derived show'
obj = B()
# Aobj = A()
obj.show()
obj.__class__ = A
obj.__class__ = B
obj.show()


class C(object):
	def __init__(self,a,b):
		self.__a = a
		self.__b = b
	def myprint(self):
		print 'a = ', self.__a,'b=', self.__b
	def __call__(self,num):
		self.__num = num
		print 'number', self.__num
al = C(10,20)
al.myprint()
al(80)
#3
class D(object):
	def fn(self):
		print 'D fn'
	def __init__(self):
		print 'D INIT'
class E(D):
	def fn(self):
		print 'E fn'
	def __new__(cls,a):
		print 'New', a
		if a >10:
			return super (D,cls).__new__(cls)
		return D()
	def __init__(self,a):
		print "INTI",a
d1= E(5)
d1.fn()
d2= E(20)
d2.fn()
#4
class F(object):
	def fn(self):
		print 'F fn', self.af
	def __init__(self,a):
		self.af = a
		print 'this is ', a
f1 = F(10)
f1.fn()

dic = {'x': x*2 for x in (2,4,6)}
print 'dic["x"]',dic[ 'x' ]
#5
num = 9
def f1():
	global num
	num = 20
def f2():
	print num
f2()
f1()
f2()
#6
a_swap = 9
b_swap = 10
(a_swap,b_swap) = (b_swap,a_swap)
print 'a_swap', a_swap,'b_swap',b_swap

class G(object):
	def __init__(self,a,b):
		self._a = a
		self._b = b
		print "init"
	def default(self,*args):
		print "default" +str(args[0])
	def __getattr__(self,name):
		print 'other fn', name
		return self.default

G1 = G(10,20)
G1.fn(20)
G1.fn2('hello')
G1.fn3(12)

