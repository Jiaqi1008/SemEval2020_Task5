import csv
import json
import re
import sys


def analysis(filename):
    lst=[]
    cf_total=total=0
    is_AS=is_A=no_A=0
    for i in range(1,15):
        lst.append(['pattern'+str(i),0,0,0,0])
    with open(filename,encoding='utf-8-sig')as csvfile:
        reader= csv.DictReader(csvfile)
        for row in reader:
            total+=1
            if row['antecedent']!='':
                if row['consequent']!='':
                    is_AS+= 1
                    cf_total+=1
                else:
                    is_A+=1
                    cf_total+=1
            else:
                no_A+=1
            for i in range(1,15):
                j=str(i)
                if i ==1:
                    if (j in row['pattern']) & (('10' not in row['pattern'] )or ('11' not in row['pattern'] ) or (
                            '12' not in row['pattern'] ) or('13' not in row['pattern'] ) or(
                            '14' not in row['pattern'] )or('15' not in row['pattern'] )):
                        lst[i-1][1]+=1
                        if row['antecedent'] !='':
                            if row['consequent'] !='':
                                lst[i-1][2]+=1
                            else:
                                lst[i - 1][3] += 1
                        else:
                            lst[i - 1][4] += 1
                elif i==2:
                    if (j in row['pattern']) & ('12' not in row['pattern']):
                        lst[i-1][1]+=1
                        if row['antecedent'] !='':
                            if row['consequent'] !='':
                                lst[i-1][2]+=1
                            else:
                                lst[i - 1][3] += 1
                        else:
                            lst[i - 1][4] += 1
                elif i == 3:
                    if (j in row['pattern']) & ('13' not in row['pattern']):
                        lst[i - 1][1] += 1
                        if row['antecedent'] !='':
                            if row['consequent'] !='':
                                lst[i-1][2]+=1
                            else:
                                lst[i - 1][3] += 1
                        else:
                            lst[i - 1][4] += 1
                elif i == 4:
                    if (j in row['pattern']) & ('14' not in row['pattern']):
                        lst[i - 1][1] += 1
                        if row['antecedent'] !='':
                            if row['consequent'] !='':
                                lst[i-1][2]+=1
                            else:
                                lst[i - 1][3] += 1
                        else:
                            lst[i - 1][4] += 1
                elif i == 5:
                    if (j in row['pattern']) & ('15' not in row['pattern']):
                        lst[i - 1][1] += 1
                        if row['antecedent'] !='':
                            if row['consequent'] !='':
                                lst[i-1][2]+=1
                            else:
                                lst[i - 1][3] += 1
                        else:
                            lst[i - 1][4] += 1
                elif (j in row['pattern']):
                    lst[i - 1][1] += 1
                    if row['antecedent'] != '':
                        if row['consequent'] != '':
                            lst[i - 1][2] += 1
                        else:
                            lst[i - 1][3] += 1
                    else:
                        lst[i - 1][4] += 1
        for i in range(len(lst)):
            print ('%s, totoal#:%d, A&S#/total#:%.2f%%, A#/total#:%.2f%%, no A&S#/total#:%.2f%%'
                  %(lst[i][0],lst[i][1],lst[i][2]/(lst[i][1]+0.00001)*100,lst[i][3]/(lst[i][1]+0.00001)*100,lst[i][4]/(lst[i][1]+0.00001)*100))

        print('Total conuterfactual number: %d'%cf_total)

        print("- in all sentences, with antecedent and consequent : %d(percent: %.2f)" % (is_AS, is_AS / total))
        print("- in all sentences, with antecedent only : %d(percent: %.2f)" % (is_A, is_A / total))
        print("- in all sentences, without antecedent: %d(percent: %.2f)" % (no_A, no_A / total))


if __name__ =='__main__':
    savedStdout = sys.stdout
    log_file='Batch3 2019.8.23.txt'
    with open(log_file, 'wt') as f:
        sys.stdout = f
        analysis('Dataset/Subtask2_results_8.23.csv')
    sys.stdout = savedStdout
    print('All information has been saved in %s' % log_file)




