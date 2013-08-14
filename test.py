import copy

input =[ [ "Shashank","Amit","Ankit", "Harish" ], [ "works","codes","enjoys"], ["at rigvee", "in office"],['and is'], ['smart','happy'] ] 

answer =[''];
for arr in  input:
	temp_answer = [];	
	for word in arr:
		temp_answer.extend( [ answer[i] + " " + word for i in range(len(answer))] )		
	answer = copy.copy(temp_answer);
	
for (i,sentence) in enumerate(answer):
	print "%d. %s" % (i+1,sentence)
