from utils import load_chunks
from embeddings import SiliconFlowEmbedding
from vector_store import build_index, save_index

MAX_LEN = 500
OVERLAP = 0
INDEX_PATH = f"index_{MAX_LEN}_{OVERLAP}.json" if OVERLAP > 0 else f"index_{MAX_LEN}.json"

if __name__ == "__main__":
    chunks = load_chunks("data/tinyrag_readme.md", MAX_LEN, OVERLAP)
    index = build_index(chunks, SiliconFlowEmbedding())
    save_index(index, INDEX_PATH)