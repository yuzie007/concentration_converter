from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from collections import OrderedDict
import numpy as np
from mendeleev import get_all_elements


class ConcentrationConverter(object):
    _element_data = OrderedDict(
        (e.symbol, e.atomic_weight) for e in get_all_elements())

    def __init__(self):
        self._symbols = None
        self._concentrations_at = None
        self._concentrations_wt = None

    def run(self, symbols, concentrations, mode):
        data = self._element_data

        if mode == 'at2wt':
            concentrations_at = concentrations
            concentrations_wt = [
                c * data[s] for s, c in zip(symbols, concentrations)]
        elif mode == 'wt2at':
            concentrations_wt = concentrations
            concentrations_at = [
                c / data[s] for s, c in zip(symbols, concentrations)]
        else:
            raise ValueError('Invalid mode:', mode)

        self._symbols = symbols
        self._concentrations_at = self._normalize(concentrations_at)
        self._concentrations_wt = self._normalize(concentrations_wt)

    @staticmethod
    def _normalize(concentrations):
        return np.array(concentrations) / sum(concentrations) * 100

    def write(self, mode):
        if mode == 'at':
            weights = self._concentrations_at
        elif mode == 'wt':
            weights = self._concentrations_wt
        else:
            raise ValueError('Invalid mode:', mode)

        for symbol in self._symbols:
            print('{:16s}'.format(symbol), end='')
        print()
        for weight in weights:
            print('{:16.9f}'.format(weight), end='')
        print()

    def get_symbols(self):
        return self._symbols

    def get_concentrations_at(self):
        return self._concentrations_at

    def get_concentrations_wt(self):
        return self._concentrations_wt
