from collections.abc import Collection
# ---- 事实类：答案就在教程里 ----
EVAL_SET =[
    {
        "question": "RAG 的全称是什么，它是用来解决什么问题的",
        "type": "must_include",
        "keywords": ["检索增强生成", "幻觉"],
        "category": "completely_relevant"
    },
    {
        "question": "教程里建议切分文档时以什么为单位",
        "type": "must_include",
        "keywords": ["以句子为单位"],
        "category": "completely_relevant"
    },
    {
        "question": "教程里向量检索用的是哪种相似度计算方法",
        "type": "must_include",
        "keywords": ["余弦相似度"],
        "category": "completely_relevant"
    },
    {
        "question": "教程 Demo 里切分文本块的默认参数是多少",
        "type": "must_include",
        "keywords": ["600", "150"],
        "category": "completely_relevant"
    },
    {
        "question": "教程 Demo 里向量数据持久化保存在哪里",
        "type": "must_include",
        "keywords": ["storage"],
        "category": "completely_relevant"
    },
    {
        "question": "教程的 Embedding 代码里，默认使用的具体模型名称是什么",
        "type": "must_include",
        "keywords": ["text-embedding-3-large"],
        "category": "completely_relevant"
    },
    # ---- 跨 chunk 类：答案要拼几处内容 ----
    {
        "question": "教程里提到的 Embedding 模型有哪些",
        "type": "must_include",
        "keywords": ["JinaEmbedding", "ZhipuEmbedding", "OpenAI"],
        "category": "cross_chunk"
    },
    {
        "question": "RAG 是怎么减少大模型幻觉的",
        "type": "must_include",
        "keywords": ["文档数据库", "检索"],
        "category": "cross_chunk"
    },
    # ---- 陷阱类：别把教程里提到的东西当成系统实际用的 ----
    {
        "question": "这个 RAG 系统用的是哪个成熟向量数据库",
        "type": "must_not_include",
        "keywords": ["Milvus", "Pinecone", "Qdrant", "Chroma", "Faiss", "Weaviate"],
        "category": "somewhat_relevant"
    },
    # ---- 完全无关类：应该拒绝回答 ----
    {
        "question": "怎么用 Python 写一个贪吃蛇游戏",
        "type": "must_include",
        "keywords": ["资料里没有相关内容"],
        "category": "completely_irrelevant"
    }

]