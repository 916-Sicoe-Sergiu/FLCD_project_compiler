class ProductionRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Grammar:
    def __init__(self):
        self.non_terminals = set()
        self.terminals = set()
        self.productions = []

        self.load_from_file()

    def load_from_file(self):
        with open("D:\Semester V\FLCD\FLCD_project_compiler\My_language\parser\grammar.txt") as file:

            self.non_terminals = set(next(file).strip().split())
            self.terminals = set(next(file).strip().split())

            for line in file:
                line = line.strip()
                if line:
                    self.parse_production(line)

    def parse_production(self, production_str):
        left, right = production_str.split("->")
        left = left.strip()
        right = [symbol.strip() for symbol in right.split()]

        self.productions.append(ProductionRule(left, right))

    def print_non_terminals(self):
        print("Non-terminals:", *self.non_terminals)

    def print_terminals(self):
        print("Terminals:", *self.terminals)

    def print_productions(self):
        for production in self.productions:
            print(f"{production.left} -> {' '.join(production.right)}")

    def print_productions_for_non_terminal(self, non_terminal):
        matching_productions = [p for p in self.productions if p.left == non_terminal]
        if matching_productions:
            for production in matching_productions:
                print(f"{production.left} -> {' '.join(production.right)}")
        else:
            print(f"The non-terminal {non_terminal} does not exist!")

    def cfg_check(self):

        return (set(rule.left for rule in self.productions) == self.non_terminals and
                all(symbol in self.terminals.union(self.non_terminals) for rule in self.productions for symbol in rule.right ))


grammar = Grammar()

grammar.print_non_terminals()
grammar.print_terminals()
grammar.print_productions()
grammar.print_productions_for_non_terminal("program")

print(grammar.cfg_check())
