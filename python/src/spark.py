from pyspark import SparkContext, SparkConf

def sparkly():
    #logFile = "s3a://elasticmapreduce/samples/wordcount/wordSplitter.py"
    logFile = "s3a://europace.reporting/banking-batch.csv"

    conf = SparkConf()\
        .setAppName("Simple Application")\
        .setMaster("local")

    sc = SparkContext().getOrCreate(conf)

    logData = sc.textFile(logFile).cache()

    numAs = logData.filter(lambda line: line.count("a")).count()
    numBs = logData.filter(lambda line: line.count("b")).count()
    print("Lines with a: {0}, Lines with b: {1}".format(numAs, numBs))

    sc.stop()

if __name__ == "__main__":
    sparkly()
