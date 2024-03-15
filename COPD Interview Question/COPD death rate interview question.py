'''
Ideally, the crude death rate should simply be the national total of the 2019 COPD deaths for each country, divided by the 2019 population.  Unfortunately, the total COPD deaths is not available, so instead I have calculated it from the actual population in each age group (from World Population Prospects), and used the COPD death rate for this age group to
estimate a figure for deaths for each group.  By adding these across all age groups, this is as close as we can get to total COPD deaths for the population.

It is also worth noting that I have grouped the age groups above 85 into one group in the crude measure, to fit with the WHO population proportions.

This calculation for Crude Death Rate gives a figure of 57.2 deaths per 100k people in the USA, and 5.8 deaths per 100k people in Uganda.  At first, this difference is staggering - almost 900% greater.  However, the issue is the population structure of both countries.  The USA population pyramid indicates there are proportionally far more older people than in Uganda, and COPD is far more prevalent in older age groups.

In calculating the Age-standardised Death Rate (by the direct method) by using the WHO standard population proportions, these population differences are controlled against, and in this measure, the COPD standardised death rates for both countries are remarkably similar - 28.4 for the USA, and 28.7 for Uganda.

In its own way, this is just as striking: there is a known correlation between COPD and smoking, and a known correlation between smoking and lower-income groups.  Accordingly, one might expect the age-standardised rate for Uganda to diverge more widely from the USA, but it does not.  Clearly, there is more to explore here.

Ian Garforth

'''


################################################################


# INITIAL DATA
# Establish total populations for both countries from "UN World Population Prospects (2022) — Population Estimates 1950-2021"
# Total population of USA in 2019 (in 100k)
usa_total_pop = 334321000
usa_actual_by_group = [19849000, 20697000, 22092000, 21895000, 21872000, 23407000, 22842000, 22297000, 20695000, 21244000, 21346000, 22348000, 20941000, 17501000, 13689000, 9273000, 6119000, 6214000]

# Total population of Uganda in 2019 (in 100k)
uganda_total_pop = 42949000
uganda_actual_by_group = [7329000, 6614000, 5899000, 5151000, 4348000, 3500000, 2619000, 1903000, 1504000, 1235000, 953000, 687000, 500000, 353000, 197000, 93000, 44000, 20000]


#COPD data from table, by age group (might be better done as a dictionary - eg: {"0-4": 0.04, "5-9": 0.02, etc, etcz})
usa_crude_copd_death_rates = [0.04, 0.02, 0.02, 0.02, 0.06, 0.11, 0.29, 0.56, 1.42, 4, 14.13, 37.22, 66.48, 108.66, 213.1, 333.06, 491.1, 894.45]
uganda_crude_copd_death_rates = [0.4, 0.17, 0.07, 0.23, 0.38, 0.4, 0.75, 1.11, 2.04, 5.51, 13.26, 33.25, 69.62, 120.78, 229.88, 341.06, 529.31, 710.4]

# WHO reference population for standardised calculation
who_av_pop_by_age_group = [8.86, 8.69, 8.60, 8.47, 8.22, 7.93, 7.61, 7.15, 6.59, 6.04, 5.37, 4.55, 3.72, 2.96, 2.21, 1.52, 0.91, 0.63]
reference_who_100k_pop = [8860, 8690, 8600, 8470, 8220, 7930, 7610, 7150, 6590, 6040, 5370, 4550, 3720, 2960, 2210, 1520, 910, 630]


################################################################


# CRUDE RATES
# Create list of expected number of deaths in actual population group (drawn from UN World Population Prospects)
usa_crude_exp = []
for index in range(18):
    usa_crude_exp.append(usa_crude_copd_death_rates[index] / 100000 * usa_actual_by_group[index])

# Total estimated COPD deaths in 2019 in USA
usa_crude_copd = 0
for value in usa_crude_exp:
    usa_crude_copd += value

print("The Crude Death Rate in the USA in 2019 from COPD deaths was " + str(round((usa_crude_copd  / usa_total_pop * 100000), 1)) + " deaths per 100 000 people")


# Create list of expected number of deaths in actual population group (drawn from UN World Population Prospects)
uganda_crude_exp = []
for index in range(18):
    uganda_crude_exp.append(uganda_crude_copd_death_rates[index] / 100000 * uganda_actual_by_group[index])

# Total estimated COPD deaths in 2019 in Uganda
uganda_crude_copd = 0
for value in uganda_crude_exp:
    uganda_crude_copd += value

print("The Crude Death Rate in Uganda in 2019 from COPD deaths was " + str(round((uganda_crude_copd  / uganda_total_pop * 100000), 1)) + " deaths per 100 000 people")


################################################################


# STANDARDISED RATES
# calculate expected mortalities in reference population based on crude rates and append to list
usa_exp_copd_mortalities = []
for index in range(18):
    usa_exp_copd_mortalities.append(usa_crude_copd_death_rates[index] / 100000 * reference_who_100k_pop[index])

# sum expected standardised mortalities
usa_standardised_copd = 0
for value in usa_exp_copd_mortalities:
    usa_standardised_copd += value

print("The Age-standardised Death Rate for all ages in the USA in 2019 from COPD deaths was " + str(round((usa_standardised_copd), 1)) + " deaths per 100 000 people")


# calculate expected mortalities in reference population based on crude rates and append to list
uganda_exp_copd_mortalities = []
for index in range(18):
    uganda_exp_copd_mortalities.append(uganda_crude_copd_death_rates[index] / 100000 * reference_who_100k_pop[index])

# sum expected standardised mortalities
uganda_standardised_copd = 0
for value in uganda_exp_copd_mortalities:
    uganda_standardised_copd += value

print("The Age-standardised Death Rate for all ages in Uganda in 2019 from COPD deaths was " + str(round((uganda_standardised_copd), 1)) + " deaths per 100 000 people")