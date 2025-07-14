from datetime import datetime
import os



def generateOutput(INSTANCE_NAME,REPO_NAME,RESULTS,OUTPUT_FOLDER="output",RESULTS_FILE="results.csv"):
    currTime = datetime.now()
    year = currTime.year
    month = currTime.month
    day = currTime.day
    hour = currTime.hour
    minute = currTime.minute
    second = currTime.second

    title = f"{INSTANCE_NAME}_{REPO_NAME}_{year}_{month}_{day}_{hour}_{minute}_{second}"

    outputPath = os.path.join(OUTPUT_FOLDER,title)
    os.mkdir(outputPath)

    results_string = f"distance;duration;path\n{RESULTS.get('cost')};{RESULTS.get('duration')};{RESULTS.get('tour')}\n"
    results_path = os.path.join(outputPath,RESULTS_FILE)
    with open(results_path,'w') as file:
        file.write(results_string)
    
def getGapBKS(bks,br):
    return ((br - bks)/bks) * 100