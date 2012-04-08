from fileUtil import *
from data import *
from PyML import *

if __name__ == '__main__':
    # Print some sample data to make sure it works.

  rawdata = TrainData.data
  control = TrainData.control
  disease = TrainData.disease
  genes = TrainData.genes
  ids = TrainData.ids

  #PyML
  data = SparseDataSet('trainData/train.data')
  '''
  print 'Recursive Feature Elimination'
  rfe = featsel.RFE()
  rfe.select(data)
    
  features = data.featureID
  print 'Number of features selected: ' + str(len(features)) + ' of ' + str(len(genes))
  '''

  print 'Filter Method'
  score = featsel.FeatureScore('golub')
  filter = featsel.Filter(score)
  filter.select(data)
  
  features = data.featureID
  print 'Number of features selected: ' + str(len(features)) + ' of ' + str(len(genes))
  print features
  
  
    
    
