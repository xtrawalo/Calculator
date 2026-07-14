<h1 align="center">Double Calculator in Python</h1>
<p align="center">
<img src="asset.png">
</p>

## Table of content

- [How it works](#how-it-works)
  - [Left-to-right calculator](#left-to-right-calculator)
  - [Precedence-aware calculator](#precedence-aware-calculator)
- [Built With](#built-with)
- [Installation](#installation)
- [AI Usage](#ai-usage)
- [Author](#author)

## How it works

First, the program defines the required variables (`Numbers`, `Operators`, and `solution`). Next, the user is asked to select which calculator should be used. The program executes until the user decides to exit.

### Left-to-right calculator

The program asks the user to input numbers and operators gradually. At the same time, each operation is performed right away. Thus, `2 + 3 * 4 = (2 + 3) * 4`. After performing each step, the user can either continue, go back to the start, or exit the program.

### Precedence-aware calculator

At first, all the numbers and operators that were entered by the user are stored. Later, the operations are performed according to the rules of order of operations by substituting subtraction with addition, division with multiplication, executing all multiplication operations, and adding all other numbers. Therefore, `2 + 3 * 4 = 2 + (3 * 4)`. After the result is printed, the user can restart or exit the program.

## Built With

- Python

## Installation

To Download it, check the latest Windows version from the **Releases** page.

Here → https://github.com/xtrawalo/Calculator/releases/latest

View the project on **Horizons** : https://horizons.hackclub.com/projects/5501

## AI USAGE

This project is my own work. I used Claude only for debugging.

## Author

Me : [xtrawalo](https://github.com/xtrawalo)
