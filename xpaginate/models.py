from math import *
from django.template import Library, Node
from django import template
from django.template.loader import render_to_string
import traceback

class Xoptions():
    def __init__(self,uri=None,total_items=None,current=None,per_page=None,show=None,jump=None,range=None):
        self._uri=uri
        self._total_items=total_items
        self._current=current
        self._per_page=per_page
        self._show=show
        self._jump=jump
        self._range=range

class XPaginate:
    def __init__(self, page):
        self.total_items = int(page._total_items)
        self.current = int(page._current)
        self.per_page = int(page._per_page)
        self.show = int(page._show)
        self.jump = page._jump
        self.range = int(page._range)
        self.jump_calc = 2
        self.uri = page._uri

        if self.current is 0:
            self.current = 1

        # Total number of pages
        self.total_pages = int(ceil(float(self.total_items) / float(self.per_page)))

        if self.current is not 1:
            self.has_previous = True
        else:
            self.has_previous = False

        if self.current < self.total_pages:
            self.has_next = True
        else:
            self.has_next = False

        last_foward=self.total_pages
        # Get the first foward set of page links if avaliable
        self.foward_pages = []
        if self.has_next:
            a = self.current
            self.foward = int(self.current + 1)
            total = 0
            while total is not self.show:
                a = a + 1
                total = total + 1
                if a <= self.total_pages:
                    if total is self.show:
                        last_foward = a
                    self.foward_pages.append(a)
            if last_foward is self.total_pages or (last_foward + self.show) > self.total_pages:
                self.show_last = False
            else:
                self.show_last = True
            #print self.foward_pages, '\n'

        # GET the set of previous pages
        self.previous_pages = []
        if self.has_previous:
            self.previous = int(self.current - 1)
            a = int((self.current - 1) - self.show)
            total = 0
            while total is not self.show:
                a = a + 1
                total = total + 1
                if a <= self.total_pages and a is not 0:
                    if total is self.show:
                        last_previous = int(a)
                    self.previous_pages.append(a)

            #print self.previous_pages, '\n'

        # Calculate if we have the ability to jump foward pages
        if self.jump and (self.current - ceil(self.range * self.jump_calc)) >= 2:
            self.has_jump_previous = True
        else:
            self.has_jump_previous = False

        if self.jump and (self.current + ceil(self.range * self.jump_calc)) < self.total_pages:
            self.has_jump_foward = True
        else:
            self.has_jump_foward = False

        ## Calc Jump pages foward

        if self.has_jump_foward:
            a = last_foward
            total = 0
            self.foward_page_jump = []
            while total is not self.range:
                total = total + 1
                a = int(float(ceil(a * self.jump_calc)))
                if a <= self.total_pages:
                    self.foward_page_jump.append(a)

        if self.has_jump_previous:
            a = int(last_previous)
            total = 0
            self.previous_page_jump = []
            while total is not self.range:
                total = total + 1
                a = int(ceil(a / float(self.jump_calc)))
                if a <= self.total_pages and a >= 2:
                    self.previous_page_jump.insert(0, a)

class RenderXPage(Node):
    def __init__(self, page):
        self.page=template.Variable(page)

    def render(self, context):
        self.page = self.page.resolve(context)
        return render_to_string('templates/xpaginate/xpaginate.html', { 'xpaginate': XPaginate(self.page) })