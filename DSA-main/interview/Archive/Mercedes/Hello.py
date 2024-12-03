# word_rapid = ['dataset-india-eye', 'dataset-india-face', 'dataset-europe-Face', 
#  'dataset-america-child', 'china-dataset-body', 'dataset-india-head', 
#  'dataset-america-head', 'dataset-china-eye', 'dataset-europe-child']

# output = [ 'dataset-india-face', 'dataset-europe-Face']

def filter_w(word):
    res = []
    for i in word:
        if 'face' in i.lower():
            res.append(i)
    return res


if __name__ == "__main__":
    word_rapid = ['dataset-india-eye', 'dataset-india-face', 'dataset-europe-Face', 
 'dataset-america-child', 'china-dataset-body', 'dataset-india-head', 
 'dataset-america-head', 'dataset-china-eye', 'dataset-europe-child']
    res = filter_w(word_rapid)
    print(res)