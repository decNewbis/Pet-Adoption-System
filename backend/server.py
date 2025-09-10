from flask import Flask


app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello'


@app.route('/auth/register', methods=['POST'])
def register():
    pass


@app.route('/auth/login', methods=['POST'])
def login():
    pass


@app.route('/users/profile', methods=['GET'])
def user_profile():
    pass


@app.route('/pets', methods=['GET'])
def pets_list():
    pass


@app.route('/pets/<string:id_>', methods=['GET'])
def pet_profile(id_):
    pass


@app.route('/pets', methods=['POST'])
def add_pet():
    pass

@app.route('/pets/<string:id_>', methods=['PUT'])
def update_pet_profile():
    pass


@app.route('/pets/<string:id_>', methods=['DELETE'])
def remove_pet():
    pass


@app.route('/adoptions', methods=['POST'])
def add_adoption_request():
    pass


@app.route('/adoptions/user', methods=['GET'])
def get_user_adoptions_requests():
    pass


@app.route('/adoptions', methods=['GET'])
def get_all_adoptions_requests():
    pass


@app.route('/adoptions/<string:id_>', methods=['PUT'])
def update_adoption():
    pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)