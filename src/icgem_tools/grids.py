import numpy as np
import xarray as xr
from typing import Dict


class ICGEMGrid:
    def __init__(self, filename: str, encoding: str = 'latin1'):
        self.filename = filename
        self.encoding = encoding
        self.metadata: Dict[str, str] = {}
        self.column_descriptions: Dict[int, str] = {}
        self.grid: xr.DataArray = xr.DataArray()
        
    def read(self):

        with open(self.filename, 'r', encoding=self.encoding) as f:
            lines = f.readlines()

        data_start_index = 0

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith("end_of_head"):
                data_start_index = i + 1
                break

            if stripped.startswith("[deg.]"):
                data_start_index = i + 1
                continue

            if stripped.startswith("longitude"):
                data_start_index = i + 1
                continue

            parts = stripped.split(None, 1)
            if len(parts) == 2:
                key, value = parts
                self.metadata[key.strip()] = value.strip()
            
        # Read grid data
        grid_data = np.loadtxt(self.filename, skiprows=data_start_index)

        self.grid = self._grid_to_xarray(grid_data)

    def _grid_to_xarray(self, grid_data):
        """
        Convert grid data to xarray.Dataset
        grid_data: array with columns [lon, lat, height, value]
        """

        value_name = self.metadata.get('functional')
        value_unit = self.metadata.get('unit')
        
        lons = grid_data[:, 0]
        lats = grid_data[:, 1]
        heights = grid_data[:, 2]
        value = grid_data[:, 3]
        
        # Define unique coordinates and sort them
        unique_lons = np.sort(np.unique(lons))
        unique_lats = np.sort(np.unique(lats))
        
        # Initialize arrays for data
        height_grid = np.full((len(unique_lats), len(unique_lons)), np.nan)
        value_grid = np.full((len(unique_lats), len(unique_lons)), np.nan)
        
        # Fill the arrays with data
        for lon, lat, height, value in grid_data:
            lat_idx = np.searchsorted(unique_lats, lat)
            lon_idx = np.searchsorted(unique_lons, lon)
            height_grid[lat_idx, lon_idx] = height
            value_grid[lat_idx, lon_idx] = value

        # Create xarray Dataset with two variables
        ds = xr.Dataset({
            'height': (['lat', 'lon'], height_grid),
            'value': (['lat', 'lon'], value_grid)
        }, coords={
            'lat': unique_lats,
            'lon': unique_lons
        })

        # add attributes
        ds.attrs['source_file'] = self.filename
        for key, value in self.metadata.items():
            ds.attrs[key] = value
        ds['height'].attrs['units'] = 'm'
        ds['value'].attrs['units'] = value_unit
        ds['height'].attrs['long_name'] = 'h_over_geoid'
        ds['value'].attrs['long_name'] = value_name

        return ds

    def get_metadata(self) -> Dict[str, str]:
        return self.metadata

    def get_grid(self) -> xr.DataArray:
        return self.grid

