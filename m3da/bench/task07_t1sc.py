from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.cc359 import cc359_base
from ..utils import flatten


split_t1sc = load_json(REPO_PATH / "splits/Task07_T1Sc.json")
dataset_t1sc = cc359_base >> Filter(lambda id: id in flatten(split_t1sc))

labels_t1sc = tuple(range(4))
background_lbl_t1sc = 0
