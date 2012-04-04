from fileUtil import *

fin = getFile('trainData/train.tsv')

def createControlData(data):
  control = {}
  for item in data:
    if item.startswith("WGACON"):
      control[item] = data[item]
  return control

def createDiseaseData(data):
  disease = {}
  for item in data:
    if item.startswith("WGAAD"):
      disease[item] = data[item]
  return disease

class TrainData:
    data = createDataObject(fin)
    control = createControlData(data)
    disease = createDiseaseData(data)
