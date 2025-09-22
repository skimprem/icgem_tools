# ICGEM Tools

A Python library for working with ICGEM (International Centre for Global Earth Models) format files.

## Description

ICGEM Tools provides utilities for:

- Reading ICGEM format files
- Writing models to ICGEM format

## Installation

### From source

```bash
git clone <repository-url>
cd icgem_tools
pip install -e .
```

### For development

```bash
pip install -e ".[dev]"
```

## Quick Start

### Reading an ICGEM file

```python
from icgem_tools.points import ICGEMTable
from icgem_tools.grids import ICGEMGrid

# Load data file (*.dat)
table_object = ICGEMTable('path/to/file.dat')
table_object.read()
data = table_object.data

# Get table information
print(data.metadata)

# Load a grid file (*.gdf)
grid_object = ICGEMGrid('path/to/grid.gdf)
grid_object.read()
grid = grid_object.grid

# Get grid informatioin
print(grid_object.metadata)
```

### Writing an ICGEM file

At the development stage

## Project Structure

```text
icgem_tools/
├── src/icgem_tools/      # Main library
│   ├── __init__.py       # Package initialization
│   ├── coeffs.py         # Coefficient handling
│   ├── grids.py          # Grid data processing
│   └── points.py         # Point data processing
├── examples/             # Usage examples
├── docs/                 # Documentation
├── data/                 # Test data
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## API Reference

### Main Classes

- **ICGEMTable**: Reading and writing point data
- **ICGEMGrid**: Reading and writing grid data  
- **ICGEMCoeff**: Working with coefficients

### Reading Methods

- `read()`: Complete file reading

### Writing Methods

At the development stage

## License

MIT License - see [LICENSE](LICENSE) file

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

- Author: Roman Sermiagin
- Email: <roman.sermiagin@gmail.com>
- GitHub: [repository link]
