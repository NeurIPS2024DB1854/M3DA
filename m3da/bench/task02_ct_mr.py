from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base
from ..utils import flatten


split_ct_mr = load_json(REPO_PATH / "splits/Task02_CT_MR.json")
dataset_ct_mr = amos_base >> Filter(lambda id: id in flatten(split_ct_mr))

labels_ct_mr = tuple(range(16))
background_lbl_ct_mr = 0
