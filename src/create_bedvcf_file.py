"""Conversion from vcf file to bed file"""

from os import path
import gzip
from csv import DictReader, DictWriter
from argparse import ArgumentParser


def is_valied_file(parser, file):
    """Function for checking that a file exist"""
    if not path.isfile(file):
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


def setup_bed_file(out_file):
    """Setup bed file format"""
    out_file.write("chrom")
    out_file.write("\t")
    out_file.write("chromStart")
    out_file.write("\t")
    out_file.write("chromEnd")
    out_file.write("\n")


def main():
    """Create bed file and a poly file from vcf"""
    parser = ArgumentParser(description="Argument parser for vcf file location")
    parser.add_argument("-in", dest="input", required=True,
                        help="Vcf file location", metavar="FILE",
                        type=lambda x: is_valied_file(parser, x))
    parser.add_argument("-bed", dest="bedout", required=True,
                        help="Location for saving bed output",
                        metavar="FILE")
    parser.add_argument("-vcf", dest="vcfout", required=True,
                        help="Location for saving vcf output",
                        metavar="FILE")

    args = parser.parse_args()

    with gzip.open(args.input, "r") as vcf_file, open(args.bedout, "w") as bedout, open(args.vcfout, "w") as vcfout:
        # Copy original header to new cvf file,
        # save line count for creating DictReader
        fieldnames = []
        for line in vcf_file:
            if line.startswith("##"):
                vcfout.write(line)
            else:
                vcfout.write(line)
                fieldnames = line.split("\t")
                break

        # Setup DictReader with start from column headers
        reader = DictReader(vcf_file, fieldnames=fieldnames, delimiter="\t")
        writer = DictWriter(vcfout, fieldnames=reader.fieldnames, extrasaction="raise", delimiter="\t")

        setup_bed_file(bedout)

        chrome_pass_string = "PASS"
        chrome_current = ""
        start_position = ""
        for row in reader:
            if chrome_current == "":
                chrome_current = row["#CHROM"]
            chrome_filter = row["FILTER"]
            chrome_position = row["POS"]
            if chrome_filter == chrome_pass_string:
            # Get the alt allele
                chrome_alt_allele = row["ALT"]
                if start_position == "":
                    # Logic setting the start position
                    start_position = chrome_position
                if chrome_alt_allele != ".":
                    chrome_info = row["INFO"]
                    if "AA=" in chrome_info:
                        chrome_id = row["ID"]
                        if len(chrome_id) > 1:
                            chrome_id += ";"
                        else:
                            chrome_id = ""
                        chrome_split_info = chrome_info.split(";")
                        chrome_id += next(x for x in chrome_split_info if "AA=" in x)[3:]
                        row["ID"] = chrome_id
                    writer.writerow(row)
            elif start_position != "":
                # Ouput to bed bed file
                output_to_bedfile(chrome_current, start_position, chrome_position, bedout)
                start_position = ""


if __name__ == "__main__":
    main()
