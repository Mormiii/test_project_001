from tinydb import TinyDB


def users_db():
	data_file = "./test_data/test_data.json"
	return TinyDB(data_file)