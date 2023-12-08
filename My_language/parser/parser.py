from pprint import pprint

from My_language.parser.grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar()
        self.first_sets = {non_terminal: set() for non_terminal in self.grammar.non_terminals}
        self.build_first_sets()

    def build_first_sets(self):

        while True:
            prev_first_sets = {key: value.copy() for key, value in self.first_sets.items()}

            for production in self.grammar.productions:
                non_terminal = production.left
                right_symbols = production.right
                i = 0
                while i < len(right_symbols):

                    symbol = right_symbols[i]

                    if symbol in self.grammar.terminals:
                        self.first_sets[non_terminal].add(symbol)
                        break
                    elif symbol in self.grammar.non_terminals:
                        self.first_sets[non_terminal].update(self.first_sets[symbol] - {'epsilon'})
                        if 'epsilon' not in self.first_sets[symbol]:
                            break

                    i += 1
                else:
                    self.first_sets[non_terminal].add('epsilon')

            if prev_first_sets == self.first_sets:
                break


parser = Parser()
pprint(parser.first_sets)
l=10