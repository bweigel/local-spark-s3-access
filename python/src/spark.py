from pyspark import SparkContext, SparkConf


def sparkly():
    logFile = "s3a://elasticmapreduce/samples/wordcount/wordSplitter.py"

    conf = SparkConf()\
        .setAppName("Simple Application")\
        .setMaster("local")

    #sc = SparkContext(conf)                    # for whatever reason, but this will not work
    sc = SparkContext("local", "simpleApp")     # this will however...

    logData = sc.textFile(logFile).cache()

    numAs = logData.filter(lambda line: line.count("a")).count()
    numBs = logData.filter(lambda line: line.count("b")).count()
    print("Lines with a: {0}, Lines with b: {1}".format(numAs, numBs))

    sc.stop()

if __name__ == "__main__":
    sparkly()