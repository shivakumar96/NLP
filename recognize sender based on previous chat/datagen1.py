file1 = open("chat.txt",'r')
file_pers2 = open('pers2','a')
file_pers1 = open('pers1','a')

alltxt = file1.readlines()

for line in  alltxt :
       if "pers1" in line :
             txt = line.split('-')
             per1 = txt[1][txt[1].index(':')+1:]
             if "<Media omitted>" not in per1 :
                         file_pers1.write(per1)
       elif "pers2" in line :
             txt = line.split('-')
             per2 = txt[1][txt[1].index(':')+1:]
             if "<Media omitted>" not in per2 :
                         file_pers2.write(per2)

file1.close()
file_pers1.close()
file_pers2.close()
