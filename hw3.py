from data import CountyDemographics
from build_data import get_data

#Task 1
def population_total(l: list[CountyDemographics]) -> float:
    total = 0   #this function takes a list of county demographics from a database and returns the TOTAL of all their 2014 populations combined
    for county in l:
        if '2014 Population' in county.population:
            total += county.population['2014 Population']
    return total

print(population_total(get_data()))

#Task 2
def filter_by_state(l1: list[CountyDemographics], s: str) -> list[CountyDemographics]:
    state_info = []
    for state in l1:
        if state.state == s:
            state_info.append(state)
    return state_info

print(filter_by_state(get_data(), 'WY'))



