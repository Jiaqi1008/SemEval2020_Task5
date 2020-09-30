import json
import re
import unicodedata
import nltk


def read_turk(turk_json_list):
    turk_list = []
    for file in turk_json_list:
        with open(file, 'r') as f:
            for line in f:
                io = line.strip('\n')
                dic = json.loads(io)
                sentence = dic['sentence']
                turk_list.append(sentence)
        f.close()
        print("finish reading % s" %str(file))
    return turk_list


def rules(sentence):
    cc = []  # POS_tag list
    key = []  # pattern list

    # input your patterns
    x = re.search('(if|If) (.*) then (.*)', sentence, re.M)
    y = re.search('(even|Even|What|what|As|as) if (.*) then (.*)', sentence, re.M)
    if x and not y:
        key.append(1)

    x = re.search('(if|If) (.*) (had|hadn\'t|had not) (?!a |the |to |an )(.*)', sentence, re.M)
    y = re.search('(even|Even|What|what|As|as) (if|If) (.*) (had|hadn\'t|had not) (?!a |the |to |an )(.*)', sentence,
                  re.M)
    if x and not y:
        key.append(2)

    x = re.search('(\'d|could|may|might|should|would|ought to) (have|not have|haven\'t) (?!a |the |to |an )(.*)',
                  sentence, re.M)
    y = re.search('(wouldn\'t|couldn\'t|shouldn\'t) have (?!a |the |to |an )(.*)', sentence, re.M)
    if x or y:
        key.append(3)

    x = re.search('(what if|What if) (.*)', sentence, re.M)
    if x:
        key.append(4)

    x = re.search('(even if|Even if) (.*)', sentence, re.M)
    if x:
        key.append(5)

    x = re.search('(if|If) (I|there|he|she|you) (were|weren\'t|were not) (?!to )(.*)', sentence, re.M)
    x1 = re.search('(even|Even|What|what|As|as) (if|If) (I|there|he|she|you) (were|weren\'t|were not) (?!to )(.*)',
                   sentence, re.M)
    y = re.search('(if|If) (.*) (were|weren\'t|were not) to (.*)', sentence, re.M)
    y1 = re.search('(even|Even|What|what|As|as) (if|If) (.*) (were|weren\'t|were not) to (.*)', sentence, re.M)
    if (x and not x1) or (y and not y1):
        key.append(6)

    x = re.search(
        '(Wish|wish) (?!to) (.*) (could|may|might|would|should|wouldn\'t|couldn\'t|shouldn\'t) (have|not have|haven\'t) (?!a |the |to |an )(.*)',
        sentence, re.M)
    y = re.search(
        '(Wish|wish) (I\'d|we\'d|you\'d|he\'d|she\'d|they\'d|there\'d) (have|not have|haven\'t) (?!a |the |to |an )(.*)',
        sentence, re.M)
    if x or y:
        key.append(7)

    x = re.search('(Wish|wish) (?!to)(.*) (were|weren\'t|(had|had not|hadn\'t) (?!a |the |to |an ))(.*)', sentence,
                  re.M)  # No need to check for a or the after had since it is perfectly valid to have it after
    if x:
        key.append(8)

    x = re.search('wish (?!to)(.*)', sentence, re.M)
    if x:
        tokenized = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized)
        if case4_(tagged):
            cc.append(4)
            key.append(9)

    x = re.search(
        '(But|but) for (?!now)(.*) (could|might|would|should|wouldn\'t|couldn\'t|shouldn\'t) (have|not have|haven\'t) (?!a |the |to |an )(.*)',
        sentence, re.M)
    if x:
        key.append(10)

    x = re.search('(If|if) only (?!for)(.*)', sentence, re.M)
    x1 = re.search('(even|Even|What|what|As|as) (If|if) only (?!for)(.*)', sentence, re.M)
    if x and not x1:
        key.append(11)

    x = re.search('(Had|Were) (.*)', sentence, re.M)
    y = re.search('(Had|Were) (.*)\?', sentence, re.M)
    # z = re.search('Were (.*) to (.*),(.*)', sentence, re.M) # This part is not working as intended for some reason.
    # Want to remove sentences like "Were I to become president, ..." so it would be helpful to make it work

    if x and not y:
        key.append(12)

    x = re.search('(if|If) ', sentence, re.M)
    x1 = re.search('(even|Even|What|what|As|as) (if|If) ', sentence, re.M)
    if x and not x1:
        tokenized = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized)
        if case1_(tagged) or case2_(tagged):
            cc.append(1)
            key.append(
                13)  # new pattern, please check -- appears good to me but could be redundant checking for tags here

    x = re.search(
        '(I\'d|we\'d|you\'d|he\'d|she\'d|they\'d|there\'d|would|could|should|might|wouldn\'t|couldn\'t|shouldn\'t) (have) (.*)(?!,)(.*)(without) (.*)',
        sentence, re.M)
    y = re.search(
        '(Without) (.*) (I\'d|we\'d|you\'d|he\'d|she\'d|they\'d|there\'d|would|could|should|might|wouldn\'t|couldn\'t|shouldn\'t|would not|could not|should not) (have) (.*)(?!,)(.*)',
        sentence, re.M)
    if x or y:
        key.append(14)

    x = re.search('(I\'d|we\'d|you\'d|he\'d|she\'d|they\'d|there\'d|could|might|should|would|ought to|cannot|can) (.*) (had|were) (I|it|there|he|she|you|they|some) (.*)', sentence, re.M)
    if x:
        key.append(15)  # no corresponding sentences for this pattern -- fixed now -- gives sentences
        # slight problem is that tags eliminate sentences like "Were I a woman or a person of color or Jewish or Muslim, I think many of the attacks against me would involve slurs against those group"
        # Above problem was fixed with tags


    # x = re.search('(I\'d|we\'d|you\'d|he\'d|she\'d|they\'d|there\'d|would|could|should|might|wouldn\'t|couldn\'t|shouldn\'t) (have|be) (.*)(?!,)(.*)(with|without) (.*)', sentence, re.M)
    # if x:
    #      key.append(15)  # Added this back in to match pattern 6 from the twitter paper
    # Amber: with "with", there would be too many non-cf sentences. We can write by ourselves

    # x = re.search('(should|shouldn\'t) have (?!a |the |to )(.*)', sentence, re.M)
    # if x:
    #     tokenized = nltk.word_tokenize(sentence)
    #
    #     tagged = nltk.pos_tag(tokenized)
    #     for tags in tagged:
    #         if (tags[1] in ['VBD', 'VBN']):
    #
    #             key.append(16)  # This part is necessary to catch sentences of pattern 4 like I should have gone... using case 4 or any other cases won't work
    #             break

    if key != []:
        # print(key)
        cc = []
        if (1 not in key) or (8 not in key) or (11 not in key) or (
                14 not in key):  # （1）patterns that do not use further POS tag filtering：if..then / wish were.. / if only
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
            # print(cc)
            if len(cc) == 0:
                return []
    return key


# Case 1
def case1_(tagged):
    case1 = 0
    for tags in tagged:
        # if (tags[1] == 'IN') and (case1 == 0):
        if (tags[0] in ['If', 'if']) and (case1 == 0):
            case1 = 1
        elif (case1 == 1) and (tags[1] in ['VBD', 'MD', 'VBN']):
            case1 = 2
            continue
        elif (case1 == 2) and (tags[1] == 'MD'):
            return True  # If VBD/MD/VBN MD


# Case 2
def case2_(tagged):
    case2 = 0
    for tags in tagged:
        if (tags[1] == 'MD') and (case2 == 0):
            case2 = 1
        elif (case2 == 1) and (tags[1] in ['VB', 'VBN']):
            case2 = 2
        # if (case2 == 2) and (tags[1] == 'IN'):
        elif (case2 == 2) and (tags[0] in ['If', 'if']):  # Could be better to leave 'IN' in case of interesting results
            case2 = 3
        elif (case2 == 3) and (tags[1] in ['MD', 'VBD', 'VBN']):
            return True  # MD VB/VBN if MD/VBD/VBN


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


# start_aid
def sentenceparse(inpath, start_aid, senten_need, turk_json_file, start_sid, sentences_file, full_article=False):
    sentence_num = 0
    q = []
    turk_list = read_turk(turk_json_file)
    with open(inpath, 'r') as f:
        for line in f:
            io = line.strip('\n')
            dic = json.loads(io)
            article_id = dic['article ID']
            if article_id >= start_aid:
                full_text = dic['full text']
                url = dic['url']
                domain = dic['domain']
                website = dic['website']
                dct = {"sentence ID": "", "pattern": "", "sentence": "", "article ID": "", "url": "", "domain": "",
                       "website": "", "context": "", "full text": ""}
                for para in full_text:
                    p1 = re.sub('<[^<]+?>', '', str(para))
                    p2 = re.sub(' +\t*\n*', ' ', p1)
                    p3 = re.sub('\t*\n*', '', p2)
                    p4 = re.sub("\u2019", "'", p3)
                    p5 = re.sub('\u2014', '-', p4)
                    p6 = re.sub('\u201c', '"', p5)
                    p7 = re.sub('\u201d', '"', p6)
                    p8 = re.sub('\u2026', '...', p7)
                    p9 = re.sub("\u2018", "'", p8)
                    p10 = re.sub("\u2022", "•", p9)
                    p11 = re.sub("\u00a0", ' ', p10)
                    p12 = re.sub("\u2009", '', p11)
                    p13 = re.sub("\u20ac", '€', p12)
                    p14 = re.sub("\u00a3", '£', p13)
                    p15 = re.sub("\u00a2", '¢', p14)
                    p16 = re.sub("\u2009", '', p15)  # new -- xy
                    p17 = re.sub("\xa0", '', p16)  # new -- xy
                    p18 = re.sub("\2010", '-', p17)  # new -- xy
                    para1 = unicodedata.normalize("NFKD", p18)
                    para2 = ' '.join(para1.split())
                    sentence_lst = para2.split('. ')

                    j = 0
                    while j < len(sentence_lst) - 1:
                        # Mr. Lee won't be cut
                        senten = sentence_lst[j] + '.'
                        # Added more abbreviations to check
                        list_of_abbreviations = ["Mr.", "Mrs.", "etc.", "Ms.", "St.", "Ave.", "Dr.", "e.g.", "i.e.",
                                                 "Blvd.", "Rd.", "approx.", "D.I.Y.", "E.T.A.", "misc.", "A.D.", "B.C.",
                                                 "D.C.", "Gov.", "sq.", " vs.", " v."]
                        # if (j != len(sentence_lst) - 1) and "Mr." in senten or "Ms." in senten or "Mrs." in senten or "etc." in senten or "Dr." in senten or "St." in senten or "Dr." in senten :
                        restart = True
                        temp = senten
                        while restart == True:
                            count = False
                            for entry in list_of_abbreviations:
                                if (j != len(sentence_lst) - 1) and entry in temp:
                                    senten = senten + " " + sentence_lst[j + 1] + '.'
                                    temp = sentence_lst[j + 1] + '.'
                                    j += 1
                                    count = True
                                    break
                            if count == False:
                                restart = False
                        j += 1
                        senten = senten.strip()
                        pattern_lst = rules(senten)


                        if (pattern_lst != []) and (senten not in turk_list) and (senten not in q) and (len(senten) >= 6):
                            q.append(senten)
                            sent_id = start_sid + sentence_num
                            sentence_num += 1
                            dct['article ID'] = article_id
                            dct['sentence ID'] = str(sent_id)
                            dct['pattern'] = pattern_lst
                            dct['sentence'] = senten
                            dct['url'] = url
                            dct['context'] = para
                            dct["domain"] = domain
                            dct["website"] = website

                            if full_article:
                                dct['full text'] = full_text  # choose to print full text or not

                            with open(sentences_file, 'a', encoding='utf-8') as p:
                                p.write(json.dumps(dct))
                                p.write('\n')
                            p.close()

                            if sentence_num == senten_need:
                                print("Collected %d sentences. Now is at %s article" % (sentence_num, article_id))
                                return
    f.close()

    return


# next time
# sentenceparse('aPolitics_articles.txt', 'P011818', 2667, ['turk_json_8000 7.1.txt', 'json_6.16_fulltext_duplicated.txt', 'json_6.24_fulltext_duplicated.txt'], 111667, 'turk_json_8000 7.11.txt', full_article=True)
# sentenceparse('aFinance_articles.txt', 'F031874', 2666, ['turk_json_8000 7.1.txt', 'json_6.16_fulltext_duplicated.txt', 'json_6.24_fulltext_duplicated.txt'], 209248, 'turk_json_8000 7.11.txt', full_article=True)
# sentenceparse('aHealth_articles.txt', 'H023622', 2667, ['turk_json_8000 7.1.txt', 'json_6.16_fulltext_duplicated.txt', 'json_6.24_fulltext_duplicated.txt'], 310667, 'turk_json_8000 7.11.txt', full_article=True)
