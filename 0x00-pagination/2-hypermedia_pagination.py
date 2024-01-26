#!/usr/bin/env python3

"""a function named index_range that takes
two integer arguments page and page_size"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """new get page method"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)

        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """get_hyper method"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    @staticmethod
    def index_range(page, page_size):
        """function definition"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
