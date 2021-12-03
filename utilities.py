from typing import List, Callable, Optional


def load_data_as_list(path: str, postprocess: Optional[Callable] = None) -> List:
    with open(path, "r") as f:
        l_iterable = filter(lambda x: len(x), f.read().split("\n"))

    if postprocess:
        l_iterable = map(postprocess, l_iterable)
    return list(l_iterable)
