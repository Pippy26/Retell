EVAL_SET = [
    {
        "question": "最小RAG应该包含哪些内容",
        "type": "must_include",
        "keywords": ["向量化模块", "数据库", "文档加载和切分模块", "向量检索", "大模型模块"],
        "category": "completely_relevant"
    },
    {
        "question": "今天天气怎么样",
        "type": "must_include",
        "keywords": ["资料里没有相关内容"],
        "category": "completely_irrelevant",
    },
    {
        "question": "教程里提到的成熟数据库是什么",
        "type": "must_not_include",
        "keywords": ["Milvus", "Pinecone", "Qdrant", "Chroma", "Faiss"],
        "category": "somewhat_relevant",
    },
]