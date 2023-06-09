# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/sales_initiatives_latem.ipynb.

# %% auto 0
__all__ = ['did_latem_make_chicken_today']

# %% ../nbs/sales_initiatives_latem.ipynb 0
import sys
sys.path.append('..')
import pandas as pd
import foodcosts.core as core
import datetime

# %% ../nbs/sales_initiatives_latem.ipynb 8
def did_latem_make_chicken_today():
    range = {
        'lower': core.get_previous_n_day(1),
        'upper': core.get_previous_n_day(0)
    }
    res_kip_rosemarijn = core.get_sales_by_day(range["lower"], range["upper"], ['LATEM'], 18191)
    res_kip_italienne = core.get_sales_by_day(range["lower"], range["upper"], ['LATEM'], 53796)
    return len(res_kip_rosemarijn) > 0 or len(res_kip_italienne) > 0
