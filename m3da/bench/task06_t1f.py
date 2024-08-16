from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.cc359 import cc359_base
from ..utils import flatten


split_t1f = load_json(REPO_PATH / "splits/Task06_T1F.json")
dataset_t1f = cc359_base >> Filter(lambda id: id in flatten(split_t1f))

labels_t1f = tuple(range(4))
background_lbl_t1f = 0
