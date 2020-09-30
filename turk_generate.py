import csv
import os
import json


#changable parameters
batch_size = 20
all_size = 3000
domain_num = 3
domain=['Finance','Politics','Health']
start_idx = [0, 0, 0]
time =['2019.6.16']
file_to_1 = '../turk_data/turk_json.txt'
file_to_2 = '../turk_data/turk.csv'
file_to_3 = '../turk_data/log file.csv'
#########################################

max_idx=[]
file=[]
field_num = []
all_size = all_size/batch_size*batch_size   #??
print("all samples: %d" % all_size)

for i in range(domain_num):
    a='../all_v3/a'+domain[i]+'_sentences.txt'
    file.append(a)
    with open(file[i], 'r',encoding='utf-8') as f_max:
        lines = f_max.readlines()
        max_idx.append(len(lines))
    if i != domain_num-1:
        field_num.append(int(all_size//domain_num))
    else:
        field_num.append(int(all_size-(all_size//domain_num)*(domain_num-1)))
    if field_num[i] > max_idx[i]:
        raise ValueError('error! exceed the ori file len!')
    if start_idx[i] + field_num[i] > max_idx[i]:
        raise ValueError('error! jump exceed the ori file len!')
    print("domain: %s  range: (%d, %d)" % (domain[i],start_idx[i] + 1, start_idx[i] + field_num[i]))
print("for each field: ", field_num)
print("strat_idx:", start_idx)
print("max_idx:", max_idx)

if os.path.exists(file_to_1):
    os.remove(file_to_1)
if os.path.exists(file_to_2):
    os.remove(file_to_2)

f_to_1 = open(file_to_1, 'a',newline='',encoding='utf-8')
f_to_2 = open(file_to_2, 'a',newline='',encoding='utf-8')

s = []                          # csv file title
for i in range(batch_size):
    s.append("paragraph" + str(i + 1))
writer = csv.writer(f_to_2)
writer.writerow(s)

ss = []
start=[]
end=[]
for i in range(domain_num):
    with open(file[i], 'r') as f:
        c = 0
        if start_idx[i] != 0:
            print("jump %d samples in file %s" % (start_idx[i], file[i]))
            for jump in range(start_idx[i]):
                line = f.readline()
                if line is None:
                    raise ValueError('end of file!(jump)')

        for j in range(field_num[i]):
            line = f.readline()
            if line is None:
                raise ValueError('end of file!')

            f_to_1.write(line)     # output file 1 json

            js = json.loads(line)  # output file 2 csv
            cf = js["sentence"]

            if j== 0:
                start.append(js["sentence ID"])
            if j==field_num[i]-1:
                end.append(js["sentence ID"])

            ss.append(cf.strip().replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' '))
            if len(ss) == batch_size:
                writer.writerow(ss)
                ss = []
            c += 1

        if c != field_num[i]:
            raise ValueError('error! wrong sample number!')
        else:
            print('process file: %s, sample_num: %d' % (file[i], c))

f_to_1.close()
f_to_2.close()

with open(file_to_1, 'r',encoding='utf-8') as f1_check:
    lines = f1_check.readlines()
    print("check total lines of ||%s||: %d" % (file_to_1, len(lines)))
    if len(lines) != all_size:
        raise ValueError("--error--")
with open(file_to_2, 'r',encoding='utf-8') as f2_check:
    lines = f2_check.readlines()
    print("check total lines of ||%s||: %d" % (file_to_2, len(lines)))
    if len(lines) != all_size/batch_size+1:
        raise ValueError("--error--")

lst=[time]
with open(file_to_3,'a',newline='',encoding='utf-8') as f:
    # heading=['time','domain','Index','ID','number']
    for i in range (domain_num):
        info=['',domain[i],str(start_idx[i] + 1)+'-'+str(start_idx[i] + field_num[i]),str(start[i])+'-'+str(end[i]),field_num[i]]
        lst.append(info)
    writer = csv.writer(f)
    for row in lst:
        writer.writerow(row)