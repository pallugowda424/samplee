from matplotlib import pyplot as p
pro_na=["intel","AMD","snapdragon","tensor"]
use=[200,450,312,67]
p.bar(pro_na,use,color='black',width=0.2)
p.xlabel("processors"),p.ylabel("no of users")
p.title("processor user in a community")
p.show()