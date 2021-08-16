import sys

args = sys.argv[1:]


def try_me(args):
    print(f"You typed: {args}")
    argdict = {i: v for i, v in enumerate(args)}
    return f"Your arguments in a dictionary: {argdict}"

if __name__ == "__main__":

    try_me(args)
