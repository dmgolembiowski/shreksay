#!/bin/bash

cat refined_gen_wav_parallel.sh | parallel -j8 {}
