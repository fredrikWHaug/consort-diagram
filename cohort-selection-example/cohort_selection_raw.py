import pandas as pd
import numpy as np
import os
from utils import get_demography, print_demo

# get parent directory of this file
script_dir = os.path.dirname(__file__)

# get root directory of this project (two levels up from this file)
root_dir = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))

# MIMIC
df0 = pd.read_csv(os.path.join(root_dir, 'data', 'MIMIC_data.csv'))

df1 = df0[df0.sepsis3 == 1]

df2 = df1[df1.race_group != 'Other']

df3 = df2[df2.los_icu >= 1]

df4 = df3[df3.admission_age >= 18]

df5 = df4.sort_values(by=["subject_id", "stay_id"], ascending=True).groupby(
    'subject_id').apply(lambda group: group.iloc[0, 1:])

df6 = df5[~df5.lactate_day1.isnull()]

df6.to_csv(os.path.join(root_dir, 'data/cohorts', 'cohort_MIMIC_lac1_entire_los.csv'))
