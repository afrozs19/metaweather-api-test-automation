import json
import utilities.setup as st


def readJson(jsonFileName):
    """
        Function to read the JSON files from data folder 
            and provide JSON content to calling Test Case for Assertion.    
    """
    jsonFilePath = f"{st.get_root_test_dir()}/data/{jsonFileName}.json"

    with open(jsonFilePath) as f:
        jsonFile = json.load(f)

    return jsonFile
