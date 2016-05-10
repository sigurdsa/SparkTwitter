import json


#with open('C:\Users\SigurdLap\Desktop\Master\geotweets3_first_10.txt', 'r') as f:
myFile = open('exampleFilterCoordinates3.txt', 'a')
with open('geotweets31.txt', 'r') as f:

    try:
        for line in f:  # read only the first tweet/line
            try:
                tweet = json.loads(line)  # load it as Python dict
                myFile.write(json.dumps(tweet['place']['bounding_box']) + '\n')
            except ValueError:
                pass
                print "valueError detected"
            except RuntimeError:
                print "Runtime Error"
                pass
            except TypeError:
                print "Typeerror"
                pass
    except Exception:
        print "Unexpected error:", sys.exc_info()[0]
        raise
