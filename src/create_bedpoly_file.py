"""Conversion from vcf file to bed file"""

import os
import csv
from argparse import ArgumentParser


def is_valied_file(parser, file):
    """Function for checking that a file exist"""
    if not os.path.isfile(file):
        parser.error("The file %s does not exist!" % file)
    else:
        return file


def output_to_bedfile(chromo, start, finish, out_file):
    """Output bed data to file"""
    out_file.write(chromo)
    out_file.write("\t")
    out_file.write(start)
    out_file.write("\t")
    out_file.write(finish)
    out_file.write("\n")


def output_to_polyfile(chromo, position, out_file):
    """Output poly data to file"""
    out_file.write(chromo)
    out_file.write("\t")
    out_file.write(position)
    out_file.write("\n")


def setup_bed_file(out_file):
    """Setup bed file format"""
    out_file.write("chrom")
    out_file.write("\t")
    out_file.write("chromStart")
    out_file.write("\t")
    out_file.write("chromEnd")
    out_file.write("\n")


def setup_poly_file(out_file):
    """Setup poly file"""
    out_file.write("chrom")
    out_file.write("\t")
    out_file.write("POS")
    out_file.write("\n")


def main():
    """Convert vcf file to bed file"""
    parser = ArgumentParser(description="Argument parser for vcf file location")
    parser.add_argument("-in", dest="input", required=True,
                        help="Vcf file location", metavar="FILE",
                        type=lambda x: is_valied_file(parser, x))
    parser.add_argument("-bed", dest="bedout", required=True,
                        help="Location for saving bed output",
                        metavar="FILE")
    parser.add_argument("-poly", dest="polyout", required=True,
                        help="Location for saving poly output",
                        metavar="FILE")


    args = parser.parse_args()

    with open(args.input) as vcf_file, open(args.bedout, "a") as bedout, open(args.polyout, "a") as polyout:
        reader = csv.DictReader(vcf_file, delimiter="\t")
        setup_bed_file(bedout)
        setup_poly_file(polyout)

        chrome_pass_string = "PASS"
        start = ""
        for row in reader:
            chrome_chrome = row["#CHROM"]
            chrome_filter = row["FILTER"]
            chrome_position = row["POS"]
            chrome_alt_allele = row["ALT"]
            if start == "" and chrome_filter == chrome_pass_string:
                start = chrome_position
            if start != "" and chrome_filter != chrome_pass_string:
                output_to_bedfile(chrome_chrome, start, chrome_position, bedout)
                start = ""
            if chrome_filter == chrome_pass_string and chrome_alt_allele != ".":
                output_to_polyfile(chrome_chrome, chrome_position, polyout)


if __name__ == "__main__":
    main()
