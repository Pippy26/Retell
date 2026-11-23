from eval_set import EVAL_SET
from vector_store import load_index
from embeddings import SiliconFlowEmbedding
from rag import ask
from collections import Counter

index = load_index("index.json")
emb = SiliconFlowEmbedding()

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


def get_answer(question: str) -> str:
    reply, result = ask(question, index, emb)

    return reply


def run_eval(eval_set: list[dict]):
    fail_dict = {}
    pass_dict = {}
    total_right_number = 0
    for index in range(len(eval_set)):
        answer = get_answer(eval_set[index]['question'])
        try:
            if judge(eval_set[index], answer):
                print(f"[通过] {eval_set[index]['question']}")
                if eval_set[index]["category"] not in pass_dict:
                    pass_dict[eval_set[index]["category"]] = 1
                else:
                    pass_dict[eval_set[index]["category"]] += 1
                total_right_number += 1
            else:
                print(f"[不通过] {eval_set[index]['question']}")
                print(answer)
                if eval_set[index]["category"] not in fail_dict:
                    fail_dict[eval_set[index]["category"]] = 1
                else:
                    fail_dict[eval_set[index]["category"]] += 1

        except ValueError as e:
            print(f"题目出错了! {e}")

    total_dict = Counter(fail_dict) + Counter(pass_dict)
    for key, value in sorted(total_dict.items(), reverse=True):
        print(f"{key} 通过{pass_dict.get(key, 0)}/{value}")

    print(f"通过{total_right_number}/{len(eval_set)}")

if __name__ == "__main__":
    run_eval(EVAL_SET)