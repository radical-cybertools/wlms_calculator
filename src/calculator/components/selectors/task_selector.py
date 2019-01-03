import radical.utils as ru
from ..algorithms.selection_algos import select_all
from ...exceptions import CalcValueError


class Task_Selector(object):

    def __init__(self):

        self._uid = ru.generate_id('selector.%(item_counter)04d', ru.ID_CUSTOM)
        self._criteria_options = ['all']
        self._criteria = None

    @property
    def criteria(self):
        return self._criteria

    @criteria.setter
    def criteria(self, val):
        if val not in self._criteria_options:
            raise CalcValueError(obj=self._uid, attribute='criteria',
                                 expected_value=self._criteria_options,
                                 actual_value=val)
        self._criteria = val

    def select(self, collection, count):

        if not self._criteria:
            raise CalcValueError(obj=self._uid, attribute='criteria',
                                 expected_value=self._criteria_options,
                                 actual_value=None)

        if self._criteria == 'all':
            return select_all(collection, count)
