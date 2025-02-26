import data
import build_data
import unittest
from hw3 import *


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total(self):
        p1 = population_total(get_data())
        self.assertEqual(318857056, p1)
        self.assertNotEqual(1, p1)
    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        f1 = filter_by_state(get_data(), 'CA')
        f2 = filter_by_state(get_data(), 'ZZ')
        self.assertNotEqual([], f1)
        self.assertEqual([], f2)
    # Part 3
    # test population_by_education
    def test_population_by_education(self):
        t1 = population_by_education(get_data(), "Bachelor's Degree or Higher")
        self.assertEqual(92216021.02199993, t1)
        t2 = population_by_ethnicity(get_data(), "GED")
        self.assertEqual(0, t2)

    # test population_by_ethnicity
    def test_population_by_ethnicity(self):
        s1 = population_by_ethnicity(get_data(), "Two or More Races")
        self.assertEqual(7991261.383000009, s1)
        s2 = population_by_ethnicity(get_data(), "Wasian")
        self.assertEqual(0, s2)
    # test population_below_poverty_level
    def test_population_below_poverty_level(self):
        p1 = population_below_poverty_level(get_data())
        self.assertEqual(48996488.47399998, p1)
        self.assertNotEqual(0, p1)

    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        e1 = percent_by_education(get_data(), 'High School or Higher')
        self.assertEqual(85.94008207646526, e1)
        e2 = percent_by_education(get_data(), "Bachelor's Degree or Higher")
        self.assertEqual(28.920803001455276, e2)
    # test percent_by_ethnicity
    def test_percent_by_ethnicity(self):
        eth1 = percent_by_ethnicity(get_data(), "Two or More Races")
        self.assertEqual(2.5062206504848397, eth1)
        eth2 = percent_by_ethnicity(get_data(), "Wasian")
        self.assertEqual(0.0, eth2)
    # test percent_below_poverty_level
    def test_percent_below_poverty(self):
        pov1 = percent_below_poverty_level(get_data())
        self.assertEqual(15.366286413307403, pov1)
        self.assertNotEqual(0, pov1)
    # Part 5
    # test education_greater_than
    def test_education_greater_than(self):
        edu1 = education_greater_than(get_data(), "Bachelor's Degree or Higher", 5)
        self.assertNotEqual([], edu1)
        edu2 = education_greater_than(get_data(), "Bachelor's Degree or Higher", 100)
        self.assertEqual([], edu2)
    # test education_less_than
    def test_education_less_than(self):
        edu3 = education_less_than(get_data(), "Bachelor's Degree or Higher", 5)
        self.assertNotEqual([], edu3)
        edu4 = education_less_than(get_data(), "Bachelor's Degree or Higher", 0.0001)
        self.assertEqual([], edu4)
    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        eth1 = ethnicity_greater_than(get_data(), "White Alone", 10)
        self.assertNotEqual([], eth1)
        eth2 = ethnicity_greater_than(get_data(), "Wasian", 10)
        self.assertEqual([], eth2)
    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        eth3 = ethnicity_less_than(get_data(), "White Alone", 10)
        self.assertNotEqual([], eth3)
        eth4 = ethnicity_less_than(get_data(), "Wasian", 10)
        self.assertEqual([], eth4)
    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater(self):
        pov1 = below_poverty_level_greater_than(get_data(), 10)
        self.assertNotEqual([], pov1)
        pov2 = below_poverty_level_greater_than(get_data(), 99)
        self.assertEqual([], pov2)
    # test below_poverty_level_less_than
    def test_below_poverty_level_less(self):
        pov3 = below_poverty_level_less_than(get_data(), 0)
        self.assertEqual([], pov3)
        pov4 = below_poverty_level_less_than(get_data(), 10)
        self.assertNotEqual([], pov4)


if __name__ == '__main__':
    unittest.main()
