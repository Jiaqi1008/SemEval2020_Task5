import csv
from collections import Counter
import os
import numpy as np
from io import StringIO
import json


def getExtraction(path,lst,heading):
    lst.append(heading)
    with open(path,encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['AssignmentStatus']!='Rejected':
                s=[]
                for i in heading:
                    s.append(row[i])
                lst.append(s)
    return lst

def workerpickup(lst,f_num,t_avg,path):
    id=[]
    li = [a[1] for a in lst]
    s = Counter(li).most_common(f_num)
    for i in range(f_num):
        id.append(s[i][0])
    if os.path.exists(path):
        os.remove(path)
    csvfile = open(path, 'a', newline='', encoding='utf-8')
    writer=csv.writer(csvfile)
    for row in lst:
        if row[1]=='WorkerId':
            continue
        if row[1] in id:
            writer.writerow(row)
            continue
        if int(row[2])<t_avg:
            writer.writerow(row)
    csvfile.close()
    return id

def getgoldkey(lst,in_path,out_path):
    pos=['']
    list=[]
    s=[]
    ss=[]
    for row in lst:
        if row[3]=='Input.paragraph1':
            continue
        if int(pos[0] != row[3]):
            del pos[0]
            pos.append(row[3])
            if ss!=[]:
                list.append(np.array(ss).transpose().tolist())
                ss = []
        s.append(pos[0])
        for i in range(4,24):
            if row[i]=="X":
                s.append(7)
                continue
            s.append(row[i])
        ss.append(s)
        s=[]
    list.append(np.array(ss).transpose().tolist())
    result_stat=result_to_key(list,in_path,out_path)
    return result_stat

def result_to_key(lst,in_path,out_path):
    a=-1
    cont=k=0
    cf=ncf=cf_5=cf_3=cf_2=error=total=0
    list=[]
    with open(in_path,encoding='utf-8') as f:
        with open(out_path,'wt',encoding='utf-8') as p:
            for line in f:
                io = StringIO(line.strip('\n'))
                dic = json.load(io)
                if a== -1:
                    for k in range(len(lst)):
                        if (dic['sentence']==lst[k][0][0])or(dic['sentence']==(' '+lst[k][0][0])):
                            lst[k][0][0]=''
                            a=len(lst[k])-2
                            break
                if a!=-1:
                    for i in range(len(lst[k][0])):
                        j='label'+str(i+1)
                        dic[j]=lst[k][len(lst[k])-a-1][i]
                        cont+=int(dic[j])
                    if cont<3:
                        dic['gold_label'] = 0
                        ncf+=1
                    elif cont<6:
                        dic['gold_label'] = 1
                        cf+=1
                    # elif cont>5:
                    #     dic['gold_label'] = 'Error'
                    #     error+=1
                    if cont==5 or cont==0:
                        cf_3+=1
                    if cont==4 or cont==1:
                        cf_2+=1
                    if cont==2 or cont==3:
                        cf_5+=1
                    total+=1
                    cont=0
                    a-=1
                del dic['context']
                del dic['full text']
                p.write(json.dumps(dic))
                p.write('\n')
            list.append('Total num: '+str(total))
            list.append('Counterfactual num: '+str(cf))
            list.append('Non-Counterfactual num: '+str(ncf))
            list.append('Error num: '+str(error))
            list.append('Strong agreement num: '+str(cf_3))
            list.append('Not Strong agreement num: '+str(cf_2))
            list.append('Weak agreement num: '+str(cf_5))
            for k in range(len(lst)):
                print(lst[k][0][0])
    return list


if __name__=='__main__':
    #changable parameters
    results_path='../Batch_3773394_batch_results.csv'
    in_path='../turk_json_2000 9.19.txt'
    out_path='turk_json_processed.txt'
    workerpickup_path='workerpickup.csv'
    f_num=3
    t_avg=0
    lst=[]
    heading=['HITId', 'WorkerId', 'WorkTimeInSeconds','Input.paragraph1',]
    #################################

    for i in range(20):
        a='Answer.Sel1@cvae&memo_cvae'+str(i+1)
        heading.append(a)

    infolist=getExtraction(results_path,lst,heading)
    select_list=workerpickup(infolist,f_num,t_avg,workerpickup_path)
    resultstat_list=getgoldkey(infolist,in_path,out_path)
    print(resultstat_list)










