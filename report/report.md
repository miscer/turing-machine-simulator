% CS3052 Practical 1 Report
% 140015533
% 28 February 2017

# Overview

# Turing Machine Simulation

## Design

I have split the program into logical parts.

The first one is a tape. It can hold a (potentially) infinite number of cells and has read and write operations. Reading an empty cell succeeds, but an empty value is returned.

The head remembers its position on the tape and can move either left or right. If the head is at the first cell and it is moved left, it remains on the same cell.

Transitions are specified using a transition function. Transition function is created from a transition table.

Tape, head and transition function are used in a Turing machine. Each machine has a start, accept and reject state and a transition function.

The machine can be executed on an input. For each input it creates a new tape and head and remembers its current state. This means that the machine can be re-used for different inputs.

Parser reads a file that has the specified format for describing a Turing machine and produces a Turing machine. It verifies the machine definition as it is parsing it - it validates each row in the transition table.

## Implementation

## Testing

I have written unit tests for each part of the program, so I can be sure that the simulator works correctly and all edge cases are handled. This also forced me to separate the program into small, independent parts that can be tested easily.

All tests for the program can be found in the `source/turingmachine/test` directory.

# Solutions to Problems

## Palindromes

The Turing machine for recognising palindromes goes through the input from one side to the other comparing each half of the input with the other. It stops if there is a mismatch in one letter.

1. If there are no letters on the tape, accept.
2. Read a letter, remember it and mark it.
3. Go right until the end of the tape, or until a marked letter is found.
4. Go one cell left and check if the letter matches the remembered letter.
    1. If it does, mark it.
    2. If not, reject.
5. Go left until a marked letter is found.
6. Go one cell right and go back to 2.
7. Repeat while there are unmarked letters. If there are only marked letters, accept.

## Binary Addition

## Insertion Sort

## Substring

## Divisible by 4

# Analysis

I have created a number of series of inputs for each solution. The inputs in a series grow linearly and all have a common characteristic (e.g. all are palindromes). These series are generated procedurally using Python generators.

Then I let the machine run on first 100 inputs in each series and counted the number of transitions the machine makes for each input. The output of the analysis program is a CSV file, with a column for each series and a row for each analysed input.

For example, for the palindromes solution the output file begins like this:

```
n,input 0,input 1,input 2
0,4,4,3
1,5,5,6
2,6,6,10
3,7,7,15
4,8,8,21
5,9,9,28
```

The first column, `n` is the position of the analysed input in the series. The other numerical values are numbers of transitions.

## Palindromes

In the solution the machine needs to go back and forth through the tape for each letter in the first half of the input.

This means that if the input is a palindrome, the program has time complexity $O(n^2)$, as this is the worst case - the head needs to go through the whole tape twice ($2n$ transitions) for each letter in a half of the input ($\frac{n}{2}$ transitions). We can see this in Figure \ref{fig:palindromeworst}.

The best case is when the input is not a palindrome, and the first and last letters do not match. In this case the machine only goes through the whole tape once ($n$ transitions), resulting in $O(n)$ time complexity, as shown in Figure \ref{fig:palindromebest}.

The series of inputs used for measurements are:

* Input 0: ab, aab, aabb, aaabb, ...
* Input 1: ab, aab, aaab, aaaab, ...
* Input 2: a, aa, aaa, aaaa, ...

Inputs 0 and 1 are both not palindromes, and the first and last letters do not match, resulting in the $O(n)$ time complexity in Figure \ref{fig:palindromebest}.

Input 2 is a palindrome, which is the worst case for the algorithm.

![Best case for the palindrome TM \label{fig:palindromebest}](figures/palindrome-best.png){width=80%}

![Worst case for the palindrome TM \label{fig:palindromeworst}](figures/palindrome-worst.png){width=80%}

## Binary Addition

## Insertion Sort

## Substring

## Divisible by 4

# Conclusion
