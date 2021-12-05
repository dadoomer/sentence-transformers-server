"""Start a server with NLP functionality."""
import bottle
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import argparse

parser = argparse.ArgumentParser(description="Start an NLP server.")
parser.add_argument(
        "--port",
        type=int,
        help="Server port",
        required=True,
    )
parser.add_argument(
        "--model",
        type=str,
        help="Transformer model ID",
        required=True,
    )
args = parser.parse_args()

model = SentenceTransformer(args.model)


@bottle.error(405)
def method_not_allowed(res):
    """Adds headers to allow cross-origin requests to all OPTION requests.
    Essentially this allows requests from external domains to be processed."""
    if bottle.request.method == 'OPTIONS':
        new_res = bottle.HTTPResponse()
        new_res.set_header('Access-Control-Allow-Origin', '*')
        new_res.set_header('Access-Control-Allow-Headers', 'content-type')
        return new_res
    res.headers['Allow'] += ', OPTIONS'
    return bottle.request.app.default_error_handler(res)


@bottle.hook('after_request')
def enable_cors():
    """Sets the CORS header to `*` in all responses. This signals the clients
    that the response can be read by any domain."""
    bottle.response.set_header('Access-Control-Allow-Origin', '*')
    bottle.response.set_header('Access-Control-Allow-Headers', 'content-type')


@bottle.post('/embedding')
def embedding():
    """Returns `{'embeddings': v}` where `v` is a list of vectors with the
    embeddings of each document in `documents`."""
    documents = bottle.request.json["documents"]
    embeddings = model.encode(documents)
    return {"embeddings": embeddings.tolist()}


@bottle.post('/semantic_search')
def semantic_search():
    """Returns `{'similarities': v}` where `v` is a list of numbers with the
    similarities of `query` to each document in `documents`."""
    query = bottle.request.json["query"]
    documents = bottle.request.json["documents"]
    query_embedding = model.encode(query)
    document_embeddings = model.encode(documents)
    scores = util.dot_score(query_embedding, document_embeddings).squeeze()
    return {"similarities": [float(s) for s in scores]}

bottle.run(port=args.port)
