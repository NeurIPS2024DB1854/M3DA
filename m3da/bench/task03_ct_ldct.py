from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base, CTNoise
from ..utils import flatten


split_ct_ldct = load_json(REPO_PATH / "splits/Task03_CT_LDCT.json")
dataset_ct_ldct = amos_base >> Filter(lambda id: id in flatten(split_ct_ldct)) >> CTNoise()

labels_ct_ldct = tuple(range(16))
background_lbl_ct_ldct = 0
