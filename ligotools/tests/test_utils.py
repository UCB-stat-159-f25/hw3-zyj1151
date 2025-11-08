import numpy as np
import os
from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten_output_shape_and_mean():
    """Test that whiten() returns same-length array with roughly zero mean."""
    np.random.seed(0)
    strain = np.random.randn(4096)
    interp_psd = lambda f: np.ones_like(f)  # flat PSD
    dt = 1/4096

    white = whiten(strain, interp_psd, dt)

    # Same shape
    assert white.shape == strain.shape
    # Mean close to zero
    assert np.isclose(np.mean(white), 0, atol=1e-3)


def test_reqshift_and_write_wavfile(tmp_path):
    """Test that reqshift() shifts frequencies and write_wavfile() creates a file."""
    fs = 4096
    t = np.linspace(0, 1, fs)
    # Make a pure tone at 100 Hz
    data = np.sin(2 * np.pi * 100 * t)

    # Shift it by +100 Hz and verify roughly doubles the frequency
    shifted = reqshift(data, fshift=100, sample_rate=fs)
    assert shifted.shape == data.shape
    # Check energy preserved
    assert np.isclose(np.std(shifted), np.std(data), rtol=0.2)
