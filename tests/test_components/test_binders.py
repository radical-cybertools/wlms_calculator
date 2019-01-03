from calculator.exceptions import *
from calculator.components.binders.temporal_binder import Temporal_Binder
from calculator.components.binders.spatial_binder import Spatial_Binder
import pytest

def test_binders_init():

    bind = Temporal_Binder()
    assert bind._uid.split('.')[0] == 'binder'
    assert bind._criteria_options == ['rr','tte','util','random']
    assert bind._criteria == None
    assert bind._schedule == None

    bind = Spatial_Binder()
    assert bind._uid.split('.')[0] == 'binder'
    assert bind._criteria_options == ['rr','tte','util','random']
    assert bind._criteria == None
    assert bind._schedule == None

def test_binders_bind():
    
    binder = Temporal_Binder()
    with pytest.raises(CalcValueError):
        binder.bind(workload=list(), resource=list(), submit_time=0)

    with pytest.raises(CalcValueError):
        binder.criteria = 'new'

    binder = Spatial_Binder()
    with pytest.raises(CalcValueError):
        binder.bind(workload=list(), resource=list())

    with pytest.raises(CalcValueError):
        binder.criteria = 'new'