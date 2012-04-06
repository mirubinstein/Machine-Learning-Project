from fileUtil import *
from data import *

if __name__ == '__main__':
  # Print some sample data to make sure it works.
  data = TrainData.data
  control = TrainData.control
  disease = TrainData.disease
  genes = TrainData.genes
  ids = TrainData.ids
  
  print ids
  print data['WGAAD-148']['GI_10047091-S']
  print control['WGACON-244']['GI_10047091-S']
  print disease['WGAAD-148']['GI_10047091-S']
