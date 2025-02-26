from data import CountyDemographics
from build_data import get_data

#Task 1
def population_total(l: list[CountyDemographics]) -> float:
    total = 0   #this function takes a list of county demographics from a database and returns the TOTAL of all their 2014 populations combined
    for county in l:
        if '2014 Population' in county.population:
            total += county.population['2014 Population']
    return total

print()

#Task 2
def filter_by_state(l1: list[CountyDemographics], s: str) -> list[CountyDemographics]:
    state_info = [] #this filter takes a list of county demographics and a string (state abbreviation) and returns the information (in objects) in the counties in that state
    for state in l1:
        if state.state == s:
            state_info.append(state)
    return state_info

print()

#Task 3
#Part A
def population_by_education(l3: list[CountyDemographics], s2: str) -> float:
    education_population = 0 #this function takes a list of county demographics and an education level and returns the total number of people (in inputted counties in 2014) with that education level.
    for county in l3:
        if '2014 Population' in county.population:
            if s2 in county.education:
                edu_percent = county.population['2014 Population'] * (county.education[s2]/100) #given in percentages so must multipy that percentage with population total.
                education_population += edu_percent
    return education_population
print()
#Part B
def population_by_ethnicity(l4: list[CountyDemographics], s3: str) -> float:
    ethnic_pop = 0  # this function takes a list of county demographics and an ethnicity and returns the total number of people (in inputted counties in 2014) with that ethnicity.
    for county in l4:
        if '2014 Population' in county.population:
            if s3 in county.ethnicities:
                eth_percent = county.population['2014 Population'] * (county.ethnicities[s3] / 100)
                ethnic_pop += eth_percent
    return ethnic_pop
print()
#Part C
def population_below_poverty_level(l5:list[CountyDemographics]) -> float:
    poverty_pop = 0  # this function takes a list of county demographics and returns the total number of people (in inputted counties in 2014) living below poverty level.
    for county in l5:
        if '2014 Population' in county.population:
            pov_percent = county.population['2014 Population'] * (county.income['Persons Below Poverty Level'] / 100)
            poverty_pop += pov_percent
    return poverty_pop
print()

#Task 4
#Part A
def percent_by_education(lst: list[CountyDemographics], s4: str) -> float:
    final_percent_by_education = 0 #this function takes a list of county demographics and returns the percent of the population in 2014 who has the inputted education level.
    for county in lst:
        if '2014 Population' in county.population:
            pop_by_edu = population_by_education(lst, s4)
            pop_total = population_total(lst)
            final_percent_by_education = (pop_by_edu/pop_total) * 100
    return final_percent_by_education
print()
#Part B
def percent_by_ethnicity(l3: list[CountyDemographics], s5: str) -> float:
    final_percent_by_ethnicity = 0 #this function takes a list of county demographics and returns the percent of the population in 2014 who has the inputted ethnicity.
    for county in l3:
        if '2014 Population' in county.population:
            pop_by_eth = population_by_ethnicity(l3, s5)
            pop_total_e = population_total(l3)
            final_percent_by_ethnicity = (pop_by_eth / pop_total_e) * 100
    return final_percent_by_ethnicity

print()

#Part C
def percent_below_poverty_level(l4: list[CountyDemographics]) -> float:
    final_percent_by_poverty = 0 #this function takes a list of county demographics and returns the percent of the population in 2014 that lives below the poverty level.

    for county in l4:
        if '2014 Population' in county.population:
            pop_by_pov = population_below_poverty_level(l4)
            pop_total_p = population_total(l4)
            final_percent_by_poverty = (pop_by_pov / pop_total_p) * 100
    return final_percent_by_poverty
print()

#Task 5
#Part A
def education_greater_than(list5a: list[CountyDemographics], s5a: str, f5a: float) -> list[CountyDemographics]:
    population_greater = [] #this function takes a list of county demographics, education level, and a threshold and returns a list of county demographics that are greater than the percentage threshold of the education level inputted.
    for county in list5a:
        if county.population['2014 Population'] > 0:
            if s5a in county.education:
                edu_percent = (county.education[s5a] / county.population['2014 Population']) * 100
                if edu_percent > f5a:
                    population_greater.append(county)
    return population_greater
print()

def education_less_than(list5b: list[CountyDemographics], s5b: str, f5b: float) -> list[CountyDemographics]:
    population_less = [] #this function takes a list of county demographics, education level, and a threshold and returns a list of county demographics that are less than the percentage threshold of the education level inputted.
    for county in list5b:
        if county.population['2014 Population'] > 0:
            if s5b in county.education:
                edu_percent = (county.education[s5b] / county.population['2014 Population']) * 100
                if edu_percent < f5b:
                    population_less.append(county)
    return population_less
print()
#Part B
def ethnicity_greater_than(list5be: list[CountyDemographics], s5be: str, f5be: float) -> list[CountyDemographics]:
    pop_e_greater = [] #this function takes a list of county demographics, ethnicity, and a threshold and returns a list of county demographics that are greater than the percentage threshold of the ethnicity inputted.
    for county in list5be:
        if county.population['2014 Population'] > 0:
            if s5be in county.ethnicities:
                e_percent = (county.ethnicities[s5be]/county.population['2014 Population']) * 100
                if e_percent > f5be:
                    pop_e_greater.append(county)
    return pop_e_greater
print()
def ethnicity_less_than(list5ae: list[CountyDemographics], s5bae: str, f5bae: float) -> list[CountyDemographics]:
    pop_e_less = []  #this function takes a list of county demographics, ethnicity, and a threshold and returns a list of county demographics that are less than the percentage threshold of the ethnicity inputted.
    for county in list5ae:
        if county.population['2014 Population'] > 0:
            if s5bae in county.ethnicities:
                e_percent = (county.ethnicities[s5bae] / county.population['2014 Population']) * 100
                if e_percent > f5bae:
                    pop_e_less.append(county)
    return pop_e_less
print()
#Part C
def below_poverty_level_greater_than(listp: list[CountyDemographics], fa:float) -> list[CountyDemographics]:
    pop_pov = []  #this function takes a list of county demographics and a threshold and returns a list of county demographics that are greater than the percentage threshold of people in poverty.
    for county in listp:
        if county.population['2014 Population'] > 0:
            p_percent = (county.income['Persons Below Poverty Level']/county.population['2014 Population']) * 100
            if p_percent > fa:
                pop_pov.append(county)
    return pop_pov
print()

def below_poverty_level_less_than(listpb: list[CountyDemographics], fb:float) -> list[CountyDemographics]:
    pop_povb = [] #this function takes a list of county demographics and a threshold and returns a list of county demographics that are less than the percentage threshold of people in poverty.
    for county in listpb:
        if county.population['2014 Population'] > 0:
            p_percent = (county.income['Persons Below Poverty Level']/county.population['2014 Population']) * 100
            if p_percent < fb:
                pop_povb.append(county)
    return pop_povb
print(below_poverty_level_less_than(get_data(), 0))


