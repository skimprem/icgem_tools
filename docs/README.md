# ICGEM Tools Documentation

This folder contains documentation for the ICGEM Tools library.

## Structure

- `api/` - Auto-generated API documentation
- `user_guide/` - User guide
- `tutorials/` - Tutorials and examples
- `reference/` - Reference information about ICGEM format

## Building Documentation

To build documentation use Sphinx:

```bash
pip install -e ".[docs]"
cd docs/
make html
```

Documentation will be available at `docs/_build/html/index.html`

## Contents

- Introduction to ICGEM format
- API Reference
- Usage examples
- FAQ and troubleshooting
- Developer information