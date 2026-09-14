# Master README

## Purpose

This folder contains the master tables that consolidate the main subject information used in the EMG analysis workflow. These files are intended to provide a more structured and reusable view of the dataset for exploratory analysis and downstream processing.

## What this folder contains

The folder includes the following files:

- intact_subjects.csv
- amputated_subjects.csv
- intact_signals.csv
- amputated_signals.csv

## General structure

### Subject-level tables

The files ending in subjects.csv contain participant-level metadata for the intact and amputated groups. They include relevant variables such as:

- subject identifier,
- hand condition,
- handedness,
- age,
- height,
- weight,
- clinical descriptors,
- database reference.

These tables are useful for understanding the study population and for performing descriptive comparisons between groups.

### Signal-related tables

The files ending in signals.csv contain the larger datasets associated with the corresponding subject groups. They are used when the analysis needs to work directly with the experimental signal information together with the available subject context.

## Role in the project

This folder acts as a central reference point for the main analytical datasets. It is commonly used to:

- inspect the curated subject information,
- compare intact and amputated cohorts,
- support notebook-based exploratory analysis,
- prepare data for more advanced processing steps.

## Notes

The master tables are designed to make the project easier to navigate by grouping the most relevant data sources in a more compact and interpretable form.
