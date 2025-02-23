

print("hello world")

inputs=[]

state=True;
while (state):
    print("Enter a input:")
    x=input()
    if(x=='x'):
        state=False
    else:
        inputs.append(x)
print(inputs)
