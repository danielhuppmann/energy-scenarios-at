# Workflows for Austrian energy and emissions scenarios

[![license](https://img.shields.io/badge/License-MIT-blue)](https://github.com/iiasa/energy-scenarios-at/blob/main/LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) 
[![pytest](https://img.shields.io/github/actions/workflow/status/iiasa/energy-scenarios-at/validation.yml?logo=GitHub&label=pytest)](https://github.com/iiasa/energy-scenarios-at/actions/workflows/validation.yml) 
 
Copyright 2026 IIASA Scenario Services team and contributing modeling teams
 
This repository is licensed under the [MIT License](LICENSE). 

## Overview

This is a workflow repository for definitions and processing related to the development and analysis
of Austrian energy and emissions scenarios.


> [!TIP]
> For *users not comfortable working with GitHub repositories and yaml files*,
> the definitions for this project are available for download as an xlsx spreadsheet
> at https://files.ece.iiasa.ac.at/energy-scenarios-at/energy-scenarios-at-template.xlsx.

### Project nomenclature

The folder `definitions` can contain the project nomenclature, i.e., list of allowed
variables and regions, for use in the validation workflow. See the **nomenclature**
package for more information ([link](https://github.com/iamconsortium/nomenclature)).

The folder `mappings` can contain model mappings that are used to register models and
define how results should be processed upon upload to a Scenario Explorer.

### Workflow

The module `workflow.py` has a function `main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:`.

Per default, this function takes an **IamDataFrame** and returns it without
modifications. [Read the docs](https://pyam-iamc.readthedocs.io) for more information
about the **pyam** package for scenario analysis and data visualization.

## Funding acknowledgement

This work builds on scenario analysis compiled for the [Second Austrian Assessment Report
on Climate Change (AAR2)](https://aar2.ccca.ac.at/en) and was initiated as part of the ACRP
Project "INFRA-ENSURE" funded by the Austrian [Climate and Energy Fund](https://www.klimafonds.gv.at).
