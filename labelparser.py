map = {}
map["Business"]= ["business"]
map["SciTech"] = ["science", "technology computing"]
map["Sports"] = ["sports"]
map["World"] = ["law govt poltics"]

map["Society and Culture"] = ["society"]
map["Science and Mathematics"] = ["science"]
map["Health"] = ["health fitness"]
map["Education and Reference"] = ["education"]
map["Computers and Internet"] = ["technology computing"]
map["Business and Finance"] = ["business"]
map["Entertainment and Music"] = ["arts entertainment"]
map["Family and Relationships"] = ["family parenting"]
map["Politics and Government"] = ["law govt politics"]


input1 = "News Classification DataSet.tsv"
file_in = open(input1, "r")
finalOut = []
firstline = file_in.readline()
for line in file_in:
	separate = line.split("\t")
	
	
	label = map[separate[1].rstrip()]
	
	if(type(label) =='str'):
		finalOut.append(separate[0] + '\t' + label)
	else:
		finalOut.append(separate[0] + '\t' + ','.join(label))
	
file_in.close()
fileout = open("news.tsv" , "w")
writeout = '\n'.join(finalOut)
fileout.write(firstline)
fileout.write(writeout)
fileout.close()

finalOut = []
input2 = "Yahoo QA Topic Classification.tsv"
file_in = open(input2, "r")

firstline = file_in.readline()

for line in file_in:
	separate = line.split("\t")
	
	
	label = map[separate[1].rstrip()]
	
	if(type(label) =='str'):
		finalOut.append(separate[0] + '\t' + label)
	else:
		finalOut.append(separate[0] + '\t' + ','.join(label))
	
file_in.close()

writeout = '\n'.join(finalOut)
fileout = open("yahoo.tsv" , "w")
fileout.write(firstline)
fileout.write(writeout)
fileout.close()

