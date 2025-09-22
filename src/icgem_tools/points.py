import numpy as np
import pandas as pd
from typing import Dict
import re


HEADER = '''
 1 identifier (from input)
 2 longitude  (from input)    [degree]
 3 latitude   (from input)    [degree]
 4 h_over_ell (from input)     [meter]
 -------------------------------------
 5 height_anomaly              [meter]  T(h)/normal_gravity(h)            
 6 height_anomaly_ell          [meter]  T(h=0)/normal_gravity(h=0)        
 7 geoid                       [meter]  h_anomaly_ell + Topo-Term         
 8 gravity_disturbance          [mGal]  gravity(h) - gamma(h)             
 9 gravity_disturbance_sa       [mGal]  sph. approx. (h=0)                
10 gravity_anomaly              [mGal]  gravity(h) - gamma(h-h_anomaly)   
11 gravity_anomaly_sa           [mGal]  sph. approx. (h=0)                
12 gravity_anomaly_bg           [mGal]  gravity_anomaly_sa + Topo-Term    
13 gravitation                  [mGal]  gravitation(h)                    
14 gravitational_potential [m**2/s**2]  gravitational_potential(h)        
15 gravity                      [mGal]  gravity(h)                        
16 gravity_potential       [m**2/s**2]  gravity_potential(h)              
17 h_topo_over_ell             [meter]  geoid + topo over geoid (model)   
18 h_topo_over_geoid           [meter]  topo over geoid (from model)      
19 normal_gravity               [mGal]  normal_gravity(h)                 
20 normal_gravity_ell           [mGal]  normal_gravity(h=0)               
21 vertical_deflection_abs    [arcsec]  abs(vertical_deflection(h))       
22 vertical_deflection_ew     [arcsec]  vertical_deflection_east-west(h)  
23 vertical_deflection_ns     [arcsec]  vertical_deflection_north-south(h)
'''

class ICGEMTable:
    def __init__(self, filename: str, encoding: str = 'latin1'):
        self.filename = filename
        self.encoding = encoding
        self.metadata: Dict[str, str] = {}
        self.column_descriptions: Dict[int, str] = {}
        self.data: pd.DataFrame = pd.DataFrame()

    def read(self):
        with open(self.filename, 'r', encoding=self.encoding) as f:
            lines = f.readlines()

        data_start_index = 0
        in_column_description = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith("end_of_head"):
                data_start_index = i + 1
                break

            if re.match(r'^-+$', stripped):
                continue  # skip separator lines

            if stripped.startswith("description of columns"):
                in_column_description = True
                continue

            if in_column_description:
                match = re.match(r'(\d+)\s+(.+)', stripped)
                if match:
                    col_idx = int(match.group(1))
                    desc = match.group(2).strip()
                    self.column_descriptions[col_idx] = desc
                continue

            parts = stripped.split(None, 1)
            if len(parts) == 2:
                key, value = parts
                self.metadata[key.strip()] = value.strip()
        
        # Extract column names
        column_count = max(self.column_descriptions.keys())
        column_names = [self.column_descriptions.get(i + 1, f"col{i + 1}") for i in range(column_count)]

        # Read table data
        self.data = pd.read_csv(
            self.filename,
            skiprows=data_start_index,
            # delim_whitespace=True,
            sep=r'\s+',
            header=None,
            names=column_names,
            engine='python'
        )

    def get_metadata(self) -> Dict[str, str]:
        return self.metadata

    def get_data(self) -> pd.DataFrame:
        return self.data 

