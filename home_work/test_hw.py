def test_hwa():
    assert ('home', 'work') == ('home', 'work')

def test_hwb():
   assert ('QA') != ('QC')

def test_hwc():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)


