# Builds "Data/s/-2000 attack speed table.erm" from "src/attack speed values.md".
# Run from the "Forge & Fury" folder: python src/make_attack_speed_table.py
import re
t=open('src/attack speed values.md',encoding='utf-8').read()
vals=sorted((int(i),n.strip(),int(v)) for i,n,v in re.findall(r'^\| (\d+) \| ([^|]+) \|[^\n]*?\*\*(\d+)\*\*',t,re.M))
out=['ZVSE2','','** ATTACK SPEED TABLE - generated from "src/attack speed values.md" by "src/make_attack_speed_table.py".',
     '** Do not edit by hand: change the .md file and run the script again.','',
     '!?FU(AS_SetUpTable);']
for i,n,v in vals: out.append('!!VRi^as_base_%d^:S%d;  [%s]'%(i,v,n))
out+=['','!?FU(OnStartOrLoad);','!!FU(AS_SetUpTable):P;','']
open('Data/s/-2000 attack speed table.erm','w',encoding='latin1',newline='\r\n').write('\n'.join(out))
print(len(vals),'creatures')
