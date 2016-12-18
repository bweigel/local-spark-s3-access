# Accessing S3A from pySpark

__Test-Environment__

- Anaconda with Python 3.5
- Spark 2.0.2 precomiled with Hadoop 2.7
- Scala 2.12.0
- Oracle Java JVM 1.8.0_111

__Requirements__

1. Add `aws-java-sdk 1.7.4.jar` and `hadoop-aws 2.7.1.jar` to classpath using `spark.jars` setting in `spark-defaults.conf`
2. Set `spark.hadoop.fs.s3a.impl` to use correct implementation in `spark-defaults.conf` 
    - => resulting `$SPARK_HOME/conf/spark-defaults.conf`:
        ```
        spark.jars=/home/bweigel/Public/s3-jars/hadoop-aws-2.7.1.jar,/home/bweigel/Public/s3-jars/aws-jav$
        spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
        ```
3. set correct environmental variables:        
    1. set aws credentials (`AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`)  
    2. set `SPARK_HOME` to `/path/to/spark`
    3. set `PYTHONPATH` to `/path/to/spark/python`
    
__Setting environmental variables in IntelliJ__
    
Use _Edit Run Configuration_ to set environmental variables or start intellij from shell, where you first have to export the environmental variables:
    
    ```
    $ export SPARK_HOME=/path/to/spark
    $ export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python
    $ export AWS_ACCESS_KEY_ID=...
    $ export AWS_SECRET_ACCESS_KEY=...
    $ ./path/to/idea/bin/idea.sh
    ```