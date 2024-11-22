#a.
a = [x**2 for x in range(1, 11)]    

#b.
nums = [1, 2, 3, 4, 5, 6, 7, 8] 
b = [num for num in nums if num % 2 == 0] 

#c. 
words = ['apple', 'banana', 'cherry'] 
c = [word.upper() for word in words]     

#d. 
sentence = 'The quick brown fox'  
d = [len(word) for word in sentence.split()]  

#e. 
sentence = 'Hello World from Python'  
e = [word[0] for word in sentence.split()] 

#f.
f = [[x for x in range(2)] for y in range(3)]  

#g.
g = [[2*x for x in range(1, 4)] for y in range(3)] 