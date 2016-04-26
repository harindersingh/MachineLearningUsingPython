import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time


class Utility:
    def timing(func, *args):
        # Timing Python operations
        pass


    def fill_missing_values(df_data):
        """
        Dealing with missing data:
        1. Fill forward (to avoid peeking into the future)
        2. Fill backward
        """
        """Fill missing values in data frame, in place."""
        df_data.fillna(method='ffill', inplace=True)
        df_data.fillna(method='bfill', inplace=True)
        return df_data
