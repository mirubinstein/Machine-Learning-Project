from fileUtil import *

fin = getFile('trainData/train.tsv')

class TrainData:
    data = createDataObject(fin)
