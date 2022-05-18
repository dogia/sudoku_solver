# Sudoku Solver [![Awesome](https://awesome.re/badge.svg)](https://github.com/dogia)

Sudoku solver is a opensource project based in backtraking, it makes the solver very fast because it verify the consistency of a brench before exploring it.

## Installation
* For installation, make sure you have installed Python in version >= 3.9 from [python 3](https://www.python.org/)

* Copy the repo
```bash
git clone https://github.com/dogia/sudoku_solver.git
```


## Usage
change main.py:

```python
sudoku = init()
sudoku = load(sudoku, "yourfilename.txt")
solve(sudoku)
```

```bash
py main.py
```

OR 

```bash
python3 main.py
```

# File in TXT format
The file in .txt format shoud contain 1 digit of sudoku for line reading left-right and top-buttom
use 0 for empty cells in board.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) [2022] [Daniel Osorio Orozco]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
