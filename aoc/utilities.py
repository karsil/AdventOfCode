from pathlib import Path
from typing import List, Callable, Optional, Union


def load_data_as_list(path: Union[str, Path], postprocess: Optional[Callable] = None) -> List:
    with open(path, "r") as f:
        l_iterable = filter(lambda x: len(x), f.read().split("\n"))

    if postprocess:
        l_iterable = map(postprocess, l_iterable)
    return list(l_iterable)
