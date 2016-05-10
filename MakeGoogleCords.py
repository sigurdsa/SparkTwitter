__author__ = 'SigurdLap'

myFile = open('GoogleCoordinates.txt', 'a')
with open('exampleFilterCoordinates3.txt', 'r') as f:
    try:
        for line in f:  # read only the first tweet/line
            if "{" in line:
                pass
            elif '"' in line:
                pass
            elif "[" in line:
                pass
            elif "]" in line:
                pass
            elif "}" in line:
                pass
            else:
                myFile.write(line);

    except Exception:
        raise

