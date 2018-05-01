map = {};
map["Business"]= ["business"]
map["SciTech"] = ["science", "technology computing"]
map["Sports"] = ["sports"]
map["World"] = ["law govt poltics"]

map["Society and Culture"] = ["society"]
map["Science and Mathematics"] = ["science"]
map["Health"] = "health fitness"
map["Education and Reference"] = ["education"]
map["Computers and Internet"] = ["technology and computing"]
map["Business and Finance"] = ["business"]
map["Entertainment and Music"] = ["arts entertainment"]
map["Family and Relationships"] = ["family parenting"]
map["Politics and Government"] = ["law govt politics"]


file_in = open("News Classification DataSet.tsv", "r");
finalOut = [];
for line in file_in:
	separate = line.split("\t");
	
	
	label = map[separate[1].rstrip()]
	
	if(type(label) =='str'):
		finalOut.append(separate[0] + '\t' + label)
	else:
		finalOut.append(separate[0] + '\t' + ','.join(label))
	
file_in.close()
file_in = open("Yahoo QA Topic Classification.tsv", "r");

for line in file_in:
	separate = line.split("\t");
	
	
	label = map[separate[1].rstrip()]
	
	if(type(label) =='str'):
		finalOut.append(separate[0] + '\t' + label)
	else:
		finalOut.append(separate[0] + '\t' + ','.join(label))
	


writeout = '\n'.join(finalOut);
fileout = open("labeledText.tsv" , "w");
fileout.write("input\tresult\n")
fileout.write(writeout);

'''
	if separate[1] in map.keys():
		print(map[separate[1]]);
	else:
		print("wtf?")
		print(separate[1])

'''



'''
business == business
sci-tech == science * tech & computing
sports == sports
world == law, gov't & poltics
society and culture == society

science and mathematics == science
health == healthand fitness
Educatoin and Reference = education

computers and internet == technology and computing
business and finance = business

entertainmenta nd music = arts and entertainment
family and relationships = family and parenting
politics and govt = law, goc't & politics
'''
