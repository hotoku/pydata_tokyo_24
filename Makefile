DATASET := 20211126_pydata


.PHONY: clean
clean:
	bq rm -r -f $(DATASET)


.PHONY: table
table: dataset
	bq mk -t $(DATASET).prediction prediction.json


.PHONY:
dataset:
	bq mk --default_table_expiration=$$((60 * 60 * 24 * 10)) --location asia-northeast1 $(DATASET)
