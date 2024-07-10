import json

CV_DATA_PATH = 'app/data/cv_data.json'


def read_cv_data():
	with open(CV_DATA_PATH, 'r') as f:
		return json.load(f)


def get_cv_by_id(id: int) -> dict:
	cv_data = read_cv_data()
	for cv in cv_data:
		if cv['id'] == id:
			return cv
	return None