import re
str = '6104628192'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if(match){
	print("Country code:"+61+"nactional number":04628192+"Leading zero:False");
}else{
	print(match)
}

