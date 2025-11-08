import numpy as np
from ligotools.readligo import dq_channel_to_seglist


def test_single_contiguous_segment():
    """
    If the DQ channel is all ones, we should get one segment
    covering the entire array length * fs.
    """
    dq = np.ones(5, dtype=int)
    fs = 4  # arbitrary sampling rate

    segs = dq_channel_to_seglist(dq, fs=fs)

    # Expect one slice from 0 to len(dq)*fs = 20
    assert len(segs) == 1
    assert segs[0].start == 0
    assert segs[0].stop == len(dq) * fs


def test_multiple_segments():
    """
    Check that disjoint active regions are returned as separate slices.
    """
    # Active in [1,3) and [5,6)
    dq = np.array([0, 1, 1, 0, 0, 1, 0], dtype=int)
    fs = 2

    segs = dq_channel_to_seglist(dq, fs=fs)

    # Expect 2 segments:
    #   indices [1,3) -> samples [2,6)
    #   indices [5,6) -> samples [10,12)
    assert len(segs) == 2
    assert segs[0].start == 2 and segs[0].stop == 6
    assert segs[1].start == 10 and segs[1].stop == 12
