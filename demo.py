from EmotionRecognition.configuration.aws_syncer import S3Sync

obj = S3Sync('emtion-sentiment')
obj.download_from_s3('text.csv','datapath/newtxt.csv')
obj.upload_to_s3('datapath/sentiment.csv' ,'sentiment.csv')