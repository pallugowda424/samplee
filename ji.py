from matplotlib import pyplot as p
Q=["Q1","Q2","Q3","Q4"]
ssd=[200,300,400,600]
hdd=[234,257,145,456]
p.plot(Q,ssd,'^-',color='black')
p.plot(Q,hdd,'o-.r')
p.xlabel("Quarters in 2022"),p.ylabel("sales units")
p.title("sdd & hdd sales in stores")
p.legend(['sdd','hdd'])
p.show()