# Ragnar Leg Assignment

This code will assign leg numbers to runners based on their top 3 preferences using the SciPy library's `linear_sum_assignment` Hungarian Algorithm

References

- [Hungarian Assignment](https://en.wikipedia.org/wiki/Hungarian_algorithm)
- [SciPy Linear Sum Assignment](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html)

## Prerequisites

- Python
- Chocolatey
  - Virtualenv
- VSCode (optional)
- Poll your runners for their top 3 leg preferences

## Running the code

1. Create and set up a virtual environment

```python
python -m venv venv
./venv/scripts/activate.ps1
pip install -r requirements.txt
```

Then, ensure that VSCode is using the correct version of python with your virtualenv. For example: `Python 3.8.2 64-bit ('venv': venv)`

1. Replace your runner names and leg numbers

Edit the "runners" Ordered Dictionary with your runners names and preferred legs (1-12).

1. Run the code from Powershell or VSCode
    - python -m ragnar_leg_assignments
    - or use included launch.json file for VSCode
