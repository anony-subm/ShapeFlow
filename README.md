# ShapeFlow

## Installation

1. Create a Python3 virtual environment.

2. source path-to-virtualenv/bin/activate

3. sudo apt install python3-dev python3-pip OR follow first 3 instructions from [Install TensorFlow from source](https://www.tensorflow.org/install/source) 

4. Install [Bazel](https://docs.bazel.build/versions/master/install.html). ShapeFlow was developed using Bazel version 0.10.0.

5. Run `./configure`

6. Run `install.sh` using your preferred shell.

## Structuring

``tensorflow`` directory contains the modified tensorflow code (shapeflow).

`Johirul_benchmarks` directory contains the benchmarks from Johirul et al.'s paper (FSE 2019).

`experiments` directory contains the timing results for all our benchmarks.
