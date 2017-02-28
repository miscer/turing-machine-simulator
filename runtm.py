import argparse

from turingmachine.parser import parse_turing_machine, ParseError
from turingmachine.tape import tape_list_to_string

# Parse command line arguments
parser = argparse.ArgumentParser(description='Runs the given Turing machine on the input')
parser.add_argument('machine', help='machine description file')
parser.add_argument('input', help='input file')

arguments = parser.parse_args()

# Open the machine definition file and try to parse it
with open(arguments.machine) as machine_file:
    try:
        turing_machine = parse_turing_machine(machine_file)
    except ParseError as error:
        print(str(error))
        exit(2)

if arguments.input == '-':
    # Read the input from STDIN
    input_word = input('> ')
else:
    # Read the input from the specified file
    with open(arguments.input) as input_file:
        input_word = list(input_file.read().strip())

# Run the machine on the input
accepted, tape = turing_machine.run(input_word)

# Print result
if accepted:
    print('Accepted')
    print(tape_list_to_string(tape))
    exit(0)
else:
    print('Rejected')
    print(tape_list_to_string(tape))
    exit(1)
