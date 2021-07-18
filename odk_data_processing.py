from flask import Flask, json, request


# companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/volunteer', methods=['POST'])
def save_volunteer():
    api.logger.debug('This is request.data')
    print(request.data)
    api.logger.debug('This is request.args')
    print(request.args)
    api.logger.debug('This is request.json')
    print(request.json)
    print(f"Received request successfully")
    return "True"

if __name__ == '__main__':
    api.run()
