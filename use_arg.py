from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("name")
parser.add_argument("msg")
parser.add_argument("--emoji")
parser.add_argument("--sleep")
args = parser.parse_args()

print(args.name)
print(args.msg)
print(args.emoji)
print(args.sleep)