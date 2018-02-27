from flask import Flask, request, jsonify, session, render_template
import pymysql.cursors

app = Flask(__name__) 
conn = pymysql.connect(host='localhost', database='TODO', user='cs1122', password='cs1122', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#connect to a local host database

@app.route('/')
def showWebpage():
	with conn.cursor() as cursor:
		databases = cursor.execute("SHOW DATABASES").fetchall()
		print("Databases: "+databases)
		#Go inside within a database here		cursor.execute("USE insert_database_name")	
		tables = cursor.execute("SHOW TABLES").fetchall()
		print("Tables: "+tables)
		#get columns of a table here 				columns = cursor.execute("DESCRIBE insert_table_name")
		

		for table in data:
				if table['Tables_in_db'] == 'week3'

		for week3 in data:
				response[week3['id']] = week3['items']

		json_data = jsonify(dictionary)
				return json_data

		return render_template('week3.html')

@app.route('/todo/create', methods=['POST'])
def create():
	if request.method == 'POST':
		task = request.json
		with conn.cursor() as cursor:
			cursor.execute("INSERT INTO week3(item) VALUES(task)")
			return 'Success'
	else:
		return 'failed'

@app.route('/todo/read', methods=['GET'])
def read():
	dictionary = {}
	if request.method == 'GET':
		with conn.cursor() as cursor:
			cursor.execute("SELECT item FROM week3") #selects all the stuff under items
			result = cursor.fetchall()
			for stuff in result:
				response[stuff['id']] = stuff['item']
			json_result = jsonify(dictionary)
			return json_result
	else:
		return 'failed'

@app.route('/todo/update', methods=['PUT'])
def update():
	index = request.get_json()['index']
	task = request.get_json()['task']
	with conn.cursor() as cursor:
		cursor.execute("UPDATE week3 SET item =%s WHERE week3.id=%s", (str(task),index))
		#should we index += 1 because the id goes from 1 to 4, while index goes from 0 to .....


#Not sure how to implement the delete one because if I delete one id, the numbers on the rest of the ids stay the same, while in the site the list would move up
@app.route('/todo/delete', methods=['DELETE'])
def delete():
		if request.method != 'DELETE':
				return "error: wrong request type"
		if len(session['data']) < int(deleteIndex) or len(session['data']) < 0:
			return "error: index out of range"

		with conn.cursor() as cursor:
				deleteIndex = request.json
				delete = "DELETE FROM week3 WHERE id=int(deleteIndex)"
				cursor.execute(delete)

		# del session['data'][int(deleteIndex)]
		# session.modified = True
		# print(session['data']) #print the session to make sure it was deleted
		# return jsonify("success")


if __name__ == '__main__':
		app.run(debug=True)
