import nltk
from nltk.corpus import stopwords
import re
import pickle
import get_twitter_data_new as gtd2


sw = stopwords.words('english')
open('twitter_out.txt' , 'w').close()


################################declaration
def process_data(data):
    data = data.lower()
    data = re.sub('[\s]+', ' ', data)
    data = data.strip(' \'"?,. !')
    data = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', data)
    data = re.sub('@[^\s]+', 'AT_USER', data)
    data = re.sub(r'#([^\s]+)', r'\1', data)
    return data


def replace_two_or_more(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)


def get_stopwords(stopwords_file):
    sw.append("AT_USER")
    sw.append("URL")
    fp = open(stopwords_file , 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        sw.append(word)
        line = fp.readline()
    return sw


def get_feature_vector(data):
    feature_vector = []
    words = data.split()
    for w in words:
        w = replace_two_or_more(w)
        w = w.strip('\'"?,.!')
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if (w in sw or val is None and len(w)  < 3 ):
            continue
        else:
            feature_vector.append(w.lower())
    return feature_vector


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in document_words)
    return features
###################################################
documents_f = open("pickled_algos3/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()


feature_list_f = open("pickled_algos3/featurelist.pickle", "rb")
featureList= pickle.load(feature_list_f)
feature_list_f.close()

#print 'training...'
training_set = nltk.classify.apply_features(extract_features ,documents)
training_set = training_set[:200]
testing_set = training_set[:200]

nbc_f = open("pickled_algos3/nbc.pickle", "rb")
nbc= pickle.load(nbc_f)
nbc_f.close()

def sentiment(testdata):
    processedTestData = process_data(testdata)
    return nbc.classify(extract_features(get_feature_vector(processedTestData)))


def accuracy():
    return nltk.classify.accuracy(nbc, testing_set)

def get_tweet(keyword):
       return gtd2.get_tweet(keyword)
        



