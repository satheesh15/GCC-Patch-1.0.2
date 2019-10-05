# modify this function, and create other functions below as you wish
def question03(scores, alice):
    # modify and then return the variable below
    sc = set(scores)
    scores = list(sc)
    scores.sort()

    ranks = []
    for i in alice:
	    ir = 1
	    for j in scores:
	    	if i<j:
	    		ir +=1
	    ranks.append(ir)

    dic = {}
    k = 0
    v = 0
    for i in ranks:
    	if i in dic.keys():
	    	j = dic[i]+1
		    dic[i] = j
	    	if j>v:
		    	k = i
			    v = j
	    	elif j==v:
		    	if i>k:
			    	k = i
    	else:
	    	j = 1
		    dic[i] = j
    		if j>v:
	    		k = i
		    	v = j
		    elif j==v:
			    if i>k:
				    k = i
    return k
