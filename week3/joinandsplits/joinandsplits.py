#csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
#friends_list = ['Exercise: fill me with names']

#step1=csv.split(",")
#print(step1)
#friends_list=[step1[0:4]]
#step2=step1[4].split(":")
#print(step2)
#step3=step2[1].split(";")
#print(step3)

#friends_list=friends_list.concatenate([step2[0]],step3)
#friends_list.push(step2[0])
#friends_list.push(step3[0])
#friends_list.push(step3[1])
#print(friends_list)


csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = []

step1 = csv.split(",")
step2 = step1[4].split(":")
step3 = step2[1].split(";")

friends_list= [*step1[0:4], step2[0],*step3]

print(friends_list)