from django.core.paginator import Paginator

from .const_nums import POSTS_COUNT


def get_paginator(request, queryset,
                  number_of_pages=POSTS_COUNT):
    paginator = Paginator(queryset, number_of_pages)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
