"""
Calculate the probability of zero
for a specific X chromosome
"""

from os import path
from argparse import ArgumentParser
import vcf
import re
import sys

def is_valid_file(parser, file):
    """Function for checking that a file exist"""
    if not path.isfile(file):
        parser.error("The file %s does not exist!" % file)
    else:
        return file


def main():
    """Function for calculation"""
    parser = ArgumentParser(description="Argument parser for vcf file")
    parser.add_argument("-in", dest="input", required=True,
                        help="Vcf file location", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    vcf_reader = vcf.Reader(open(args.input, "r"))
    # Hold all the sample information
    samples = vcf_reader.samples

    for record in vcf_reader:
        gender = "none"
        genotype = "-1/-1"
        for sample in samples:
            match_male_female = re.search(r"[\w]*_(\w)_[\d]+", sample)
            if match_male_female:
                gender = match_male_female.group(1)
                print("Gender", gender)
            else:
                print("Not possible to finder gender, aborting program")
                sys.exit(1)
            genotype = record.genotype(sample)["GT"]
            print("For", sample, "Genotype:", genotype)
    print("Done")


if __name__ == "__main__":
    main()
