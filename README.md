# sentence-transformers-server

Single file NLP API server endpoint to perform operations like semantic search
and sentence embedding. This uses [bottle](https://bottlepy.org/) as a server
and [sbert](https://www.sbert.net/) as the embedding library.

## Installation

### Without poetry

```
git clone https://gitlab.com/da_doomer/sentence-transformers-server.git
cd sentence-transformers-server
pip install -U bottle
pip install -U sentence-transformers
python server.py --port 3000 --model all-MiniLM-L6-v2
```

### With poetry

If you have [poetry](https://python-poetry.org/) you can configure a virtual
environment automatically:

```
git clone https://gitlab.com/da_doomer/sentence-transformers-server.git
cd sentence-transformers-server
poetry install
poetry shell
python server.py --port 3000 --model all-MiniLM-L6-v2
```

## Use

```
python server.py --port PORT_N --model MODEL_ID
```

See the [list of models](https://www.sbert.net/docs/pretrained_models.html)
available in sbert.

### Semantic search

Send a POST request to `/semantic_search` of type `application/json` and the
following body structure:

```JSON
{
	"query": "make stick",
	"documents": [
		"place wooden plank at 2 comma 2",
		"craft stick",
		"place stick"
	]
```

The response is of type `application/json` and contains the similarity of the
query to the corresponding document:

```JSON
{
	"similarities": [
		0.23651659488677979,
		0.7974543571472168,
		0.5554141402244568
	]
}
```

### Sentence embedding

Send a POST request to `/embedding` of type `application/json` and the
following structure:

```JSON
{
	"documents": [
		"place wooden plank at 2 comma 2",
		"craft stick",
		"place stick"
	]
}
```

The response is of type `application/json` and contains a list of numbers
representing a vector of norm 1 which can be used with dot-product,
cosine-similarity of Euclidean distance:

```JSON
{
	"embeddings": [
		[...],
		[...],
		[...]
	]
}
```
