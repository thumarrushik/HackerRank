A = str(input())
A = A.lower()

Answer = []

for a1 in A:
    if a1 not in Answer and a1 !=" ":
        Answer.append(a1)
        
if len(Answer) == 26:
    print("pangram")
else:
    print("not pangram")
