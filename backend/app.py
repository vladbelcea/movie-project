from flask import Flask, jsonify, request
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, origins=['*'], methods=['GET', 'POST', 'PUT', 'DELETE'], allow_headers=['Content-Type', 'Authorization'])

@app.route('/api/movies', methods=['GET'])
@cross_origin()
def get_movies():
    title = request.args.get('title', '')
    sort = request.args.get('sort', '')  #sort= title_asc
    sort_direction = sort.split('_')[1]
    sort_key = sort.split('_')[0]

    url = f'http://www.omdbapi.com/?s={title}&apikey=708b84fe'
   
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'False':
        return jsonify({'error': data['Error']})

    movies = data['Search']
    result = []
    for movie in movies:
        title = movie['Title']
        year = movie['Year']
        poster = movie['Poster']
        result.append({'title': title, 'year': year, 'poster': poster})

    result.sort(key=lambda x: x.get(sort_key), reverse=(sort_direction == 'desc'))

    return jsonify({'movies': result})

if __name__ == '__main__':
    app.run(debug=True)
