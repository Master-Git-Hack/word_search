"""
Code Challenge
Module to search for words in a matrix of letters using Flask.

Date: 11 de abril de 2023
Author: Einar Jhordany Serna Valdivia
Version: 1.0.0

This module provides a Flask application that exposes an API endpoint for searching
for words in a matrix of letters. The API endpoint can be accessed via HTTP POST method
at the '/api/v1/word_search' route.

Methods
search_words(matrix: List[List[str]], words: List[str]) -> Dict[str, List[Tuple[int, int]]]:
Search for the positions of the given words in the given matrix.

endpoint_search_words() -> JSON:
Search for the given words in the given matrix, and return their positions in a JSON format.
"""
from typing import Dict, List, Tuple

from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load the environment variables from the flaskenv file
load_dotenv()

app = Flask(__name__)


def search_words(
    matrix: List[List[str]], words: List[str]
) -> Dict[str, List[Tuple[int, int]]]:
    """
    Search for the positions of the given words in the given matrix.

    Args:
        matrix: A list of lists of strings, representing the matrix of letters.
        words: A list of strings, representing the words to search for in the matrix.

    Returns:
        A dictionary with words as keys, and their positions as values (list of tuples).
    """
    positions = {}
    rows, cols = len(matrix), len(matrix[0])

    # Define the range of directions to search in
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    # Loop through the matrix and search for each word
    for i in range(rows):
        for j in range(cols):
            letter = matrix[i][j]
            matching_words = (word for word in words if letter == word[0])

            for word in matching_words:
                for direction in directions:
                    x, y = i, j
                    positions_of_letters = [
                        (x + a * direction[0], y + a * direction[1])
                        for a in range(len(word))
                    ]

                    if all(
                        0 <= pos[0] < rows
                        and 0 <= pos[1] < cols
                        and matrix[pos[0]][pos[1]] == word[i]
                        for i, pos in enumerate(positions_of_letters)
                    ):
                        positions[word] = positions_of_letters

    return positions


@app.route("/api/v1/word_search", methods=["POST"])
def endpoint_search_words():
    """
    Search for the given words in the given matrix, and return their positions in a JSON format.

    Returns:
        A JSON string with the positions of the given words.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No request data found"}), 400
    # Check if the 'matrix' and 'words' keys are present in the request data
    if "matrix" not in data:
        return jsonify({"error": "Matrix not found in request data"}), 400
    if "words" not in data:
        return jsonify({"error": "Words not found in request data"}), 400

    # Get the matrix and words from the request
    matrix = data.get("matrix")
    words = data.get("words")

    # Check if the words list is empty

    if not words:
        return jsonify({"error": "No words to search for"}), 400

    # Search for the words in the matrix
    positions = search_words(matrix, words)

    # Check if any words were found in the matrix
    if not positions:
        return jsonify({"message": "No words found in matrix"}), 404

    # Return the positions as a JSON response
    return jsonify(positions), 200


if __name__ == "__main__":
    app.run()
