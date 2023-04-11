# Code Challenge

This module provides a Flask application that exposes an API endpoint for searching for words in a matrix of letters. The API endpoint can be accessed via HTTP POST method at the `/api/v1/word_search` route.

# Requirements

- Python 3.x
- Flask 2.2.3
- python-dotenv 1.0.0

# Installation
1. Clone this repository:

2. Change into the project directory:

```sh
$ cd word-search-api

3. Create a virtual environment:

```sh
$ python -m venv venv
```

4. Activate the virtual environment:

```sh
$ source venv/bin/activate  # for Linux/Mac
$ venv\Scripts\activate    # for Windows
```

5. Install the required packages:

```sh
$ pip install -r requirements.txt
```

6. Usage

To start the Flask application, run:
```sh
$ python app.py
```
o
```sh
$ flask run
```

This will start the application on http://localhost:5000. You can then use a tool like curl or Postman to make HTTP POST requests to the /api/v1/word_search endpoint.

# Example Request

```sh
$ curl -X POST \
       -H "Content-Type: application/json" \
       -d '{"matrix" : [[ "c", "g", "h", "t" ],[ "a", "a", "a", "y" ],[ "s", "z", "p", "g" ],[ "a", "o", "b", "a" ]],"words" : ["casa", "capa"]}' \
       http://localhost:5000/api/v1/word_search
```

# Example Response

```json
{ "capa": [ [ 0, 0 ], [ 1, 1 ], [ 2, 2 ], [ 3, 3 ] ], "casa": [ [ 0, 0 ], [ 1, 0 ], [ 2, 0 ], [ 3, 0 ] ] }
```

# Author

Einar Jhordany Serna Valdivia

# Version

1.0.0