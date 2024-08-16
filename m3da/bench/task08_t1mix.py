from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.cc359 import cc359_base
from ..utils import flatten


split_t1mix = load_json(REPO_PATH / "splits/Task08_T1Mix.json")
dataset_t1mix = cc359_base >> Filter(lambda id: id in flatten(split_t1mix))

labels_t1mix = tuple(range(4))
background_lbl_t1mix = 0
