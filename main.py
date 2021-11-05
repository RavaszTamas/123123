# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def executeStatements(tokens, startingPoint, res):
    if tokens[startingPoint] == "print":
        res += tokens[startingPoint + 1]
        return res, 2


def lookFor(tkn, tokens, idx):
    while idx < len(tokens) and tkn != tokens[idx]:
        idx += 1
    return idx


def main():
    variables = {}
    sub_list_of_tokens = []
    current_level = -1

    res = ""

    with open("./level3/level3_example.in") as f:
        lines = int(f.readline().strip())
        allText = ""
        for token_idx in range(lines):
            allText += f.readline().strip() + " "
        tokens = allText.split()
        token_idx = 0
        prev_bool = None
        error = False

        while token_idx < len(tokens):
            if tokens[token_idx] == "start":
                current_level += 1
                token_idx += 1
            elif tokens[token_idx] == "print":
                res += tokens[token_idx + 1]
                token_idx += 2
            elif tokens[token_idx] == "var":
                if tokens[token_idx + 1] not in variables.keys():
                    name = tokens[token_idx + 1]
                    value = tokens[token_idx + 2]
                    variables[name] = value
                    token_idx += 3
                else:
                    error = True
            elif tokens[token_idx] == "set":
                if tokens[token_idx + 1] in variables.keys():
                    name = tokens[token_idx + 1]
                    value = tokens[token_idx + 2]
                    variables[name] = value
                    token_idx += 3
                else:
                    error = True
            elif tokens[token_idx] == "if":
                current_level += 1
                prev_bool = None
                if tokens[token_idx + 1] == "true":
                    token_idx += 2
                    prev_bool = True
                elif tokens[token_idx + 1] == "false":
                    token_idx += 2
                    token_idx = lookFor("end", tokens, token_idx)
                    prev_bool = False
            elif tokens[token_idx] == "end":
                current_level -= 1
                token_idx += 1
            elif tokens[token_idx] == "else":
                if not prev_bool:
                    token_idx += 1
                else:
                    token_idx = lookFor("end", tokens, token_idx)
            elif tokens[token_idx] == "return":
                break

    # with open("./level2/level2_5.out", "w") as f:
    #         f.write(res)


#     res = ""
#     for i in range(1,len(arr),2):
#         res += arr[i]
# with open("./level1/level1_5.out","w") as f:
#     f.write(res)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# res, processed_tokens = executeStatements(tokens, i + 2, res)
#         i += processed_tokens
#         i += 2
#         prev_bool = "true"
#     elif tokens[i+1] == "false":
#         prev_bool = "false"
#         pass

#     elif tokens[i] == "else":
#     # always gets checked
#     if prev_bool == "true":
#         pass
#     else:
#         pass

# elif tokens[current_token] == "end":
#     current_token += 1
# elif tokens[current_token] == "return":
#     break
# print(res)
