# spans
[![Build Status](https://travis-ci.org/AaronRobson/spans.svg?branch=master)](https://travis-ci.org/AaronRobson/spans)
[![CircleCI](https://circleci.com/gh/AaronRobson/spans.svg?style=svg)](https://circleci.com/gh/AaronRobson/spans)
[![Coverage Status](https://coveralls.io/repos/github/AaronRobson/spans/badge.svg?branch=master)](https://coveralls.io/github/AaronRobson/spans?branch=master)

# Getting started
This program is designed to print out a list of numbers with any ranges
simplified out.
For instance you could ask your printer to print the first 5 pages of
a document like this:
`1,2,3,4,5`
or like this:
`1-5`

# Download
```bash
git clone https://github.com/AaronRobson/spans.git
cd spans
```

# Install python packages
```bash
make install-packages
```

# Lint
```bash
make check
```

# Test
```bash
make test
```

# Running

## Via Make
```bash
make run args="1 2 3 5-7 10"
```

## Directly
```bash
python3 spans.py 1 2 3 5-7 10
```

## Expected result
Either of the two forms should return:
```bash
1-3, 5-7, 10
```
