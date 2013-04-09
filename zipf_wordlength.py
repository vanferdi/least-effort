##hey there!

import random
import matplotlib.pyplot as py

iterations = 10000
n_things = 1000
n_letters = 3

things = [[0] for i in range(n_things)]

################################################################################
### PROGRAM LOOP

for iteration in range(iterations):

	for thing in range(len(things)):
		#print "-------------------------------------------- " +str(thing)
		mutation_type = random.randint(0,2)
		thing_length = len(things[thing])
		new_letter = random.randint(0,n_letters)
		
		if mutation_type == 0: # add letter
			#print "add letter " +str(new_letter)
			mutation_site = random.randint(0,thing_length)
			#print "mutation_site: " +str(mutation_site)
			things[thing].insert(mutation_site,new_letter)
		
		if mutation_type == 1: # change letter
			if len(things[thing]) > 0:
				#print "change letter to " +str(new_letter)
				mutation_site = random.randint(0,thing_length-1)
				#print "mutation_site: " +str(mutation_site)
				things[thing][mutation_site] = new_letter
			
		if mutation_type == 2: # delete letter
			if len(things[thing]) > 0:
				#print "delete letter"
				mutation_site = random.randint(0,thing_length-1)
				#print "mutation_site: " +str(mutation_site)
				things[thing].pop(mutation_site)
		
################################################################################
### ANALYSES

max_length = 0
for thing in things:
	if len(thing) > max_length:
		max_length = len(thing)
print "max_length = " +str(max_length)

counts = [0] * (max_length+1)
for thing in things:
	counts[len(thing)] += 1
print "counts per length = " +str(counts)



py.bar(counts,range(len(counts)))

py.xlabel('word length')
py.ylabel('frequency')

py.show()






