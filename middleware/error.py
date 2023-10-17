from app import app


@app.errorhandler(Exception)
def bad_request(error):
    print('Error:', error)
    print(str(error))
    return f'Bad Request: {str(error)}', 400

