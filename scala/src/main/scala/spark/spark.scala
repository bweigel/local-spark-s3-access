package spark

import org.apache.spark.{SparkConf, SparkContext}

object spark {
  def main(args: Array[String]) {

    val logFile = "s3a://elasticmapreduce/samples/wordcount/wordSplitter.py"

    val conf = new SparkConf().setAppName("Simple Application")
      .setMaster("local")

    val sc = new SparkContext(conf)

    val logData = sc.textFile(logFile).cache()

    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()
    println(s"Lines with a: $numAs, Lines with b: $numBs")

    sc.stop()
  }
}
