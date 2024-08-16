from pathlib import Path

from .typing import OptPathLike


REPO_PATH = Path(__file__).parent

# Paths to raw datasets:
PATH_AMOS22_RAW: OptPathLike = Path("path/to/downloaded/amos22")
PATH_AMOS22_LDCT: OptPathLike = Path("path/to/downloaded/amos_ldct")
PATH_BRATS2021_RAW: OptPathLike = Path("path/to/downloaded/brats2021")
PATH_CC359_RAW: OptPathLike = Path("path/to/downloaded/cc359")
PATH_LIDC_RAW: OptPathLike = Path("path/to/downloaded/lidc")
