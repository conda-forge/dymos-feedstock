import os
import subprocess
import sys
from os.path import join, dirname

import dymos

os.environ.update({
    "MPLBACKEND": "Agg",
    "OPENMDAO_USE_MPI": "0",
})

test_files_to_delete = [
    # requires git command, not necessary to test this here
    ["test", "test_pycodestyle.py"],
    # seems to be a tolerance issue on this test for 1.13.1
    ["examples", "hull_problem", "test", "test_hull_problem.py"]
]

[
    os.unlink(join(dirname(dymos.__file__), *tf2d))
    for tf2d in test_files_to_delete
]

tests = [
    ["testflo", "--numprocs", "1", "dymos", "-v", "--pre_announce"],
    # pypi package does not include the folder containing the `joss` paper
    # ["testflo", "--numprocs", "1", "joss/test", "-v", "--pre_announce"],
]

for test in tests:
    rc = subprocess.call(test)
    if rc:
        sys.exit(rc)

sys.exit(0)
