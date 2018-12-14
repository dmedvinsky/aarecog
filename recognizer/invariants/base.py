from typing import Set


class BaseInvariant:
    """Inherit custom invariants from this base."""
    def __init__(self, data: str):
        self.data = data

    def suggest(self) -> Set[str]:
        """Suggest possible letters."""
        raise NotImplementedError('Must override method in a child class.')
