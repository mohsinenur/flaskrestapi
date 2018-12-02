from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'Python'}, {'name': 'Java'}, {'name': 'C++'}]


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'It works'})


@app.route('/lang/', methods=['GET'])
def return_all():
	return jsonify({'language': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
	lang = [language for language in languages if language['name'] == name]
	return jsonify({'language': lang[0]})


@app.route('/lang/', methods=['POST'])
def add_one():
	lang = {'name': request.json['name']}
	languages.append(lang)
	return jsonify({'language': languages})


if __name__ == '__main__':
	app.run(debug=True, port=8080)
