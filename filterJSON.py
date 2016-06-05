import json

#with open('C:\Users\SigurdLap\Desktop\Master\geotweets3_first_10.txt', 'r') as f:
myFile = open('exampleFilter3.txt', 'a')
with open('geotweets31.txt', 'r') as f:
    try:
        for line in f:  # read only the first tweet/line
            try:  # handle JSON errors
                tweet = json.loads(line)  # load it as Python dict
                myFile.write(json.dumps(tweet['place']['country_code']) + ', ')
                myFile.write(json.dumps(tweet['created_at']) + ', ')
                myFile.write(json.dumps(tweet['source']) + ', ')
                myFile.write(json.dumps(tweet['id']) + ', ')
                # myFile.write(json.dumps(tweet['user']['lang']) + ', ')
                myFile.write(json.dumps(tweet['lang']) + ', ')
                # myFile.write(json.dumps(tweet['user']['location']) + ', ')
                myFile.write(json.dumps(tweet['user']['time_zone']) + ', ')
                myFile.write(json.dumps(tweet['user']['lang']) + ', ')

                myFile.write('\n')
            except ValueError:
                pass
            except RuntimeError:
                pass
            except TypeError:
                pass
    except Exception:
        print "Unexpected error:", sys.exc_info()[0]
        raise
