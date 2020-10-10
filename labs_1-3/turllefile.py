import turtle as tur
tur.shape('turtle')

c=open('Шрифт для черепахи.txt', 'r')
lines = c.readlines()
res=[]
coords_for_number = []
for line in lines:
    line=line.strip()
    if len(line) == 1:
        current_number = int(line)
    else:
        line=line.append(coords_for_number)
print(line)

S = sajfhjfbwhjba
S.find()