# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class QuickHandler(object):

    def __init__(self,snippets, queryset, fourteen_qset):
        self.snippets=snippets
        self.queryset=queryset
        self.fourteen_qset=fourteen_qset
        print(self.fourteen_qset)
        print('*'*60)
        print(self.queryset)
        print('*' * 60)
        print(self.fourteen_qset)


    def process_data(self):
        pass