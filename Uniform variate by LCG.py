def uvar(x):
	m,a,c=1771875,2416,374441
	x=(a*x+c)%m
	r=x/m
	return r,x

print(uvar(263519)[0])
def uniform_numbers(x,size):
   L=[]
   for i in range(size):
   	r,x=uvar(x)
   	L.append(r)
   return L
   
print(uniform_numbers(263519,5))
   