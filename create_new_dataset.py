import os
from dotenv import load_dotenv
from pyDataverse.api import NativeApi
from pprint import pprint

import json
load_dotenv()

BASE_URL = os.environ['BASE_URL']
API_TOKEN = os.environ['API_TOKEN']

api = NativeApi(BASE_URL, API_TOKEN)

###################################################
# Dataverse Level
###################################################

DATAVERSE = os.environ["DATAVERSE"]

resp = api.get_dataverse(DATAVERSE)
pprint(resp.json())

# create_dataverse
# publish_dataverse
# delete_dataverse
# get_dataverse_roles

resp = api.get_dataverse_roles(DATAVERSE)
pprint(resp.json())

resp = api.get_dataverse_contents(DATAVERSE)
pprint(resp.json())

resp = api.get_dataverse_facets(DATAVERSE)
pprint(resp.json())

resp = api.dataverse_id2alias("243")
pprint(resp)

###################################################
# Dataset Level
###################################################


# Existing dataset that I created using the Web Interface
resp = api.get_dataset("doi:10.5072/FK2/OJTRUA")
pprint(resp.json(), compact=True, width=80, depth=3)
print( json.dumps(resp.json(), indent=4))
# Save the json
ds1_json = resp.json()


# get_dataset
# get_dataset_versions
# get_dataset_version
# get_dataset_export


# Triying to figure which fields are relevant. SOURCE Schema from:
# https://github.com/gdcc/pyDataverse/blob/main/pyDataverse/schemas/json/dataset_upload_default_schema.json

# According to the Guide, these are the minimum parameters
# https://guides.dataverse.org/en/latest/api/native-api.html#create-a-dataset-in-a-dataverse-collection
# minimum_dataset_metadata.json
with open('minimum_dataset_metadata.json') as file:
    metadata = json.load(file)
resp = api.create_dataset(dataverse=DATAVERSE,
                          metadata=metadata)
pprint(resp.json())
# But it returns an error
# {'code': 400,
#  'message': 'Bad Request. The API request cannot be completed with the '
#             'parameters supplied. Please check your code for typos, or consult '
#             'our API guide at http://guides.dataverse.org.',
#  'requestMethod': 'POST',
#  'requestUrl': 'https://dataverse.example.com/api/v1/dataverses/my_dataverse/datasets?User-Agent=pydataverse&key=MY-TOKEN',
#  'status': 'ERROR'}

# So, using the WebInterface, the mandatory fields are the following:
#
# WebInterface HPC-Dev Dataverse REQUIRED FIELDS
# Title
# Author
#    Name
#    Affiliation
#    Identifier Type: [ORCID ISNI LCNA VIAF GND DAI ResearcherID ScopusID]
#    Identifier
# Description
#    Text
#    ---Date--- NOT REQUIRED
# Subject
#    Agricultural Sciences, Arts and Humanities, Astronomy and Astrophysics
#    Business and Management, Chemistry, Computer and Information Science
#    Earth and Environmental Sciences, Engineering, Law, Mathematical Sciences,
#    "Medicine, Health and Life Sciences", Physics, Social Sciences, Other
# ---Keyword--- NOT REQUIRED, Skip
# ---Related Publication--- Not Required, Skip
#    ---arxiv, doi...---
# ---Notes--- NOT REQUIRED, Skip
# Funding Information
#    Agency
#    ---Identifier---
# ---Depositor--- NOT REQUIRED, Skip
# ---Deposit Date--- NOT REQUIRED, Skip


from pyDataverse.models import Dataset
from pyDataverse.utils import read_file

ds = Dataset()
ds_filename = "minimum_dataset_metadata.json"
ds.from_json(read_file(ds_filename))
ds.get()
ds.set({'title':'Youth from Austria 2005'})
ds.get()['author']
ds.validate_json()


# Existing dataset that I created using the Web Interface
resp = api.get_dataset("doi:10.5072/FK2/OJTRUA")
pprint(resp.json(), compact=True, width=80, depth=2)
# Save the json
#ds1_json = resp.json()


ds1 = Dataset()
ds1_filename = "metadata_dataset_test.json"
ds1.from_json(read_file(ds1_filename))
ds1.set({'title':'New Dataset created with API & pyDataverse'})
datasetContactInfo= {'datasetContact': [
    {'datasetContactName': 'Gómez-Cortés, Felipe L', 
     'datasetContactAffiliation': 'HPC', 
     'datasetContactEmail': 'felipe@example.com'}]}
ds1.set(datasetContactInfo)
ds1.validate_json()
metadata = ds1.json()

# Returns ERROR, Dataverse Identifier not found
resp = api.create_dataset("Felipe SANDBOX Dataverse", ds1.json())
resp.json()


# Returns ERROR, Bad Request
resp = api.create_dataset(243, ds1.json())
resp.json()
# 'status': 'ERROR', 'code': 400, 'message': 'Bad Request. The API request cannot be completed with the parameters supplied...'

# Returns ERROR, Bad Request
resp = api.create_dataset(DATAVERSE, ds1.json())
resp.json()
# 'status': 'ERROR', 'code': 400, 'message': 'Bad Request. The API request cannot be completed with the parameters supplied...'
