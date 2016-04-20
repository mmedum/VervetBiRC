class VariableHolder(object):
    """Calculation object for holding information about population group"""

    def __init__(self):
        self._male = 0
        self._female = 0
        self._zero_male_genotype = 0
        self._zero_one_female_genotype = 0
        self._zero_zero_female_genotype = 0

    @property
    def male(self):
        """Get male"""
        return self._male

    @male.setter
    def male(self, value):
        """Set male"""
        self._male = value

    @property
    def female(self):
        """Get female"""
        return self._female

    @female.setter
    def female(self, value):
        """Set female"""
        self._female = value

    @property
    def zero_male_genotype(self):
        """Get male zero"""
        return self._zero_male_genotype

    @zero_male_genotype.setter
    def zero_male_genotype(self, value):
        """Set male zero"""
        self._zero_male_genotype = value

    @property
    def zero_one_female_genotype(self):
        """Get zero one female"""
        return self._zero_one_female_genotype

    @zero_one_female_genotype.setter
    def zero_one_female_genotype(self, value):
        """Set zero one female"""
        self._zero_one_female_genotype = value

    @property
    def zero_zero_female_genotype(self):
        """Get zero zero female"""
        return self._zero_zero_female_genotype

    @zero_zero_female_genotype.setter
    def zero_zero_female_genotype(self, value):
        """Set zero zero female"""
        self._zero_zero_female_genotype = value

    def reset_values(self):
        """Reset all variables"""
        self.male = 0
        self.female = 0
        self.zero_male_genotype = 0
        self.zero_one_female_genotype = 0
        self.zero_zero_female_genotype = 0

    def probability_calculation(self):
        """Perform Probability calculation based on own data"""
        numerator = self.zero_male_genotype + self.zero_one_female_genotype + (2 * self.zero_zero_female_genotype)
        denominator = self.male + (2 * self.female)
        if numerator == 0 and denominator == 0:
            return str(0)
        return str(numerator/denominator)

