import os
from common import *

name = os.path.basename(__file__)[5:-3]

run_quast(name, contigs=[contigs_1k_2], params='-1 ' + reads_1)
assert_metric(name, '# reads', ['56320'])