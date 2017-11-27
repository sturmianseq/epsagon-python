"""General constants"""

import os

__version_info__ = ('0', '1', '1')
__version__ = '.'.join(__version_info__)

TC_REGIONS = [
    'us-east-1',
]

DEFAULT_REGION = 'us-east-1'
REGION = os.environ.get('AWS_REGION', DEFAULT_REGION)
if REGION not in TC_REGIONS:
    REGION = DEFAULT_REGION

TRACE_COLLECTOR_STREAM = 'tc.{0}'.format(REGION)
COLD_START = True
