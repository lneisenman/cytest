# -*- coding: utf-8 -*-
import cytest
import cytest.fubar as cf
import cytest.snafu as cs


def test_top():
    res = cytest.top()
    assert res == 'top'


def test_fubar():
    res = cf.fubar()
    assert res == 'fubar'


def test_hello():
    res = cf.hello()
    assert res == 42.0


def test_snafu():
    res = cs.snafu_fcn()
    assert res == 'snafu'
