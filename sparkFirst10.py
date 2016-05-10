from pyspark import SparkContext


logFile = "geotweets31.txt"  # Should be some file on your system

sc = SparkContext("local", "Simple App")

logData = sc.textFile(logFile)

logData.first(10)
logData.saveAsTextFile("geotweets31_first_10.txt")
