class SearchFilter:
    @staticmethod
    def filter_books_by_title_and_author(books_option, query):
        return list(filter(lambda x: query in x.obj_instance.title.lower() or query in x.obj_instance.author.lower(),
                           books_option))
    @staticmethod
    def filter_borrowed_books(books_list):
        return list(filter(lambda x: x.is_borrowed is True and x.borrowed_by is not None,
                           books_list))
    @staticmethod
    def filter_reserved_books(books_list):
        return list(filter(lambda x: x.is_reserved is True and x.reserved_by is not None,
                           books_list))
    @staticmethod
    def filter_awaiting_to_return_books(books_list):
        return list(filter(lambda x: x.to_return is True and x.is_borrowed is True and x.borrowed_by is not None,
                           books_list))
