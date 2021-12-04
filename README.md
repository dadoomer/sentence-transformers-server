# sentence-transformers-server

Your own API endpoint to perform NLP functions like semantic search, sentence
embedding, etc. This uses [bottle](https://bottlepy.org/) as a server and
[sbert](https://www.sbert.net/) as the embedding library.

## Installation instructions

Install the dependencies in [pyproject.toml](pyproject.toml) and you are good
to go: `python server.py --port 3000`.

Assuming you have Python3.9 or above and
[poetry](https://python-poetry.org/) you can do this automatically with:

```
poetry install
poetry shell
python server.py --port 3000
```

## Use

### Semantic search

Send a POST request with the following structure:

```JSON
{
	"query": "this is my query in natural language",
	"documents": [
		"sentence 1 to compare against",
		"another sentence",
		"just one more as an example,
	]
```

The returned value is a list of numbers, each number the computed similarity
of the query to the corresponding document.

### Sentence embedding

TODO (pull requests accepted).

Send a POST request with the following structure:

```JSON
{
	"query": "this is my query in natural language",
}
```

The returned value is a list of numbers representing a vector
of norm 1 which can be used with dot-product, cosine-similarity of
Euclidean distance.

## Using other models

Simply modify the code to select a different model. TODO: add
this functionality as an argument to `server.py` (pull requests accepted).
