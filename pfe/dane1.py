import matplotlib.pyplot as plt

f= open("scatter.txt",'r')
#print("float(x.splot())");
#print ("float(y.splot())")
x=[]
for y in f.readline().split():
    x.append(y)
    print(x.len[0],x.len[1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
#plt.plot(x,y, linestyle="dashed",marker="0",color="green")
plt.scatter(x, y)
plt.show()
