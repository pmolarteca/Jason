#con este codigo descargo archivos fpt desde la consola (Globwave SAR)

tiempo=[]

for i in range(1,366):
	if i <10:
		tiempo.append('00'+str(i))
	elif i<100:
		tiempo.append('0'+str(i))
	else:
		 tiempo.append(i)

	


#for i in range (2002,2011):
for j in tiempo:
     print ('ftp://w1f612@eftp.ifremer.fr/waveuser/globwave/data/l2p/sar/gdr/envisat/2006/'+str(j))



