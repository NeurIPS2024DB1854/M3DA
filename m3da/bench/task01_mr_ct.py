from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base
from ..utils import flatten


split_mr_ct = load_json(REPO_PATH / "splits/Task01_MR_CT.json")
dataset_mr_ct = amos_base >> Filter(lambda id: id in flatten(split_mr_ct))

labels_mr_ct = tuple(range(16))
background_lbl_mr_ct = 0
