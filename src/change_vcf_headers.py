"""
Change header name in poly vcf file
to append group and gender
"""

from os import path
from argparse import ArgumentParser
from collections import OrderedDict

def is_valid_file(parser, file):
    """Function for checking that a file exist"""
    if not path.isfile(file):
        parser.error("The file %s does not exist!" % file)
    else:
        return file


def setup_keys(or_dict):
    """Setup key/value list for gender and population group"""
    or_dict["#CHROM"] = "#CHROM"
    or_dict["POS"] = "POS"
    or_dict["ID"] = "ID"
    or_dict["REF"] = "REF"
    or_dict["ALT"] = "ALT"
    or_dict["QUAL"] = "QUAL"
    or_dict["FILTER"] = "FILTER"
    or_dict["INFO"] = "INFO"
    or_dict["FORMAT"] = "FORMAT"
    or_dict["A8518"] = "A8518_M_2"
    or_dict["AG23"] = "AG23_F_10"
    or_dict["AG5417"] = "AG5417_F_10"
    or_dict["AGM126"] = "AGM126_F_1"
    or_dict["AGM127"] = "AGM127_F_1"
    or_dict["AGM129"] = "AGM129_F_1"
    or_dict["AGM130"] = "AGM130_F_1"
    or_dict["AGM131"] = "AGM131_M_1"
    or_dict["AGM136"] = "AGM136_F_1"
    or_dict["AGM137"] = "AGM137_M_1"
    or_dict["AGM141"] = "AGM141_F_1"
    or_dict["AGM142"] = "AGM142_M_1"
    or_dict["AGM143"] = "AGM143_F_1"
    or_dict["AGM144"] = "AGM144_M_1"
    or_dict["B5616"] = "B5616_F_2"
    or_dict["C2166"] = "C2166_M_2"
    or_dict["C2265"] = "C2265_M_2"
    or_dict["C2439"] = "C2439_F_2"
    or_dict["V952"] = "V952_F_2"
    or_dict["VBOA1003"] = "VBOA1003_F_10"
    or_dict["VBOA1005"] = "VBOA1005_M_10"
    or_dict["VEA1001"] = "VEA1001_M_3"
    or_dict["VEA1002"] = "VEA1002_F_3"
    or_dict["VEA1003"] = "VEA1003_F_3"
    or_dict["VEA1004"] = "VEA1004_M_3"
    or_dict["VEA1005"] = "VEA1005_F_3"
    or_dict["VEA1007"] = "VEA1007_F_3"
    or_dict["VEA1008"] = "VEA1008_M_3"
    or_dict["VEB1009"] = "VEB1009_M_3"
    or_dict["VEB1010"] = "VEB1010_M_3"
    or_dict["VEB1011"] = "VEB1011_M_3"
    or_dict["VEB1012"] = "VEB1012_F_3"
    or_dict["VEB1013"] = "VEB1013_F_3"
    or_dict["VEB1014"] = "VEB1014_F_3"
    or_dict["VEB1015"] = "VEB1015_M_3"
    or_dict["VEC1016"] = "VEC1016_F_3"
    or_dict["VEC1017"] = "VEC1017_F_3"
    or_dict["VGA00002"] = "VGA00002_F_4"
    or_dict["VGA00006"] = "VGA00006_F_4"
    or_dict["VGA00010"] = "VGA00010_F_4"
    or_dict["VGA00019"] = "VGA00019_M_4"
    or_dict["VGA00021"] = "VGA00021_M_4"
    or_dict["VGA00025"] = "VGA00025_F_4"
    or_dict["VGA00085"] = "VGA00085_F_4"
    or_dict["VGA00090"] = "VGA00090_M_4"
    or_dict["VGA00092"] = "VGA00092_M_4"
    or_dict["VGA00098"] = "VGA00098_F_4"
    or_dict["VGA00100"] = "VGA00100_M_4"
    or_dict["VGA00101"] = "VGA00101_F_4"
    or_dict["VGA00107"] = "VGA00107_M_4"
    or_dict["VGA00114"] = "VGA00114_F_4"
    or_dict["VGA00138"] = "VGA00138_F_4"
    or_dict["VGA00142"] = "VGA00142_M_4"
    or_dict["VGA00146"] = "VGA00146_F_4"
    or_dict["VGA00151"] = "VGA00151_M_4"
    or_dict["VGA00152"] = "VGA00152_M_4"
    or_dict["VGA00153"] = "VGA00153_F_4"
    or_dict["VGA00155"] = "VGA00155_F_4"
    or_dict["VGA00156"] = "VGA00156_M_4"
    or_dict["VGHA1001"] = "VGHA1001_M_4"
    or_dict["VGHB1002"] = "VGHB1002_M_4"
    or_dict["VKA3"] = "VKA3_F_6"
    or_dict["VKB7"] = "VKB7_F_6"
    or_dict["VKC6"] = "VKC6_F_6"
    or_dict["VKD7"] = "VKD7_F_6"
    or_dict["VSAA2010"] = "VSAA2010_F_5"
    or_dict["VSAA2015"] = "VSAA2015_F_5"
    or_dict["VSAA2020"] = "VSAA2020_M_5"
    or_dict["VSAB1003"] = "VSAB1003_M_5"
    or_dict["VSAB2009"] = "VSAB2009_F_5"
    or_dict["VSAB2010"] = "VSAB2010_F_5"
    or_dict["VSAB2011"] = "VSAB2011_F_5"
    or_dict["VSAB2012"] = "VSAB2012_F_5"
    or_dict["VSAB2017"] = "VSAB2017_M_5"
    or_dict["VSAB2023"] = "VSAB2023_F_5"
    or_dict["VSAB3001"] = "VSAB3001_F_5"
    or_dict["VSAB3004"] = "VSAB3004_F_5"
    or_dict["VSAB5004"] = "VSAB5004_F_5"
    or_dict["VSAB5005"] = "VSAB5005_M_5"
    or_dict["VSAC1004"] = "VSAC1004_F_5"
    or_dict["VSAC1012"] = "VSAC1012_F_5"
    or_dict["VSAC1014"] = "VSAC1014_M_5"
    or_dict["VSAC1015"] = "VSAC1015_F_5"
    or_dict["VSAC1016"] = "VSAC1016_F_5"
    or_dict["VSAD1003"] = "VSAD1003_M_5"
    or_dict["VSAE2005"] = "VSAE2005_F_5"
    or_dict["VSAE2009"] = "VSAE2009_F_5"
    or_dict["VSAE2011"] = "VSAE2011_F_5"
    or_dict["VSAE3001"] = "VSAE3001_F_5"
    or_dict["VSAE3002"] = "VSAE3002_F_5"
    or_dict["VSAE3003"] = "VSAE3003_F_5"
    or_dict["VSAF1004"] = "VSAF1004_F_5"
    or_dict["VSAF1009"] = "VSAF1009_F_5"
    or_dict["VSAF1011"] = "VSAF1011_F_5"
    or_dict["VSAF1012"] = "VSAF1012_M_5"
    or_dict["VSAF1015"] = "VSAF1015_F_5"
    or_dict["VSAG2001"] = "VSAG2001_M_5"
    or_dict["VSAG2003"] = "VSAG2003_F_5"
    or_dict["VSAG2005"] = "VSAG2005_F_5"
    or_dict["VSAH1001"] = "VSAH1001_M_5"
    or_dict["VSAI3005"] = "VSAI3005_F_5"
    or_dict["VSAJ2008"] = "VSAJ2008_M_5"
    or_dict["VSAK3004"] = "VSAK3004_F_5"
    or_dict["VSAL1001"] = "VSAL1001_F_5"
    or_dict["VSAL2002"] = "VSAL2002_F_5"
    or_dict["VSAL3005"] = "VSAL3005_F_5"
    or_dict["VSAL4002"] = "VSAL4002_M_5"
    or_dict["VSAL5001"] = "VSAL5001_F_5"
    or_dict["VSAM0021"] = "VSAM0021_F_5"
    or_dict["VSAM1003"] = "VSAM1003_F_5"
    or_dict["VSAM2001"] = "VSAM2001_F_5"
    or_dict["VSAM3001"] = "VSAM3001_M_5"
    or_dict["VSAM4001"] = "VSAM4001_M_5"
    or_dict["VSAM5007"] = "VSAM5007_M_5"
    or_dict["VWP00201"] = "VWP00201_F_7"
    or_dict["VWP00268"] = "VWP00268_F_7"
    or_dict["VWP00301"] = "VWP00301_M_7"
    or_dict["VWP00312"] = "VWP00312_F_7"
    or_dict["VWP00384"] = "VWP00384_M_7"
    or_dict["VWP00389"] = "VWP00389_M_7"
    or_dict["VWP00390"] = "VWP00390_M_7"
    or_dict["VWP00393"] = "VWP00393_M_7"
    or_dict["VWP00410"] = "VWP00410_F_7"
    or_dict["VWP00414"] = "VWP00414_F_7"
    or_dict["VWP00437"] = "VWP00437_M_7"
    or_dict["VWP00456"] = "VWP00456_M_7"
    or_dict["VWP00494"] = "VWP00494_F_7"
    or_dict["VWP00542"] = "VWP00542_F_7"
    or_dict["VWP10008"] = "VWP10008_M_8"
    or_dict["VWP10010"] = "VWP10010_F_8"
    or_dict["VWP10020"] = "VWP10020_M_8"
    or_dict["VWP10026"] = "VWP10026_F_8"
    or_dict["VWP10045"] = "VWP10045_F_8"
    or_dict["VWP10053"] = "VWP10053_M_8"
    or_dict["VWP10064"] = "VWP10064_M_8"
    or_dict["VWP10067"] = "VWP10067_F_8"
    or_dict["VWP10070"] = "VWP10070_M_8"
    or_dict["VWP10076"] = "VWP10076_M_8"
    or_dict["VWP10077"] = "VWP10077_F_8"
    or_dict["VWP10084"] = "VWP10084_F_8"
    or_dict["VZA1001"] = "VZA1001_M_9"
    or_dict["VZA1002"] = "VZA1002_M_9"
    or_dict["VZA1003"] = "VZA1003_M_9"
    or_dict["VZA1004"] = "VZA1004_F_9"
    or_dict["VZA2005"] = "VZA2005_F_9"
    or_dict["VZA2006"] = "VZA2006_F_9"
    or_dict["VZA3008"] = "VZA3008_F_9"
    or_dict["VZA3009"] = "VZA3009_M_9"
    or_dict["VZA3010"] = "VZA3010_M_9"
    or_dict["VZA4012"] = "VZA4012_F_9"
    or_dict["VZA4013"] = "VZA4013_F_9"
    or_dict["VZC1014"] = "VZC1014_F_9"
    or_dict["VZC1015"] = "VZC1015_F_9"
    or_dict["VZC1017"] = "VZC1017_F_9"
    or_dict["VZC1018"] = "VZC1018_M_9"
    or_dict["VZC1020"] = "VZC1020_F_9"
    or_dict["W566"] = "W566_F_7"
    or_dict["X186"] = "X186_F_7"
    or_dict["X336"] = "X336_F_7"
    or_dict["X598"] = "X598_F_7"
    or_dict["Y010"] = "Y010_F_7"
    or_dict["Y083"] = "Y083_F_7"
    or_dict["Y173"] = "Y173_F_7"


def main():
    """Logic for changing name on columns"""
    parser = ArgumentParser(description="Parser for vcf file location")
    parser.add_argument("-in", dest="input", required=True,
                        help="Vcf file location", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-out", dest="output", required=True,
                        help="Vcf file location", metavar="FILE")
    args = parser.parse_args()

    or_dict = OrderedDict()
    setup_keys(or_dict)


    with open(args.input, "r") as vcf_file, open(args.output, "w") as out_file:
        for line in vcf_file:
            if line.startswith("#CHROM"):
                line = line.strip()
                keys = line.split("\t")
                for key in keys:
                    out_file.write(or_dict[key])
                    out_file.write("\t")
                out_file.write("\n")
            else:
                out_file.write(line)


if __name__ == "__main__":
    main()
