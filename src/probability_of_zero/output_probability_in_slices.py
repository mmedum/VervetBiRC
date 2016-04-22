"""
Calculate the probability of zero
for a specific X chromosome
"""

from os import path
from argparse import ArgumentParser
from collections import OrderedDict
import vcf
import re
import sys
import variable_holder

def is_valid_file(parser, file):
    """Function for checking that a file exist"""
    if not path.isfile(file):
        parser.error("The file %s does not exist!" % file)
    else:
        return file


def accumulate_gender(gender, genotype, variables):
    """Function for accumulating total he/she"""
    if gender == "m":
        if genotype == "0/0" or genotype == "1/1":
            variables.male += 1
    elif gender == "f":
        if genotype == "0/0" or genotype == "0/1" or genotype == "1/1":
            variables.female += 1


def accumulate_genotypes(gender, genotype, variables):
    """Function for accumulating genotype"""
    if gender == "m" and genotype == "0/0":
        variables.zero_male_genotype += 1
    elif gender == "f":
        if genotype == "0/0":
            variables.zero_zero_female_genotype += 1
        elif genotype == "0/1":
            variables.zero_one_female_genotype += 1


def setup_output_file(out, dict_population):
    """Setup headers in output file"""
    for key in dict_population:
        string_key = str(key)
        out.write(string_key)
        out.write("\t")
    out.write("\n")


def setup_dict_population(dict_population):
    """Setup dict for handling intermidiate results for each population group

    10 population groups, where key 0 defines the total for all groups"""
    dict_population["chromStart"] = ""
    dict_population["chromEnd"] = ""
    for i in range(11):
        dict_population[i] = variable_holder.VariableHolder()


def reset_dict_population(dict_population):
    """Reset values in dict population"""
    for key in range(11):
        dict_population[key].reset_values()


def output_dict_to_file(out, dict_population):
    """Output the current information in dict to put file"""
    out.write(dict_population["chromStart"])
    out.write("\t")
    out.write(dict_population["chromEnd"])
    out.write("\t")
    for key in range(11):
        out.write(dict_population[key].probability_calculation())
        out.write("\t")
    out.write("\n")


def main():
    """Function for calculation"""
    parser = ArgumentParser(description="Argument parser for vcf file")
    parser.add_argument("-in", dest="input", required=True,
                        help="Vcf file location", metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument("-out", dest="output", required=True,
                        help="Output file location", metavar="FILE")
    parser.add_argument("-s", dest="slice", required=True,
                        help="Slice for each chromosome",
                        metavar="VERVET", type=int)

    args = parser.parse_args()

    with open(args.output, 'a') as out:
        dict_population = OrderedDict()
        setup_dict_population(dict_population)
        setup_output_file(out, dict_population)

        vcf_reader = vcf.Reader(open(args.input, "r"))
        # Hold all the sample information
        samples = vcf_reader.samples

        window_slice = args.slice
        should_set_start_pos = True
        start_pos = -1
        temp_end_pos = -1

        for record in vcf_reader:
            if should_set_start_pos:
                start_pos = record.POS
                dict_population["chromStart"] = str(start_pos)
                should_set_start_pos = False
            elif (record.POS - start_pos) >= window_slice:
                end_position = record.POS
                dict_population["chromEnd"] = str(end_position)
                output_dict_to_file(out, dict_population)
                reset_dict_population(dict_population)
                dict_population["chromStart"] = str(end_position)
                start_pos = end_position
            gender = "none"
            population_group = -1
            genotype = "-1/-1"
            current_variable_holder = None
            for sample in samples:
                genotype = record.genotype(sample)["GT"].lower().strip()
                match_population_gender = re.search(r"[\w]+_(\w)_(\d+)", sample)
                if match_population_gender:
                    gender = match_population_gender.group(1).lower().strip()
                    population_group = int(match_population_gender.group(2).lower().strip())
                    current_variable_holder = dict_population[population_group]
                else:
                    print("Not possible to find gender or population group, aborting program")
                    sys.exit(1)
                accumulate_gender(gender, genotype, current_variable_holder)
                accumulate_genotypes(gender, genotype, current_variable_holder)
                # We need to do the total too
                accumulate_gender(gender, genotype, dict_population[0])
                accumulate_genotypes(gender, genotype, dict_population[0])
            temp_end_pos = record.POS + 1
        dict_population["chromEnd"] = str(temp_end_pos)
        output_dict_to_file(out, dict_population)

    print("Done")

if __name__ == "__main__":
    main()
