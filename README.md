# spans

[![Build Status](https://travis-ci.org/AaronRobson/spans.svg?branch=master)](https://travis-ci.org/AaronRobson/spans)
[![CircleCI](https://circleci.com/gh/AaronRobson/spans.svg?style=svg)](https://circleci.com/gh/AaronRobson/spans)
[![Coverage Status](https://coveralls.io/repos/github/AaronRobson/spans/badge.svg?branch=master)](https://coveralls.io/github/AaronRobson/spans?branch=master)

## Getting started

This program is designed to print out a list of numbers with any ranges
simplified out.
For instance you could ask your printer to print the first 5 pages of
a document like this:
`1,2,3,4,5`
or like this:
`1-5`

## Download

```sh
git clone https://github.com/AaronRobson/spans.git
cd spans
```

## Install python packages

```sh
make install-packages
```

## Lint

```sh
make check
```

## Test

```sh
make test
```

## Running

## Via Make

```sh
make run args="1 2 3 5-7 10"
```

### Directly

```sh
python3 spans.py 1 2 3 5-7 10
```

### Expected result

Either of the two forms should return:

```sh
1-3, 5-7, 10
```
