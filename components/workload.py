import radical.utils as ru
import numpy as np
from task import Task

class Workload(object):

    def __init__(self, size=0, dist=None, value=None, var=None):

        # Initialize
        self._uid = ru.generate_id('workload.%(item_counter)04d', ru.ID_CUSTOM)
        self._dist_candidates = [None, 'uniform', 'normal']
        self._workload = list()    # Empty list of execution units

        self._size = size
        if dist not in self._dist_candidates:
            raise ValueError("possible distributions are %s" %
                             (','.join(self._dist_candidates)))

        # User specified distribution, value, and variation
        self._dist = dist
        self._value = value
        self._var = var

        if self._size:
            self._create_workload()

    @property
    def size(self):
        return self._size

    @property
    def workload(self):
        return self._workload

    def _create_workload(self):

        # Select N samples from the selected distribution
        if self._dist == None:
            self._samples = [self._value for _ in range(self._size)]
        elif self._dist == 'uniform':
            self._samples = np.random.uniform(low=self._value - self._var,
                                              high=self._value + self._var,
                                              size=self._size)
        elif self._dist == 'normal':
            self._samples = [self._value*np.random.randn()+self._var for _ in range(self._size)]

        # Create N tasks with the selected samples
        self._workload = [Task(self._samples[i]) for i in range(self._size)]
