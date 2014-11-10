import argparse
import os


base_dir = os.path.dirname(__file__)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('license', nargs='+', help="License to print the text of")

    args = p.parse_args()

    license = args.license

    print license

    licenseFile = os.path.join(base_dir, '../licenses/')
    licenseFile = os.path.join(licenseFile, license[0])

    with open(licenseFile) as licenseFile:
        print licenseFile.read()
if __name__ == '__main__':
    main()
