from fileUtil import *

if __name__ == '__main__':
  # Get file
  fin = getFile('trainData/train.tsv')
  data = createDataObject(fin)
  
  print data['WGAAD-148']['GI_10047091-S']