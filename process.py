import csv
import json


if __name__ =='__main__':
    header = ['gold_label', 'degree', 'sentence', 'sentence_ID', 'pattern', 'domain', 'url', 'label1', 'label2',
              'label3','label4','label5', 'website', 'article_ID','context','full text']
    total=0
    lst=[]
    dic={}
    with open('../label_data/labeled_results_7.31.csv',encoding='utf-8-sig') as csvfile:
        with open('labeled_results_7.11_context_fulltext.csv','wt',newline='',encoding='utf-8') as f:
            reader=csv.DictReader(csvfile)
            writer=csv.DictWriter(f,header)
            writer.writeheader()
            for row in reader:
                with open('../label_data/turk_json_processed.txt',encoding='utf-8-sig') as txt:
                    for l in txt.readlines():
                        line=json.loads(l)
                        if row['sentence_ID']==line['sentence ID']:
                            dic['gold_label']=row['gold_label']
                            dic['degree']=row['degree']
                            dic['sentence']=row['sentence']
                            dic['sentence_ID']=row['sentence_ID']
                            dic['pattern']=row['pattern']
                            dic['domain']=row['domain']
                            dic['url']=row['url']
                            dic['label1']=row['label1']
                            dic['label2']=row['label2']
                            dic['label3']=row['label3']
                            dic['label4']=row['label4']
                            dic['label5']=row['label5']
                            dic['website']=row['website']
                            dic['article_ID']=row['article_ID']
                            dic['context']=line['context']
                            dic['full text']=line['full text']
                            writer.writerow(dic)
                            total+=1
                            break
                print('\r%.3f%%' % (total / 8000 * 100), end='')
