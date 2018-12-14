import logging
from typing import List
from itertools import groupby

from .base import BaseInvariant


logger = logging.getLogger(__name__)

SIGNATURES = {
    '1': {'E', 'F', 'I', 'L', 'S', 'T', 'Z'},
    '2,1': {'U', 'V', 'Y'},
    '1,2,1': {'D', 'G', 'J', 'O', 'P'},
    '1,2,3': {'Q'},
    '2,1,2': {'H', 'K', 'X'},
    '2,3,2': {'N'},
    '3,4,2': {'W'},
    '1,2,1,2': {'A', 'R', 'S'},
    '2,4,3,2': {'M'},
    '1,2,1,2,1': {'B', 'C', 'G'},
}


class HorizontalSolid(BaseInvariant):
    """Invariant based on number of solid horizontal blocks."""
    def suggest(self):
        metric = _calculate(self.data)
        signature = ','.join(str(x) for x in metric)
        logger.debug('Got signature %s', signature)
        return SIGNATURES.get(signature, None)


def _calculate(data: str) -> List[int]:
    lines = data.splitlines()
    # str.split splits by continuous whitespace blocks. We're lazy, so use it.
    segments = [len(x.split()) for x in lines]
    return [n for n, _ in groupby(segments, lambda x: x) if n > 0]
