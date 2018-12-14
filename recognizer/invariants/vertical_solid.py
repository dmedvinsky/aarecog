import logging
from typing import List
from itertools import groupby

from .base import BaseInvariant


logger = logging.getLogger(__name__)

SIGNATURES = {
    '1': {'H', 'I', 'J', 'L', 'M', 'N', 'T', 'U', 'V', 'W', 'Y'},
    '1,2': {'C', 'K'},
    '1,2,1': {'A', 'D', 'F', 'O', 'P', 'Q'},
    '1,3,2': {'E'},
    '2,1,2': {'X'},
    '2,3,2': {'S', 'Z'},
    '1,2,3,2': {'G', 'R'},
    '1,3,1,2': {'B'},
}


class VerticalSolid(BaseInvariant):
    """Invariant based on number of solid vertical blocks."""
    def suggest(self):
        # FIXME Optimize the laziest algo that came to my mind.
        transposed = _transpose(self.data)
        metric = _calculate(transposed)
        signature = ','.join(str(x) for x in metric)
        logger.debug('Got signature %s', signature)
        return SIGNATURES.get(signature, None)


def _transpose(data: str) -> str:
    lines = data.splitlines()
    max_width = max(len(x) for x in lines)
    padded_lines = [x.ljust(max_width) for x in lines]
    transposed_lines = [''.join([x[c] for x in padded_lines]) for c in range(max_width)]
    return '\n'.join(transposed_lines)


def _calculate(data: str) -> List[int]:
    lines = data.splitlines()
    # `str.split` splits by continuous whitespace blocks. We're lazy, so use it.
    segments = [len(x.split()) for x in lines]
    return [n for n, _ in groupby(segments, lambda x: x) if n > 0]
