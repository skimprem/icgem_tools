"""
Example of reading an ICGEM file and extracting basic information.

This script demonstrates:
- Reading an ICGEM file
- Getting model metadata
- Accessing spherical harmonics
- Outputting basic statistics
"""

import os
from icgem_tools.points import ICGEMTable
from icgem_tools.grids import ICGEMGrid


def table():
    """Main function demonstrating ICGEM data file reading."""
    
    # Path to example file (replace with real path)
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'height_anomaly_EIGEN-6C4_astana.dat')
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Create a test ICGEM table file or specify path to existing file.")
        return
    
    try:
        # Create icgem_table object
        icgem_table = ICGEMTable(file_path)
        icgem_table.read()
        
        # Read header only (fast way to get metadata)
        print("=== Reading metadata ===")
        metadata = icgem_table.metadata
        
        for key, value in metadata.items():
            print(f"{key}: {value}")
       
        # Read complete model
        print("\n=== Reading complete data ===")
        data = icgem_table.data
        
        print(data)

    except Exception as e:
        print(f"Error reading ICGEM file: {e}")


def grid():
    """Main function demonstrating ICGEM grid file reading."""
    
    # Path to example file (replace with real path)
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'height_anomaly_EIGEN-6C4_astana.gdf')

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Create a test ICGEM grid file or specify path to existing file.")
        return
    
    try:
        # Create icgem_table object
        icgem_grid = ICGEMGrid(file_path)
        icgem_grid.read()
        
        # Read header only (fast way to get metadata)
        print("=== Reading metadata ===")
        metadata = icgem_grid.metadata
        
        for key, value in metadata.items():
            print(f"{key}: {value}")
       
        # Read complete model
        print("\n=== Reading complete data ===")
        grid = icgem_grid.grid
        
        print(grid)

    except Exception as e:
        print(f"Error reading ICGEM file: {e}")

if __name__ == "__main__":
    table()
    grid()