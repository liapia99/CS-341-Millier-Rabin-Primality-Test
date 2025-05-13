# CS-341-Millier-Rabin-Primality-Test-Visualization 

This project creates an educational animation explaining the Miller-Rabin Primality Test, a probabilistic algorithm used to determine if a number is probably prime.

## Overview

The animation consists of several scenes that walk through:
- Introduction to the Miller-Rabin test
- Background mathematical concepts
- Step-by-step explanation of how the test works
- Practical examples
- Applications and efficiency analysis

## Prerequisites

- Python 3.x
- Manim library
- LaTeX (for mathematical expressions)

## Installation

1. Install Python dependencies:
```bash
pip install manim
```
(I have a Macbook but here's how you can install LaTeX):

2. Install LaTeX (if not already installed):
- For macOS: `brew install mactex`
- For Ubuntu: `sudo apt-get install texlive-full`
- For Windows: Install MiKTeX

## Project Structure

The animation is divided into the following scenes:

1. `TitleScene`: Introduction with title and authors
2. `WhatItDoesScene`: Overview of what the Miller-Rabin test does
3. `BackgroundScene`: Mathematical background including:
   - Fermat's Little Theorem
   - Carmichael Numbers
   - Euler Test
   - Euclid's Lemma
4. `HowItWorksScene`: Detailed explanation of the algorithm with examples:
   - Example with n = 341 (composite)
   - Example with n = 104513 (probably prime)
5. `UsefulnessScene`: Applications in cryptography and practical uses
6. `EfficiencyScene`: Analysis of time complexity and error probability

## Running the Animation

To render the animation:

```bash
python video.py
```

This will generate video files in the `media` directory.

## Mathematical Concepts Covered

1. **Fermat's Little Theorem**
   - Basic theorem and its implications
   - Examples with n = 4 and n = 7

2. **Carmichael Numbers**
   - Definition and examples
   - Limitations of Fermat's test

3. **Euler Test**
   - Square roots modulo n
   - Test procedure and examples

4. **Miller-Rabin Test**
   - Step-by-step algorithm
   - Time complexity: O(k log³ n)
   - Error probability: ≤ 4^(-k)

## Applications

The animation demonstrates how the Miller-Rabin test is used in:
- RSA key generation
- Diffie-Hellman key exchange
- ElGamal encryption
- Other cryptographic applications

## Authors

- Julia Piascik
- Bolen Alfreh

## License

This project is open source and available under the MIT License.

## Resources
Boneh, Dan. “Miller-Rabin Primality Test.” Stanford University: Crypto Notes, https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html. 
Conrad, Keith. The Miller-Rabin Primality Test. University of Connecticut, https://kconrad.math.uconn.edu/blurbs/ugradnumthy/millerrabin.pdf. 
GeeksforGeeks. “Euclid’s Lemma.” GeeksforGeeks, https://www.geeksforgeeks.org/euclids-lemma/. 
GeeksforGeeks. “Fermat’s Little Theorem.” GeeksforGeeks, https://www.geeksforgeeks.org/fermats-little-theorem/. 
GeeksforGeeks. “Primality Test | Set 3 (Miller–Rabin).” GeeksforGeeks, 12 Sept. 2023, https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/.
Hoffoss, Douglas. The Rabin-Miller Test. University of San Diego, https://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf. 
Sen, Gaurav. Miller-Rabin Primality Test – The Fastest Way to Check for Primes. YouTube, 11 Aug. 2020, https://www.youtube.com/watch?v=zmhUlVck3J0.
TutorialsPoint. “What Are the Miller Rabin Algorithm for Testing the Primality of a Given Number?” TutorialsPoint, https://www.tutorialspoint.com/what-are-the-miller-rabin-algorithm-for-testing-the-primality-of-a-given-number. 
