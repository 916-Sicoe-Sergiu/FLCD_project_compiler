# SymTable Class

The `SymTable` class represents a symbol table, which is a data structure used to store and manage a collection of unique elements. It's implemented as a hash table with separate chaining to handle collisions. The class contains methods for adding, finding, and removing elements, as well as various other operations related to the symbol table.

## Class Constants

- `SIZE`: A constant that determines the initial capacity of the symbol table.
- `NULL`: A constant representing an invalid or non-existent value in the symbol table.

## Constructor

The class constructor initializes an instance of the symbol table with the given capacity (`SIZE`). It sets the size of the symbol table (`__size`) to 0 and creates an empty data structure to hold the elements.

## Public Methods

- `hash(self, value)`: Calculates a hash value for a given input value based on the ASCII values of its characters.
- `add(self, elem)`: Inserts an element into the symbol table. It calculates the hash of the element's value and handles collisions using separate chaining.
- `find(self, elem)`: Locates an element within the symbol table.
- `remove(self, elem)`: Removes an element from the symbol table.
- `size(self)`: Returns the current size of the symbol table.
- `is_empty(self)`: Checks whether the symbol table is empty.
- `get_all(self)`: Returns the entire data structure containing the elements of the symbol table, including empty buckets.
- `get_as_list(self)`: Converts the symbol table into a list format, where each element is represented as a pair containing its position and value within the table.
- `__str__(self)`: Provides a string representation of the symbol table, displaying the position and value of each element.

## PifStructure Class

`PifStructure` is a class for managing a list of token-index pairs.

### Attributes:

- `__data (list)`: A list to store token-index pairs.

### Methods:

- `__init__()`: Initializes an empty `PifStructure`.
- `__len__()`: Returns the number of token-index pairs in the `PifStructure`.
- `__getitem__(item)`: Retrieves a token-index pair by index.
- `add(token, index)`: Adds a token-index pair to the `PifStructure`.
- `__str__()`: Returns a formatted string representation of the `PifStructure`.

## Scan Function

Scans the program text and populates the PIF and symbol table.

This method iterates through the lines of the program text, tokenizes them, and classifies tokens into program symbols, identifiers, and constants. It adds them to the PIF and symbol table accordingly. If a lexical error is encountered, it records the error message.

### Regular Expressions Explained:

- `re.match(r'[a-zA-Z]+', token)`: Checks if 'token' consists of one or more alphabetical characters.
- `re.match(r'\d+|[a-zA-Z]+', token)`: Checks if 'token' is either a sequence of one or more digits or a sequence of one or more alphabetical characters.

## Scanner Class

`Scanner` is a class responsible for lexical analysis of a program text, dividing it into tokens and managing the Program Internal Form (PIF) and Symbol Table (ST).

### Attributes:

- `__symbol_table (SymTable)`: An instance of the Symbol Table to store identifiers.
- `__pif (PifStructure)`: An instance of the Program Internal Form (PIF) to store token-index pairs.
- `__program_text (list[str])`: A list containing the lines of the input program text.
- `__program_symbols (list[str])`: A list of predefined program symbols.

### Methods:

- `__init__(program_path: str)`: Initializes a `Scanner` object with the provided program path, setting up the scanner for lexical analysis.
- `__scan()`: Scans the program text, identifies tokens, and populates the PIF and symbol table.
- `divide_in_tokens(program: str) -> list[str]`: Divides a given program string into a list of tokens based on specific lexical rules.
- `write_to_file_st_pif(error: str)`: Writes the Symbol Table (ST) and Program Internal Form (PIF) to output files.
# DFA Class

The `DFA` class represents a Deterministic Finite Automaton. It loads the DFA elements from a file and provides methods to display its elements, check if a sequence is accepted, and determine if a token is an identifier or an integer constant.

## Constructor

- `__init__(self)`: Initializes the DFA by loading elements from a file using `load_from_file()`.

## Methods

- `load_from_file(self)`: Loads DFA elements (states, alphabet, transitions, initial state, final states) from a specified file.
- `display_elements(self)`: Displays the states, alphabet, transitions, initial state, and final states of the DFA.
- `is_sequence_accepted(self, sequence)`: Checks if a given sequence is accepted by the DFA.
- `is_identifier(self, token)`: Checks if a given token is an identifier according to the DFA.
- `is_integer_constant(self, token)`: Checks if a given token is an integer constant according to the DFA.

# ProductionRule Class

The `ProductionRule` class represents a production rule in a context-free grammar.

## Constructor

- `__init__(self, left, right)`: Initializes a production rule with a left-hand side (non-terminal) and right-hand side (sequence of symbols).

# Grammar Class

The `Grammar` class represents a context-free grammar. It loads the grammar from a file and provides methods to print non-terminals, terminals, productions, and productions for a specific non-terminal.

## Constructor

- `__init__(self)`: Initializes the Grammar by loading elements from a specified file using `load_from_file()`.

## Methods

- `load_from_file(self)`: Loads grammar elements (non-terminals, terminals, productions) from a specified file.
- `parse_production(self, production_str)`: Parses a production rule from a string and adds it to the grammar.
- `print_non_terminals(self)`: Prints the non-terminals of the grammar.
- `print_terminals(self)`: Prints the terminals of the grammar.
- `print_productions(self)`: Prints all productions of the grammar.
- `print_productions_for_non_terminal(self, non_terminal)`: Prints productions for a specific non-terminal.
- `cfg_check(self)`: Checks if the grammar is in Chomsky Normal Form (CNF).

# Parser Class

The `Parser` class is responsible for building the FIRST sets for each non-terminal in a given grammar.

## Constructor

- `__init__(self)`: Initializes the Parser with a Grammar instance and an empty dictionary for FIRST sets.

## Methods

- `build_first_sets(self)`: Builds the FIRST sets for each non-terminal in the grammar.
