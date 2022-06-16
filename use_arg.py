import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("msg")
parser.add_argument("--repeat")
parser.add_argument("--sleep")
args = parser.parse_args()

print(args.name)
print(args.msg)
print(args.repeat)
print(args.sleep)