# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Local application imports
from mosqito.functions.hearing_model.sine_wave_generator import sine_wave_generator
from mosqito.functions.hearing_model.segmentation_blocks import segmentation_blocks

signal, _ = sine_wave_generator(
    fs=48000,
    t=1,
    spl_value=60,
    freq=40,
)
blocks = segmentation_blocks(signal, 8192, 2048, 1)

plt.subplot(211)
plt.plot(signal)
plt.subplot(212)
plt.plot(blocks[0], label="block 1")
plt.plot(blocks[1], label="block 2")
plt.plot(blocks[2], label="block 3")
plt.legend()
plt.show()