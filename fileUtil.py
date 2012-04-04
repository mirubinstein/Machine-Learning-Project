import sys

def getFile(path=None):
  """ Get file from stdin, ask for it if it's not there"""
  # If input, use as stdin
  if len(sys.argv) < 2:
    # Ask the user for the name of the file
    if path == None:
      print "Filename: ", 
      filename = sys.stdin.readline().strip()
    else:
      filename = path
  # Else use file input.
  else:
    filename = sys.argv[1]

  try:
    fin = open(filename, "r")
  except IOError:
    print "Error: The file '%s' was not found on this system." % filename
    sys.exit(0)
    
  return fin
  
def createDataObject(fin):
  """Creates a data object for this data. The format is a dictionary of id's which have a dictionary of genes within them. Call like this : data['Target ID']['Gene'] """
  # Get the target ids
  targetIds = fin.readline().rstrip().split('\t')
  targetIds.pop(0)
  
  # Create genes array
  genes = []
  
  # Grab a copy of the lines so we can iterate multiple times
  lines = fin.readlines()
  geneTypes = []
  
  # Collect All Genes Types
  for line in lines:
    geneArray = line.rstrip().split('\t');
    geneTypes.append(geneArray.pop(0))
    genes.append(geneArray)

  data = {}
  for person in range(len(targetIds)):
    indivData = []
    for gene in range(len(geneTypes)):
      indivData.append(genes[gene][person])
    data[targetIds[person]] = dict(zip(geneTypes, indivData))

  return data

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
      
