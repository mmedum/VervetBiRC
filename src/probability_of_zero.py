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


def accumulate_gender(male, female, gender):
    """Function for accumulating total he/she"""
    if gender == "m":
        male += 1
    else:
        female += 1
    return male, female


def accumulate_genotypes(zero_male_genotype, zero_one_female_genotype, zero_zero_female_genotype, genotype, gender):
    """Function for accumulating genotype"""
    if gender == "m" and genotype == "0/0":
        zero_male_genotype += 1
    else:
        if genotype == "0/0":
            zero_zero_female_genotype += 1
        elif genotype == "0/1":
            zero_one_female_genotype += 1
    return zero_male_genotype, zero_one_female_genotype, zero_zero_female_genotype


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

    male = female = zero_male_genotype = zero_one_female_genotype = zero_zero_female_genotype = 0

    for record in vcf_reader:
        gender = "none"
        genotype = "-1/-1"
        for sample in samples:
            genotype = record.genotype(sample)["GT"]
            if genotype == "0/0" or genotype == "0/1" or genotype == "1/1":
                match_male_female = re.search(r"[\w]*_(\w)_[\d]+", sample)
                if match_male_female:
                    gender = match_male_female.group(1).lower()
                    male, female = accumulate_gender(male, female, gender)
                else:
                    print("Not possible to find gender, aborting program")
                    sys.exit(1)
                zero_male_genotype, zero_zero_female_genotype, zero_one_female_genotype = accumulate_genotypes(zero_male_genotype, zero_one_female_genotype, zero_zero_female_genotype, genotype, gender)
                print("For", sample, "Genotype:", genotype)
    numerator = zero_male_genotype + zero_one_female_genotype + (2 * zero_zero_female_genotype)
    denominator = male + (2 * female)
    # (0/0 male GT + 0/1 female GT + (2 * 0/0 female GT)) / male + female
    print("Probability:", (numerator/denominator))
    print(male, female)
    print("Done")


if __name__ == "__main__":
    main()
