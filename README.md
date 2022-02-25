# sentence-transformers-server

Single-file Natural-Language-Processing API server to perform semantic search
and sentence embedding. This uses [bottle](https://bottlepy.org/) as the server
and [sbert](https://www.sbert.net/) as the embedding library.

Visit the [official Gitlab
repo](https://gitlab.com/da_doomer/sentence-transformers-server) or the [Github
mirror](https://github.com/dadoomer/sentence-transformers-server).

## Demo

Visit the [demo page](https://da_doomer.gitlab.io/sentence-transformers-server/) to confirm your server is
reachable.

## Installation

### Without poetry

```bash
git clone https://gitlab.com/da_doomer/sentence-transformers-server.git
cd sentence-transformers-server
pip install -U bottle
pip install -U sentence-transformers
python server.py --port 3000 --model all-MiniLM-L6-v2
```

### With poetry

If you have [poetry](https://python-poetry.org/) you can configure a virtual
environment automatically:

```bash
git clone https://gitlab.com/da_doomer/sentence-transformers-server.git
cd sentence-transformers-server
poetry install
poetry shell
python server.py --port 3000 --model all-MiniLM-L6-v2
```

## Use

```bash
python server.py --port PORT_N --model MODEL_ID
```

See the [list of models](https://www.sbert.net/docs/pretrained_models.html)
available in sbert.

See the provided [javascript example](public/index.html#L16).

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
}
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

The response is of type `application/json` and contains for each document
a list of numbers representing a vector of norm 1 which can be used with
dot-product, cosine-similarity of Euclidean distance:

```JSON
{
	"embeddings": [
		[...],
		[...],
		[...]
	]
}
```
