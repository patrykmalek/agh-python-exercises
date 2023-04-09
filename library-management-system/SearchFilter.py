class SearchFilter:
    @staticmethod
    def filter_books_by_title_and_author(books_option, query):
        return list(filter(lambda x: query in x.obj_instance.title.lower() or query in x.obj_instance.author.lower(),
                           books_option))
