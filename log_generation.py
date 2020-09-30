import csv
import sys


def analysis(switch,filename):
    lst=[]
    cf_total=ncf_total=total=0
    is_cf_s=is_cf_m=is_cf_b=0
    not_cf_s=not_cf_m=not_cf_b=0
    for i in range(1,15):
        lst.append(['pattern'+str(i),0,0,0,0])
    with open(filename,encoding='utf-8-sig')as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
            total+=1
            if switch==5:
                count = int(row['label1']) + int(row['label2']) + int(row['label3'])+ int(row['label4'])+ int(row['label5'])
                if count == 5:
                    is_cf_s += 1
                elif count == 4:
                    is_cf_m += 1
                elif count == 3:
                    is_cf_b += 1
                elif count == 2:
                    not_cf_b += 1
                elif count == 1:
                    not_cf_m += 1
                elif count == 0:
                    not_cf_s += 1
                if row['gold_label']=='1':
                    cf_total+=1
                    for i in range(1,15):
                        j=str(i)
                        if i ==1:
                            if row['pattern']=='[1]':
                                lst[i-1][1]+=1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif i==2:
                            if (j in row['pattern']) & ('12' not in row['pattern']):
                                lst[i-1][1]+=1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif i == 3:
                            if (j in row['pattern']) & ('13' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif i == 4:
                            if (j in row['pattern']) & ('14' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif i == 5:
                            if (j in row['pattern']) & ('15' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif i== 13:
                            if row['pattern']=='[13]':
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==4 :
                                    lst[i-1][4]+=1
                        elif (j in row['pattern']):
                            lst[i - 1][1] += 1
                            if count==5 :
                                lst[i-1][2]+=1
                            if count==4 :
                                lst[i-1][4]+=1
                if row['gold_label'] == '0':
                    ncf_total+=1
                    for i in range(1, 15):
                        j = str(i)
                        if i == 1:
                            if row['pattern'] == '[1]':
                                lst[i - 1][3] += 1
                        elif i == 2:
                            if (j in row['pattern']) & ('12' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 3:
                            if (j in row['pattern']) & ('13' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 4:
                            if (j in row['pattern']) & ('14' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 5:
                            if (j in row['pattern']) & ('15' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 13:
                            if row['pattern'] == '[13]':
                                lst[i - 1][3] += 1
                        elif (j in row['pattern']):
                            lst[i - 1][3] += 1
                count=0
            if switch==3:
                count = int(row['label1']) + int(row['label2']) + int(row['label3'])
                if count == 3:
                    is_cf_s += 1
                elif count == 2:
                    is_cf_b += 1
                elif count == 1:
                    not_cf_b += 1
                elif count == 0:
                    not_cf_s += 1
                if row['gold_label']=='1':
                    cf_total+=1
                    for i in range(1,15):
                        j=str(i)
                        if i ==1:
                            if row['pattern']=='[1]':
                                lst[i-1][1]+=1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif i==2:
                            if (j in row['pattern']) & ('12' not in row['pattern']):
                                lst[i-1][1]+=1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif i == 3:
                            if (j in row['pattern']) & ('13' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif i == 4:
                            if (j in row['pattern']) & ('14' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif i == 5:
                            if (j in row['pattern']) & ('15' not in row['pattern']):
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif i== 13:
                            if row['pattern']=='[13]':
                                lst[i - 1][1] += 1
                                if count==5 :
                                    lst[i-1][2]+=1
                                if count==3 :
                                    lst[i-1][4]+=1
                        elif (j in row['pattern']):
                            lst[i - 1][1] += 1
                            if count==5 :
                                lst[i-1][2]+=1
                            if count==3 :
                                lst[i-1][4]+=1
                if row['gold_label'] == '0':
                    ncf_total+=1
                    for i in range(1, 15):
                        j = str(i)
                        if i == 1:
                            if row['pattern']== '[1]':
                                lst[i - 1][3] += 1
                        elif i == 2:
                            if (j in row['pattern']) & ('12' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 3:
                            if (j in row['pattern']) & ('13' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 4:
                            if (j in row['pattern']) & ('14' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 5:
                            if (j in row['pattern']) & ('15' not in row['pattern']):
                                lst[i - 1][3] += 1
                        elif i == 13:
                            if row['pattern'] == '[13]':
                                lst[i - 1][3] += 1
                        elif (j in row['pattern']):
                            lst[i - 1][3] += 1
                count=0
        for i in range(len(lst)):
            print ('%s, %d ,is_cf#:%d, is_cf#/%s#:%.2f%%, is_strong,medium_cf#/all_strong,medium_cf_after_annotation#:%.2f%%, non-cf#:%d, %s#/all_sentences#:%.2f%%'
                  %(lst[i][0],lst[i][1]+lst[i][3],(lst[i][2]+lst[i][4]),lst[i][0],lst[i][1]/(lst[i][1]+lst[i][3]+0.00001)*100,(lst[i][2]+lst[i][4])/(is_cf_s+is_cf_m+0.00001)*100,lst[i][3],lst[i][0],(lst[i][1]+lst[i][3])/total*100))
        print('Total conuterfactual number: %d'%cf_total)
        print('Total non-counterfactal number: %d'%ncf_total)


        print("- in is_cf, strong agreement: %d(percent: %.2f)" % (is_cf_s, is_cf_s / cf_total))
        print("- in is_cf, medium agreement: %d(percent: %.2f)" % (is_cf_m, is_cf_m / cf_total))
        print("- in is_cf, border agreement: %d(percent: %.2f)" % (is_cf_b, is_cf_b / cf_total))
        print("- in not_cf, strong agreement: %d(percent: %.2f)" % (not_cf_s, not_cf_s / ncf_total))
        print("- in not_cf, medium agreement: %d(percent: %.2f)" % (not_cf_m, not_cf_m / ncf_total))
        print("- in not_cf, border agreement: %d(percent: %.2f)" % (not_cf_b, not_cf_b / ncf_total))

if __name__ =='__main__':
    savedStdout = sys.stdout
    log_file='Batch24 2019.9.19-2019.9.21.txt'
    with open(log_file, 'wt') as f:
        sys.stdout = f
        analysis(5,'../label_data/labeled_results_9.19.csv')
    sys.stdout = savedStdout
    print('All information has been saved in %s' % log_file)




