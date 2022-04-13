from abc import ABC


class GenericSearcher(ABC):
    def search(self, search_term, max_results):
        raise NotImplemented
