table:
	bq mk -t 20211126_pydata.prediction prediction.json


dataset:
	bq mk --default_table_expiration=$$((60 * 60 * 24 * 10)) --location asia-northeast1 20211126_pydata
