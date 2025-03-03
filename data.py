class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state


    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return 'CountyDemographics({}, {}, {}, {}, {}, {}, {})'.format(
                self.age,
                self.county,
                self.education,
                self.ethnicities,
                self.income,
                self.population,
                self.state
            )


def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population['2014 Population'] for county in counties)

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state]

def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    return sum((county.population['2014 Population'] * county.education.get(education_key, 0) / 100) for county in counties)

def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    return sum((county.population['2014 Population'] * county.ethnicities.get(ethnicity_key, 0) / 100) for county in counties)

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    return sum((county.population['2014 Population'] * county.income.get('Persons Below Poverty Level', 0) / 100) for county in counties)

def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    return (population_by_education(counties, education_key) / total_population * 100) if total_population > 0 else 0

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    return (population_by_ethnicity(counties, ethnicity_key) / total_population * 100) if total_population > 0 else 0

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    return (population_below_poverty_level(counties) / total_population * 100) if total_population > 0 else 0

def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) > threshold]

def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) < threshold]

def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]

def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) > threshold]

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) < threshold]