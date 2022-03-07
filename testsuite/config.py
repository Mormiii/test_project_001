from tinydb import TinyDB


def users_db():
	data_file = "./manual_testcases/manual_testcases.json"
	return TinyDB(data_file)