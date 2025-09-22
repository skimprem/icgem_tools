# ICGEM Tools

A Python library for working with ICGEM (International Centre for Global Earth Models) format files.

## Description

ICGEM Tools provides utilities for:

- Reading ICGEM format files
- Writing models to ICGEM format
- Processing spherical harmonic coefficients
- Validating gravitational field models

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
from icgem_tools import ICGEMReader

# Create reader and read file
reader = ICGEMReader()
model = reader.read_file('path/to/model.gfc')

# Get model information
print(model.summary())

# Get a coefficient
coeff = model.get_coefficient(degree=2, order=0)
print(f"C20 = {coeff.c_coefficient}")
```

### Writing an ICGEM file

```python
from icgem_tools import ICGEMWriter, GravityModel, ModelMetadata

# Create model metadata
metadata = ModelMetadata(
    product_type="gravity_field",
    modelname="test_model",
    earth_gravity_constant=3.986004418e14,
    radius=6378136.3,
    max_degree=10
)

# Create model and add coefficients
model = GravityModel(metadata)
model.add_coefficient(degree=0, order=0, c_coeff=1.0, s_coeff=0.0)
model.add_coefficient(degree=2, order=0, c_coeff=-4.84166774e-4, s_coeff=0.0)

# Write to file
writer = ICGEMWriter()
writer.write_file(model, 'output_model.gfc')
```

### Working with coefficients

```python
# Get coefficient matrices
C_matrix, S_matrix = model.coefficients.get_coefficient_matrix()

# Iterate through coefficients of a specific degree
for coeff in model.coefficients.get_coefficients_by_degree(2):
    print(f"C{coeff.degree}{coeff.order} = {coeff.c_coefficient}")
```

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
├── requirements.txt      # Dependencies
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## API Reference

### Main Classes

- **ICGEMTable**: Reading and writing point data
- **ICGEMGrid**: Reading and writing grid data  
- **ICGEMCoeff**: Working with coefficients

### Reading Methods

- `read_file()`: Complete file reading
- `read_header_only()`: Header only reading
- `iter_data()`: Streaming data reading

### Writing Methods

- `write_file()`: Write complete data
- `write_subset()`: Write data subset
- `write_ascii_table()`: Write in tabular format## Requirements

- Python 3.8+
- NumPy >= 1.20.0
- SciPy >= 1.7.0
- Pandas >= 1.3.0

## Development

### Setting up development environment

```bash
# Clone repository
git clone <repository-url>
cd icgem_tools

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Code formatting

```bash
# Format with black
black src/ examples/

# Sort imports
isort src/ examples/

# Type checking
mypy src/
```

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
