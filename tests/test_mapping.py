import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from synesthesia import sensors, mapping


def test_mapping_step_runs():
    sns = sensors.default_sensors()
    m = mapping.Mapping(sns)
    called = {}

    def cb(val):
        called['v'] = val

    m.link('accelerometer', mapping.Action(cb))
    m.step()
    assert 'v' in called
