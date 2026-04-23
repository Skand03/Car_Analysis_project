# Contributing to Car Price Prediction System

Thank you for your interest in contributing to the Car Price Prediction System! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** - Descriptive and specific
- **Steps to reproduce** - Detailed reproduction steps
- **Expected behavior** - What should happen
- **Actual behavior** - What actually happens
- **Screenshots** - If applicable
- **Environment** - OS, Python version, browser, etc.

**Example:**
```
Title: Prediction fails for CNG fuel type

Steps to reproduce:
1. Select CNG as fuel type
2. Enter 50000 km
3. Click Predict Price
4. Error appears

Expected: Price prediction
Actual: Error message "Invalid fuel type"

Environment: Windows 11, Python 3.9, Chrome 120
```

### Suggesting Enhancements

Enhancement suggestions are welcome! Include:

- **Clear description** - What you want to add/change
- **Use case** - Why this would be useful
- **Examples** - How it would work
- **Alternatives** - Other solutions considered

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
6. **Push to your fork**
7. **Open a Pull Request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Car_Analysis_project.git
cd Car_Analysis_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🔄 Pull Request Process

1. **Update documentation** - If you change functionality
2. **Add tests** - For new features
3. **Follow style guide** - PEP 8 for Python
4. **Update README** - If needed
5. **One feature per PR** - Keep PRs focused
6. **Link issues** - Reference related issues

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Dependent changes merged

## 📝 Style Guidelines

### Python Code Style

Follow PEP 8 with these specifics:

```python
# Good
def predict_car_price(insurance, fuel, kms, ownership, transmission):
    """
    Predict car price based on features.
    
    Args:
        insurance: Insurance type (0-3)
        fuel: Fuel type (0-2)
        kms: Kilometers driven
        ownership: Ownership status (0-4)
        transmission: Transmission type (0-1)
    
    Returns:
        Predicted price in lakhs
    """
    test_data = [[insurance, fuel, kms, ownership, transmission]]
    return int(model.predict(test_data)[0])

# Bad
def predict(i,f,k,o,t):
    return int(model.predict([[i,f,k,o,t]])[0])
```

### Code Organization

```python
# 1. Standard library imports
import os
import sys

# 2. Third-party imports
import streamlit as st
import pandas as pd

# 3. Local imports
from utils import helper_function

# 4. Constants
MAX_KMS = 500000
MIN_KMS = 0

# 5. Functions
def main():
    pass
```

### Documentation

- Add docstrings to all functions
- Use clear variable names
- Comment complex logic
- Update README for new features

## 💬 Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good commits
git commit -m "feat(model): Add Random Forest algorithm option"
git commit -m "fix(ui): Resolve dropdown selection bug"
git commit -m "docs(readme): Update installation instructions"

# Bad commits
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdfgh"
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_model.py

# Run with coverage
pytest --cov=app
```

### Writing Tests

```python
def test_predict_price():
    """Test price prediction function."""
    result = predict_car_price(0, 0, 50000, 0, 1)
    assert isinstance(result, int)
    assert result > 0
```

## 📚 Additional Resources

- [Python PEP 8 Style Guide](https://pep8.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

## ❓ Questions?

- Open an issue with the `question` label
- Email: skand@example.com
- GitHub Discussions: [Join Discussion](https://github.com/Skand03/Car_Analysis_project/discussions)

## 🎉 Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Credited in documentation

Thank you for contributing! 🙏
