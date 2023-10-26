from My_language.Scanner import Scanner
from My_language.SymTable import SymTable

hash = SymTable()

hash.add("abc")
hash.add("acb")
hash.add("cab")
# print(hash.find("abc"))
# print(hash.find("acb"))
# print(hash.find("cab"))
#
# print(hash.get_all())

def divide_program(program: str) -> list[str]:
    tokens = []
    current_pos = 0
    simple_tokens = [",", ";", "(", ")", "[", "]", "{", "}", " ", "+", "-", "*", "/", "%", ">", "<", "="]
    double_tokens = ["=", "<", ">"]

    while current_pos < len(program):
        token_start_pos = current_pos
        lookahead = program[current_pos]

        if lookahead.isspace():
            current_pos += 1
        elif lookahead in simple_tokens:
            if lookahead in double_tokens:
                next_lookahead = program[current_pos + 1]
                if next_lookahead in double_tokens:
                    current_pos += 2
                    tokens.append(lookahead + next_lookahead)
            else:
                current_pos += 1
                tokens.append(lookahead)


        elif lookahead.isdigit():
            text = ""
            while current_pos < len(program) and program[current_pos].isdigit():
                text += program[current_pos]
                current_pos += 1
            tokens.append(text)

        elif lookahead.isalpha():
            text = ""
            while current_pos < len(program) and program[current_pos].isalpha():
                text += program[current_pos]
                current_pos += 1
            tokens.append(text)
        else:
            raise ValueError(f"Unknown character '{lookahead}' at position {current_pos}")

    return tokens
def sequence_to_lexemes(sequence: str) -> list[str]:
    list_of_lexemes = []
    delimiter = [",", ";", "(", ")", "[", "]", "{", "}", " ", "+", "-", "*", "/", "%", ">", "<", "="]
    soft_delimiter = [">", "<", "="]
    start = 0
    end = 0
    last_char = ""
    while end < len(sequence):
        if sequence[end] == "\"":
            if len(last_char) == 0:
                start = end
                result = sequence[end + 1:].find("\"")
                if result == -1:
                    list_of_lexemes.append(sequence[start:])
                    return list_of_lexemes
                else:
                    end += result + 2
                    if end >= len(sequence):
                        list_of_lexemes.append(sequence[start:end])
                        return list_of_lexemes
                    if sequence[end] in delimiter:
                        list_of_lexemes.append(sequence[start:end])
                        if sequence[end] != " ":
                            list_of_lexemes.append(sequence[end])
                        start = end + 1
                    else:
                        list_of_lexemes.append(sequence[start:end])
                        list_of_lexemes.append(sequence[end:])
                        return list_of_lexemes
            else:
                list_of_lexemes.append(sequence[start:end + 1])
                return list_of_lexemes
        else:
            if sequence[end] == " " and len(last_char) == 0:
                end += 1
                start = end
                continue
            if sequence[end] in delimiter:
                if len(last_char) != 0:
                    last_char = ""
                    list_of_lexemes.append(sequence[start:end])
                if (sequence[end] in soft_delimiter and end + 1 < len(sequence)
                        and sequence[end + 1] in soft_delimiter):
                    list_of_lexemes.append(sequence[end:end + 2])
                    end += 1
                elif sequence[end] != " ":
                    list_of_lexemes.append(sequence[end])
                start = end + 1
            else:
                last_char = sequence[end]
        end += 1

    return list_of_lexemes

# print(sequence_to_lexemes("int a, b, c; \n a == 5; \n read(a);\n read(b);\n read(c);\n if (max(a, b) >= max(b, c)) {\n     write(max(a, b));\n } else {\n    write(c);\n}"))
# print(divide_program("int a, b, c; \n a == 5; \n read(a);\n read(b);\n read(c);\n if (max(a, b) >= max(b, c)) {\n     write(max(a, b));\n } else {\n    write(c);\n}"))

scanner = Scanner("D:\Semester V\FLCD\FLCD_project_compiler\Lab_1a\p1")

a = 5























