from typing import List

print("Hello World, From Kushal")

x=1;
y=1;

def add(a,b):
	return a+b;

def twoSum(numbers: List[int], target: int) -> List[int]:
	table={ } 
	for i, num in enumerate(numbers):
		diff = target - num
		if diff in table:
			return [table[diff],i]
		else: 
			table[num]=i
	return [0]

def sayhello():
    print("Hello World")

print("Hopefully this works well")
print("Currently using ghost tty ") 
print(twoSum([1,2,3,4],5))
print(sayhello())
