# ConwaysGoLEncoder

Have you ever wondered what would happen if **Conway's Game of Life** was used for data encryption? Me neither, yet here we are.

## Overview

**ConwaysGoLEncoder** is a completely unnecessary tool that combines text encrypting with **Conway's Game of Life**. It takes your text, converts it to binary, runs it through several iterations of the **Game of Life**, and then decodes it back into text.

The idea behind this project is that while it is simple to apply **GoL's** rules to some starting position of the cells, it is extremely difficult to reconstruct this starting position after several iterations of **Game of Life**.

## Features

- Your input sentence is transformed into a 2D array of 1s and 0s.
- The binary array evolves through 10 generations of **Conway’s Game of Life**.
- The resulting binary array is translated back into **Unicode** characters.

## How to Run

1. Run _Encoder.py_

2. Enter a sentence when prompted.

## Limitations

1. Sometimes all cells die due to underpopulation/overpopulation, setting all of the letters to "0000000000000000".
2. One encoding can correspond to a multitude of different strings.

## Disclaimer

This project was made purely for fun and has no practical use. Don't try to encrypt any private data this way. Use **SHA** instead.

