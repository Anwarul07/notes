from rest_framework.pagination import PageNumberPagination


class Pagespn(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "records"
    last_page_strings = ["end"]
    max_page_size = 7
