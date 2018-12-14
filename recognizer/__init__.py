import logging
from typing import Optional, List, Set

from . import invariants
from .invariants import BaseInvariant


logger = logging.getLogger(__name__)


class Recognizer:
    """ASCII Art recognizer."""
    default_invariants = [
        invariants.HorizontalSolid,
        invariants.VerticalSolid,
    ]

    def __init__(self, invariants: Optional[List[BaseInvariant]] = None):
        if invariants is None:
            self.invariants = self.default_invariants

    def get_suggestions(self, data: str) -> List[Set[str]]:
        """
        Try to recognize the given data and return suggestions from all
        modules.
        """
        suggestions = [x(data).suggest() for x in self.invariants]
        logger.info('Possible suggestions %s', suggestions)
        return suggestions

    def recognize(self, data: str) -> Set[str]:
        """
        Try to recognize the input data and return probable result.
        """
        suggestions = self.get_suggestions(data)
        return set.intersection(*suggestions)
