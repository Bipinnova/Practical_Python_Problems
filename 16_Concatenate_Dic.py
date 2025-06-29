# Write a Python script to concatenate following dictionaries to create a new one. 
# Sample Dictionary :  
# dic1={1:10, 2:20}  
# dic2={3:30, 4:40}  
# dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Time and space complexity: O(n)

dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60} 
result = {}
for i in (dic1, dic2, dic3):
    result.update(i)
print(result)