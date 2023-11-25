"""This is just the code for the ALU.
In the end, it wasn't actually required for solving the problem,
but it's a cool example of meta/higher-order programming,
and it can be used to verify the solution obtained by the other script."""

from functools import reduce


def build_instruction(instruction_type, var1, var2=None):
    def instruction(inputlist, inputindex, variables):
        if instruction_type == 'inp':
            variables[var1] = int(inputlist[inputindex])
            inputindex += 1
        else:
            right_hand_side_value = variables[var2] if var2.isalpha() else int(var2)
            if instruction_type == 'add':
                variables[var1] += right_hand_side_value
            elif instruction_type == 'mul':
                variables[var1] *= right_hand_side_value
            elif instruction_type == 'div':
                variables[var1] //= right_hand_side_value
            elif instruction_type == 'mod':
                variables[var1] %= right_hand_side_value
            elif instruction_type == 'eql':
                variables[var1] = int(variables[var1] == right_hand_side_value)
            else:
                print("Unknown instruction type: {}!".format(instruction_type))
        return inputlist, inputindex, variables

    return instruction


def apply_instructions(instruction_list, input_list):
    return reduce(lambda current_result, next_instruction: next_instruction(*current_result),
                  instruction_list,
                  (input_list, 0, dict(zip('wxyz', [0] * 4))))


if __name__ == '__main__':
    input = "input.txt"
    instruction_list = []
    with open(input, 'r') as infile:
        for line in infile:
            linesplit = line.strip().split()
            if linesplit[0] == 'inp':
                instruction_list.append(build_instruction(linesplit[0], linesplit[1]))
            else:
                instruction_list.append(build_instruction(*linesplit))

    # Testing the output of part 1
    print(apply_instructions(instruction_list,
                             list(str(91699394894995)))[2]['z'])
    # Part 2
    print(apply_instructions(instruction_list,
                             list(str(51147191161261)))[2]['z'])
