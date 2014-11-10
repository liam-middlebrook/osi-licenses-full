import argparse
import os


base_dir = os.path.dirname(__file__)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('license', nargs=1, help="License to print the text of")
    p.add_argument('outfile', nargs=1, help="The File to write to")

    args = p.parse_args()

    license = args.license

    print license

    licenseFile = os.path.join(base_dir, '../licenses/')
    licenseFile = os.path.join(licenseFile, license[0])

    licenseText = None

    with open(licenseFile) as licenseFile:
        licenseText =  licenseFile.read()
    with open(args.outfile[0], 'w+') as outFile:
        outFile.write(licenseText)

    print licenseText

if __name__ == '__main__':
    main()
