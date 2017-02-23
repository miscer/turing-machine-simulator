import argparse

from turingmachine.parser import parse_turing_machine, ParseError

parser = argparse.ArgumentParser(description='Runs the given Turing machine on the input')
parser.add_argument('machine', help='machine description file')
parser.add_argument('input', help='input file')

arguments = parser.parse_args()

with open(arguments.machine) as machine_file:
    try:
        turing_machine = parse_turing_machine(machine_file)
    except ParseError as error:
        print(str(error))
        exit(2)

if arguments.input == '-':
    input_word = input('> ')
else:
    with open(arguments.input) as input_file:
        input_word = list(input_file.read().strip())

accepted = turing_machine.run(input_word)

if accepted:
    print('Accepted')
    exit(0)
else:
    print('Rejected')
    exit(1)
