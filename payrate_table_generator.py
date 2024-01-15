# Columns from page 74 of The Agreement were OCR'ed and turned into arrays of the same length
scale_names = ['Intern', 'Resident Medical Officer Yr 1', 'Resident Medical Officer Yr 2', 'Resident Medical Officer Yr 3', 'Registrar Yr 1', 'Registrar Yr 2', 'Registrar Yr 3', 'Registrar Yr 4', 'Registrar Yr 5', 'Registrar Yr 6', 'Registrar Yr 7', 'Senior Registrar Yr 1', 'Senior Registrar Yr 2', 'Supervised Medical Officer Yr 1', 'Supervised Medical Officer Yr 2', 'Supervised Medical Officer Yr 3', 'Supervised Medical Officer Yr 4', 'Supervised Medical Officer Yr 5', 'Supervised Medical Officer Yr 6', 'Supervised Medical Officer Yr 7', 'Supervised Medical Officer Yr 8', 'Supervised Medical Officer Yr 9', 'Trainee Medical Administrator Yr 1', 'Trainee Medical Administrator Yr 2', 'Trainee Medical Administrator Yr 3', 'Trainee Medical Administrator Yr 4', 'Trainee Medical Administrator Yr 5', 'Trainee Medical Administrator Yr 6', 'Trainee Medical Administrator Yr 7', 'Trainee Psychiatrist Yr 1', 'Trainee Psychiatrist Yr 2', 'Trainee Psychiatrist Yr 3', 'Trainee Psychiatrist Yr 4', 'Trainee Psychiatrist Yr 5', 'Trainee Psychiatrist Yr 6', 'Trainee Psychiatrist Yr 7', 'Trainee Public Health Physician Yr 1', 'Trainee Public Health Physician Yr 2', 'Trainee Public Health Physician Yr 3', 'Trainee Public Health Physician Yr 4', 'Trainee Public Health Physician Yr 5', 'Trainee Public Health Physician Yr 6', 'Trainee Public Health Physician Yr 7']

# these are the 2023 rates spelled out on page 74 of the 2022 agreement
# they have been superseded by the new WA health wages policy, which is calculated from the 2022 rates
# https://web.archive.org/web/20230604183824/https://www.wa.gov.au/organisation/department-of-treasury/wages-policy
# annual_rates = ['82893', '90978', '99869', '109650', '115028', '120678', '129574', '135950', '142644', '149673', '157053', '168679', '177010', '115028', '120678', '129574', '135950', '142644', '149673', '157053', '168679', '177010', '120678', '129574', '135950', '142644', '149673', '157053', '168679', '129574', '135950', '142644', '149673', '157053', '168679', '177010', '120678', '129574', '135950', '142644', '149673', '157053', '168679']

annual_rates = ['80479', '88328', '96960', '106456', '111678', '117163', '125800', '131990', '138489', '145314', '152479', '163766', '171854', '111678', '117163', '125800', '131990', '138489', '145314', '152479', '163766', '171854', '117163', '125800', '131990', '138489', '145314', '152479', '163766', '125800', '131990', '138489', '145314', '152479', '163766', '171854', '117163', '125800', '131990', '138489', '145314', '152479', '163766']

# Those two arrays are then smooshed into the desired hypertext…
for i in range(0,len(scale_names)):
    # PD allowances
    # Default is $10472 with special cases for interns, RMOs, and SRs
    pd = '10167' 
    if "Intern" in scale_names[i]:
        pd = '5810'
    elif "Resident Medical Officer" in scale_names[i]:
        pd = '5810'
    elif "Senior Registrar" in scale_names[i]:
        pd = '14524'

    # Uniquely identify registrar year 4
    # This is used to calculate the on-call rate client-side
    if "Registrar Yr 4" in scale_names[i]:
        oncall=' data-payscale-epoch-oncall'
    else:
        oncall=''

    print(f'<option data-payscale-epoch-pd-allowance="{pd}" data-payscale-epoch-annual-salary="{annual_rates[i]}" value="{annual_rates[i]}"{oncall}>{scale_names[i]}</option>')

# Run `python payrate_table_generator.py | pbcopy`