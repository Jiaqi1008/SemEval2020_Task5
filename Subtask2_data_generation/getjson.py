import csv
import json
import nltk
import sys


def rule(sentence):
    cc = []
    # （1）patterns that do not use further POS tag filtering：if..then / wish were.. / if only
    tokenized = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenized)
    if case1_(tagged):
        cc.append(1)
    if case2_(tagged):
        cc.append(2)
    if case3_(tagged):
        cc.append(3)
    if case4_(tagged):
        cc.append(4)
    if case5_(tagged):
        cc.append(5)
    if len(cc) == 0:
        return 7

# Case 1
def case1_(tagged):
    case1 = 0
    for tags in tagged:
        if (tags[0] in ['If', 'if']) and (case1 == 0):
            case1 = 1
        elif (case1 == 1) and (tags[1] in ['VBD', 'MD', 'VBN']):
            case1 = 2
            continue
        elif (case1 == 2) and (tags[1] == 'MD'):
            return True  # IN VBD/MD/VBN MD

# Case 2
def case2_(tagged):
    case2 = 0
    for tags in tagged:
        if (tags[1] == 'MD') and (case2 == 0):
            case2 = 1
        elif (case2 == 1) and (tags[1] in ['VB', 'VBN']):
            case2 = 2
        elif (case2 == 2) and (tags[0] in ['If', 'if']):  # Could be better to leave 'IN' in case of interesting results
            case2 = 3
        elif (case2 == 3) and (tags[1] in ['MD', 'VBD', 'VBN']):
            return True  # MD VB/VBN IN MD/VBD/VBN

# Case 3
def case3_(tagged):
    case3 = 0
    for tags in tagged:
        if (tags[1] == 'MD') and (case3 == 0):
            case3 = 1
        elif (case3 == 1) and (tags[1] == 'VBN'):
            case3 = 2
        elif (case3 == 2) and (tags[1] == 'MD'):  # Was missing this part
            return True  # MD VBN MD

# Case 4
def case4_(tagged):
    case4a = 0
    for tags in tagged:
        if (tags[0] in ['Wish', 'wish']) and (case4a == 0):
            case4a = 1
        elif (case4a == 1) and (tags[1] in ['VBD', 'VBN']):
            return True  # wish VBD/VBN

# Case 5_
def case5_(tagged):  # I Fixed this pattern
    case5a = 0
    case5b = 0
    for tags in tagged:
        if (tags[0] in ['Had', 'had', 'were', 'Were']) and (case5a == 0):
            case5a = 1
            if (tags[0] in ['were', 'Were']):
                case5a = 2
        elif (tags[1] in ['VBD', 'VBN']) and (case5a == 1):
            case5a = 2
            continue
        elif (tags[1] == 'MD') and (case5a == 2):
            case5a = 3
        elif (tags[1] in ['VB', 'VBP', 'VBD', 'VBZ']) and (case5a == 3):
            return True  #
    for tags in tagged:
        if (tags[1] == 'MD') and (case5b == 0):
            case5b = 1
        elif (tags[1] in ['VB', 'VBP', 'VBD', 'VBZ']) and (case5b == 1):
            case5b = 2
        elif (tags[0] in ['Had', 'had', 'were', 'Were']) and (case5b == 2):
            case5b = 3
            if (tags[0] in ['were', 'Were']):
                return True
        elif (tags[1] in ['VBD', 'VBN']) and (case5b == 3):
            return True


if __name__=='__main__':
    csv.field_size_limit(500 * 1024 * 1024)
    total=count=0
    with open('subtask2_json_910_919.txt','wt',newline='',encoding='utf-8') as f:
        with open('../Pipeline/Dataset/labeled_results_9.10_context_fulltext.csv',encoding='utf-8-sig') as csvfile:
            reader=csv.DictReader(csvfile)
            for line in reader:
                total+=1
                if line['gold_label'] == '1':
                    del line['label1']
                    del line['label2']
                    del line['label3']
                    del line['label4']
                    del line['label5']
                    f.write(json.dumps(line))
                    f.write('\n')
                    count+=1
        print(count)
        with open('../Pipeline/Dataset/labeled_results_9.14_context_fulltext.csv',encoding='utf-8-sig') as csvfile:
            reader=csv.DictReader(csvfile)
            for line in reader:
                total+=1
                if line['gold_label'] == '1':
                    del line['label1']
                    del line['label2']
                    del line['label3']
                    del line['label4']
                    del line['label5']
                    f.write(json.dumps(line))
                    f.write('\n')
                    count+=1
        print(count)
        with open('../Pipeline/Dataset/labeled_results_9.15_context_fulltext.csv',encoding='utf-8-sig') as csvfile:
            reader=csv.DictReader(csvfile)
            for line in reader:
                total+=1
                if line['gold_label'] == '1':
                    del line['label1']
                    del line['label2']
                    del line['label3']
                    del line['label4']
                    del line['label5']
                    f.write(json.dumps(line))
                    f.write('\n')
                    count+=1
        print(count)
        with open('../Pipeline/Dataset/labeled_results_9.17_context_fulltext.csv',encoding='utf-8-sig') as csvfile:
            reader=csv.DictReader(csvfile)
            for line in reader:
                total+=1
                if line['gold_label'] == '1':
                    del line['label1']
                    del line['label2']
                    del line['label3']
                    del line['label4']
                    del line['label5']
                    f.write(json.dumps(line))
                    f.write('\n')
                    count+=1
        print(count)
        with open('../Pipeline/Dataset/labeled_results_9.19_context_fulltext.csv',encoding='utf-8-sig') as csvfile:
            reader=csv.DictReader(csvfile)
            for line in reader:
                total+=1
                if line['gold_label'] == '1':
                    del line['label1']
                    del line['label2']
                    del line['label3']
                    del line['label4']
                    del line['label5']
                    f.write(json.dumps(line))
                    f.write('\n')
                    count+=1
        print(count)


    print(count,total)
