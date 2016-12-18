# Accessing S3A from Spark

Tips are aggregated from [this blogpost](http://deploymentzone.com/2015/12/20/s3a-on-spark-on-aws-ec2/).

1. add dependency to project: [`aws-java-sdk-1.7.4.jar`](http://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk/1.7.4) 
    - add `libraryDependencies += "com.amazonaws" % "aws-java-sdk" % "1.7.4"` to [`build.sbt`](build.sbt)
2. add dependency to project: [`hadoop-aws-2.7.1.jar`](http://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/2.7.1)  
    - add `libraryDependencies += "org.apache.hadoop" % "hadoop-aws" % "2.7.1"` to [`build.sbt`](build.sbt)
3. specify s3a implementation, either ...
    - ... in code: 
    ``` scala
    val conf = new SparkConf().setAppName("Simple Application")
      .setMaster("local")
      .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

    val sc = new SparkContext(conf)
    ```
    - ... or in [`SPARK_HOME/conf/spark-defaults.conf`](../resources/spark-defaults.conf):
    ```
    spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
    ```
4. specify aws access key id and secret key, either ...
    - ... in code:
    ``` scala
    sc.hadoopConfiguration.set("fs.s3a.access.key", "...")
    sc.hadoopConfiguration.set("fs.s3a.secret.key", "...")
    ```
    - ... or as environmental variables (IntelliJ => set in Run Configuration):
    ```
    export AWS_ACCESS_KEY_ID=... 
    export AWS_SECRET_ACCESS_KEY=...
    ```
    
Minimal working example (Scala):

```scala
import org.apache.spark.{SparkConf, SparkContext}

object spark {
  def main(args: Array[String]) {

    val logFile = "s3a://elasticmapreduce/samples/wordcount/wordSplitter.py"

    val conf = new SparkConf()
      .setAppName("Simple Application")
      .setMaster("local")

    val sc = new SparkContext(conf)

    val logData = sc.textFile(logFile).cache()

    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()
    println(s"Lines with a: $numAs, Lines with b: $numBs")

    sc.stop()
  }
}
```

### TL;DR

- Add the following lines to [`spark-defaults.conf`](../resources/spark-defaults.conf):

```
spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
spark.jars=/path/to/hadoop-aws-2.7.1.jar,/path/to/aws-java-sdk-1.7.4.jar
```

- Set environmental variables:

```
export SPARK_HOME=/path/to/spark
```

- run application using sbt:

`AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... sbt run`
     