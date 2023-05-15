class SearchFilter:  # po co klasa, skoro ma tylko statyczne metody?
    def __init__(self):
        pass

    @staticmethod
    def filter_readers(readers_option, query):
        return list(filter(lambda x:
                           query in x.obj_instance.login.lower() or
                           query in x.obj_instance.first_name.lower() or
                           query in x.obj_instance.family_name.lower() or
                           query in x.obj_instance.library_card_number.lower(),
                           readers_option))

    @staticmethod
    def filter_books_by_title_and_author(books_option, query):
        return list(filter(lambda x: query in x.obj_instance.title.lower() or query in x.obj_instance.author.lower(),
                           books_option))

    @staticmethod
    def filter_borrowed_books(books_list):
        return list(filter(lambda x: x.is_borrowed is True and x.borrowed_by is not None,
                           books_list))

    @staticmethod
    def filter_borrowed_books_without_return_mark(books_list):
        return list(filter(lambda x: x.is_borrowed is True and x.borrowed_by is not None and x.to_return is False,
                           books_list))

    @staticmethod
    def filter_reserved_books(books_list):
        return list(filter(lambda x: x.is_reserved is True and x.reserved_by is not None,
                           books_list))

    @staticmethod
    def filter_awaiting_to_return_books(books_list):
        return list(filter(lambda x: x.to_return is True and x.is_borrowed is True and x.borrowed_by is not None,
                           books_list))
