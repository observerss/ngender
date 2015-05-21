#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

__all__ = ['guess']


def py2compat(name):
    try:
        name = name.decode('utf-8')
    except:
        pass
    return name


class Guesser(object):
    def __init__(self):
        self._load_model()

    def _load_model(self):
        self.male_total = 0
        self.female_total = 0
        self.freq = {}

        with open(os.path.join(os.path.dirname(__file__), 'charfreq.csv')) as f:
            # skip first line
            next(f)
            for line in f:
                char, male, female = line.split(',')
                char = py2compat(char)
                self.male_total += int(male)
                self.female_total += int(female)
                self.freq[char] = (int(male), int(female))

        self.total = self.male_total + self.female_total

        for char in self.freq:
            male, female = self.freq[char]
            self.freq[char] = (1. * male / self.male_total,
                               1. * female / self.female_total)

    def guess(self, name):
        name = py2compat(name)
        firstname = name[1:]
        for char in firstname:
            assert u'\u4e00' <= char <= u'\u9fa0', u'姓名必须为中文'

        pm = self.prob_for_gender(firstname, 0)
        pf = self.prob_for_gender(firstname, 1)
        if pm > pf:
            return ('male', 1. * pm / (pm + pf))
        elif pm < pf:
            return ('female', 1. * pf / (pm + pf))
        else:
            return ('unknown', 0)

    def prob_for_gender(self, firstname, gender=0):
        p = 1. * self.male_total / self.total \
            if gender == 0 \
            else 1. * self.female_total / self.total

        for char in firstname:
            p *= self.freq.get(char, (0, 0))[gender]

        return p


guesser = Guesser()


def guess(name):
    return guesser.guess(name)
