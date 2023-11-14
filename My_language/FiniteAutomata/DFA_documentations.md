# Deterministic Finite Automaton (DFA) Implementation



## Introduction

This Python implementation represents a Deterministic Finite Automaton (DFA) designed for recognizing specific patterns within sequences of symbols. The DFA is loaded from a file containing information about its states, alphabet, transitions, initial state, and final states.

## Usage

To use the DFA, an instance of the `DFA` class is created, which automatically loads its configuration from a specified input file. The input file format is as follows:


- **states**: Define the set of states in the DFA.
- **alphabet**: Specify the set of symbols in the alphabet.
- **transitions**: Describe transitions between states based on input symbols.
- **initial**: Designate the initial state.
- **final**: Specify the set of final (accepting) states.

## Methods

### `display_elements()`

Prints information about the DFA, including states, alphabet, transitions, initial state, and final states.

### `is_sequence_accepted(sequence)`

Determines whether a given sequence of symbols is accepted by the DFA.

### `is_identifier(token)`

Checks if a given token represents a valid identifier according to the DFA.

### `is_integer_constant(token)`

Verifies if a given token corresponds to a valid integer constant based on the DFA.

## Example

```python
dfa = DFA()
dfa.display_elements()

sequence = "abc"
if dfa.is_sequence_accepted(sequence):
    print(f"The sequence '{sequence}' is accepted by the DFA.")
else:
    print(f"The sequence '{sequence}' is not accepted by the DFA.")

token = "q2"
if dfa.is_identifier(token):
    print(f"The token '{token}' is a valid identifier.")
else:
    print(f"The token '{token}' is not a valid identifier.")
```