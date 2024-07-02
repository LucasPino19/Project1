"""
# Text Analysis Project

This project processes a text file named `entrada.txt` to perform specific text analysis tasks. The program evaluates sequences of characters and provides four different analytical results based on defined criteria.

## Features

The program reads the text from `entrada.txt` and performs the following analyses:

1. **Odd Digit and Non-uppercase Analysis**:
   - Counts sequences starting with an odd digit (1, 3, 5, 7, 9) and containing at least one non-uppercase letter.

2. **Longest Sequence Starting with a Vowel**:
   - Identifies the length of the longest sequence starting with a vowel (a, e, i, o, u) followed by at least one 'b' or 'B'.

3. **Consonants and Vowels Ratio**:
   - Computes the average length of sequences where the number of consonants exceeds the number of vowels, provided the sequence does not contain 'm' or 'M' and 'a', 'A', 'á', or 'Á'.

4. **Vowel Following 'd' or 'D'**:
   - Counts sequences containing at least two vowels immediately following a 'd' or 'D'.

## Usage

1. Place your input text file named `entrada.txt` in the same directory as the script.
2. Run the script:
   ```python
   python element1.py
## Example
If entrada.txt contains the text:
```vbnet
Example text with various sequences.
```
The output might look like:
```sql
First result: 2
Second result: 5
Third result: 3
Fourth result: 1
```
## Functions
-`es-letra(car)`: Checks if a letter is a letter

-`es_vocal(car)`: Checks if a character is a vowel.

-`es_consonante(car)`: Checks if a character is a consonant.

-`test()`: Main function that performs the text analysis.
