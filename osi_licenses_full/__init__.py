import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument('license', nargs='+', help="License to print the text of")

    args = p.parse_args()

    license = args.license

    print license

if __name__ == '__main__':
    main()
