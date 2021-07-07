"""
After running 2021-nyc-parse.py, run this file to upload and/or modify the data as needed
"""
import json
import os
import requests

UPLOAD_CACHE_FILENAME ='cache/uploads.json'
API_KEY = os.environ['RCVIS_API_KEY']

def getUploadsData():
    if not os.path.exists(UPLOAD_CACHE_FILENAME):
        return {}

    with open(UPLOAD_CACHE_FILENAME, 'r') as f:
        data = json.loads(f.read())
    return data

def has_uploaded_id(filepath):
    data = getUploadsData()
    return filepath in data

def set_uploaded_id(filepath, uploadedId):
    data = getUploadsData()
    assert filepath not in data
    data[filepath] = uploadedId
    if not os.path.exists(UPLOAD_CACHE_FILENAME):
        print("creating cache file to prevent duplicate uploads")

    with open(UPLOAD_CACHE_FILENAME, 'w') as f:
        json.dump(data, f)

def get_header():
    return {
        "Authorization": f"Token {API_KEY}"
    }

def post_all_files_to_rcvis():
    url = 'https://rcvis.com/api/visualizations/'
    for filename in os.listdir('outdir'):
        if '024306' in filename:
            # Skip the mayor - it's already up
            continue
        filepath = f'outdir/{filename}'
        print(f"Looking at {filepath}")

        with open(filepath, 'rb') as jsonFile:
            if has_uploaded_id(filepath):
                print(f"Ignoring already-uploaded file {filepath}. Did you want to patch?")
                continue

            files = {'jsonFile': jsonFile}

            response = requests.post(url, files=files, headers=get_header())
            assert response.status_code == 201
            responseJson = response.json()
            uploadedId = responseJson['id']
            set_uploaded_id(filepath, uploadedId)

def patch_all_files_to_rcvis():
    data = getUploadsData()
    for filepath, uploadedId in data.items():
        filename = filepath[len('outdir/'):-len('.json')]

        #with open(filepath, 'rb') as jsonFile:
        #    data = json.loads(jsonFile.read())
        #source = f'https://web.enrboenyc.us/rcv/{filename}_1.html'
        #url = f'https://rcvis.com/api/bp/{uploadedId}/'
        #response = requests.patch(url, headers=get_header(), data={'dataSourceURL': source})
        #assert response.status_code == 200
        #print("Done patching", filename, uploadedId)

        url = f'https://rcvis.com/api/visualizations/{uploadedId}/'
        with open(filepath, 'rb') as jsonFile:
            response = requests.patch(url, headers=get_header(), files={'jsonFile': jsonFile})
        assert response.status_code == 200
        print("Done patching", filename, uploadedId)
# Uncomment to upload all files to RCVis
# post_all_files_to_rcvis()

# Uncomment to patch files with whatever custom patch you wanna create
patch_all_files_to_rcvis()
