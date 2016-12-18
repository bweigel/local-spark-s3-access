Accessing S3 content from a local Spark Job
================

Lately we have been building a new data warehouse built upon the AWS Infrastructure at work. 
It has been going quite smoothly, but for the occasional ups and downs. 
However, one thing would never quite work:
Accessing S3 content from a (py)spark job that is run locally.

S3 access from AWS EMR cluster instances was quite easy. 
Simply providing the file system context `s3a://` sufficed and everything worked smoothly.
The same method on a local machine with a spark installation proved as quite cumbersome and made us encounter errors such as:

```
AttributeError: 'SparkConf' object has no attribute '_get_object_id'
```
> comment here
```
java.lang.RuntimeException: java.lang.ClassNotFoundException: Class org.apache.hadoop.fs.s3a.S3AFileSystem not found
```
> comment here
```
java.io.IOException: No FileSystem for scheme: s3a
``` 
> comment here
```
java.lang.NoSuchMethodError: com.amazonaws.services.s3.transfer.TransferManager.<init>(Lcom/amazonaws/services/s3/AmazonS3;Ljava/util/concurrent/ThreadPoolExecutor;)V
```
> bump down aws-java-sdk-x.x.x.jar to 1.7.4, see [here](https://community.hortonworks.com/questions/58920/spark-s3-write-failed.html)

...

We went through some pain and decided to put that aspect on ice for the time being. However,
 during some slack time I decided to start going at it once again. Luckily I had some luck and
 my efforts paid off.
 
Since I have spent some time banging my head, I tought I might make it easier on some people by providing some 
easy examples and verbose comments. 

I have provided examples and readmes both for [Scala](scala) and [Python](python).
I hope this helps some people and wish you luck  with your big data infrastructure!