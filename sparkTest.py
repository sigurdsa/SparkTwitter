from pyspark import SparkContext
import json

logFile = "C:\Users\SigurdLap\PycharmProjects\sparkTwitter\exampleFilterCoordinates1.txt"  # Should be some file on your system

sc = SparkContext("local", "Simple App")


logData = sc.textFile(logFile)

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
