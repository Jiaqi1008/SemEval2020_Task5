import csv
import json

if __name__=='__main__':
    results_path='Turk/Batch_3712766_batch_results.csv'
    in_path='Turk/subtask2_check 7.19.csv'
    out_path='Subtask2_results_7.19.csv'
    header = ['gold_label', 'degree', 'sentence', 'sentence_ID', 'pattern', 'domain', 'url', 'website', 'article_ID',
              'antecedent', 'consequent','']
    total=0
    with open(in_path,encoding='utf-8-sig') as f:
        with open(out_path,'wt',newline='',encoding='utf-8') as p:
            reader=csv.DictReader(f)
            writer=csv.DictWriter(p,header)
            writer.writeheader()
            for line in reader:
                a=0
                del line['context']
                del line['full text']
                with open(results_path, encoding='utf-8-sig') as csvfile:
                    readercsv = csv.DictReader(csvfile)
                    for row in readercsv:
                        if a==1:
                            break
                        for i in range(1,21):
                            if line['sentence']==row['Input.paragraph'+str(i)]:
                                line['antecedent']=row['Answer.antecedent'+str(i)]
                                line['consequent'] = row['Answer.consequent' + str(i)]
                                a=1
                                break
                writer.writerow(line)
                total+=1
    print(total)