from fileUtil import *

fin = getFile('trainData/train.tsv')

def getGenes(data):
  genes = []
  for gene in data['WGAAD-148'].keys():
    genes.append(gene)
  return genes

def getIds(data):
  ids = []
  for targetId in data.keys():
    ids.append(targetId)
  return ids
  
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
    genes = getGenes(data)
    ids = getIds(data)