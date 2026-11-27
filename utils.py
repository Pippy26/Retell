def load_chunks(path: str, max_len: int = 500, overlap : int=0) -> list[str]:
    text = read_markdown(path)
    result = split_blocks(text)
    chunks = merge_blocks(result, max_len, overlap)
    final_chunks = []
    for chunk in chunks:
        if len(chunk) > max_len:
            final_chunks.extend(split_long(chunk, max_len))
        else:
            final_chunks.append(chunk)
    return final_chunks


def read_markdown(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    keep_lines = [line for line in lines if not line.strip().startswith("![") and "手搓RAG直播" not in line.strip()]

    return "\n".join(keep_lines)


def split_blocks(text: str) -> list[str]:
    lines = text.splitlines()
    result = []
    current = []
    in_code = False

    for line in lines:

        if line.strip().startswith("```"):
            in_code = not in_code
            current.append(line)
            continue

        if not in_code and line.strip() == "":
            block = "\n".join(current)

            if block.strip() != "":
                result.append(block)
            current = []

        else:
            current.append(line)

    if current:
        block = "\n".join(current)

        if block.strip() != "":
            result.append(block)
    return result


def merge_blocks(blocks, max_len=500, overlap: int = 0) -> list[str]:
    chunks = []
    current = []
    for para in blocks:
        candidate = current + [para]
        candidate_text = "\n\n".join(candidate)
        if len(candidate_text) <= max_len:
            current.append(para)
        else:
            if current:
                chunks.append("\n\n".join(current))
            overlap_paras = []
            total = 0
            for p in reversed(current):
                add_len = len(p)
                if total + add_len > overlap:
                    break
                overlap_paras.insert(0, p)
                total += add_len
            new_candidate = overlap_paras + [para]
            new_text = "\n\n".join(new_candidate)
            if len(new_text) <= max_len:
                current = new_candidate
            else:
                current = [para]
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def split_long(chunk: str, max_len: int = 500) -> list[str]:
    result = []
    current = ""
    for line in chunk.splitlines():
        if len(line) > max_len:
            if current != "":
                result.append(current)
                current = ""
            for i in range(0, len(line), max_len):
                result.append(line[i:i+max_len])
            continue

        if current == "":
            current = current + line
        elif len(current) + len(line) <= max_len:
            current = current + "\n" + line
        else:
            result.append(current)
            current = line
    if current:
        result.append(current)
    return result

