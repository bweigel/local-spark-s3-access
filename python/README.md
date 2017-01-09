# Accessing S3A from PySpark

### Test-Environment

- Anaconda with Python 3.5
- Spark 2.0.2 precomiled with Hadoop 2.7
- Scala 2.12.0
- Oracle Java JVM 1.8.0_111

### Requirements

1. Add [`aws-java-sdk-1.7.4.jar`](http://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk/1.7.4) and [`hadoop-aws-2.7.1.jar`](http://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/2.7.1) to classpath using `spark.jars` setting in `spark-defaults.conf`
2. Set `spark.hadoop.fs.s3a.impl` to use correct implementation in `spark-defaults.conf` 
3. (for AWS S3 Frankfurt access) you need to use signature version 4 and specify the correct s3a endpoint. in [`$SPARK_HOME/conf/spark-defaults.conf`](../resources/spark-defaults.conf)...
    - set `spark.executor.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true` and `spark.driver.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true`
    - set `spark.hadoop.fs.s3a.endpoint=s3-eu-central-1.amazonaws.com`
  - the resulting [`$SPARK_HOME/conf/spark-defaults.conf`](../resources/spark-defaults.conf) should look like this:  
      ```
      spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
      spark.jars=/path/to/hadoop-aws-2.7.1.jar,/path/to/aws-java-sdk-1.7.4.jar
      spark.hadoop.fs.s3a.endpoint=s3-eu-central-1.amazonaws.com
      spark.executor.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true
      spark.driver.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true
      ```
4. set correct environmental variables:        
    1. set aws credentials (`AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`)  
    2. set `SPARK_HOME` to `/path/to/spark`
    3. set `PYTHONPATH` to `/path/to/spark/python`
    
__Running [PySpark script](src/spark.py)__

```bash
SPARK_HOME=/path/to/spark
PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

/path/to/python/bin/python spark.py
```

__Setting environmental variables in IntelliJ IDEA__
    
Use _Edit Run Configuration_ to set environmental variables ...

![](img/pyspark_idea_run_conf.png)
 
... or start intellij from shell, where you first have to export the environmental variables:
    
```
$ export SPARK_HOME=/path/to/spark
$ export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
$ ./path/to/idea/bin/idea.sh
```

### Example (see [src/spark.py](src/spark.py))

```python
from pyspark import SparkContext, SparkConf

def sparkly():
    logFile = "s3a://elasticmapreduce/samples/wordcount/wordSplitter.py"

    sc = SparkContext("local", "simpleApp")     

    logData = sc.textFile(logFile).cache()

    numAs = logData.filter(lambda line: line.count("a")).count()
    numBs = logData.filter(lambda line: line.count("b")).count()
    print("Lines with a: {0}, Lines with b: {1}".format(numAs, numBs))

    sc.stop()

if __name__ == "__main__":
    sparkly()
```

### TL;DR

- download [`aws-java-sdk-1.7.4.jar`](http://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk/1.7.4) and [`hadoop-aws-2.7.1.jar`](http://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/2.7.1) 
- add the following lines to [`spark-defaults.conf`](../resources/spark-defaults.conf):

```
spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
spark.jars=/path/to/hadoop-aws-2.7.1.jar,/path/to/aws-java-sdk-1.7.4.jar
spark.hadoop.fs.s3a.endpoint=s3-eu-central-1.amazonaws.com
spark.executor.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true
spark.driver.extraJavaOptions=-Dcom.amazonaws.services.s3.enableV4=true
```

<!--
- add the following to `$HADOOP_CONF_DIR/core-site.xml`:

``` xml
<configuration>

    <property>
        <name>fs.s3a.endpoint</name>
        <value>s3.eu-central-1.amazonaws.com</value>
    </property>

</configuration>
```
-->

- set environmental variables:

```
export SPARK_HOME=/path/to/spark
export PYTHONPATH=$PYTHONPATH:$SPARKHOME/python
export PYSPARK_PYTHON=/path/to/python/bin/python
```

- run script:

`AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... $PYSPARK_PYTHON src/spark.py`