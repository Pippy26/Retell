from eval_set import EVAL_SET

def contains_all(test_string: str, key_word_list: list[str]) -> bool:
    if key_word_list:
        for item in key_word_list:
            if item not in test_string:
                return False
        return True
    else:
        raise ValueError("用户忘记填写关键词!")

def judge(question: dict, answer: str) -> bool:
    if question["type"] == "must_include":
        if contains_all(answer, question["keywords"]):
            return True
        return False

    elif question["type"] == "must_not_include":
        if [item for item in question["keywords"] if item in answer]:
            return False
        return True

    else:
        raise ValueError(f"{question['question']}这条问题的type类型写错了,错误信息:{question['type']}")

if __name__ == "__main__":
    # print(judge({"question": "x", "type": "must_not_includ", "keywords": ["a"]}, "a"))
    print(judge(EVAL_SET[0], "需要向量化模块、数据库、文档加载和切分模块、向量检索、大模型模块"))
    print(judge(EVAL_SET[0], "需要向量化模块和大模型模块"))
    print(judge(EVAL_SET[2], "教程没有使用成熟的数据库，而是用 Numpy 自己实现"))
    print(judge(EVAL_SET[2], "教程用的是 Chroma"))







