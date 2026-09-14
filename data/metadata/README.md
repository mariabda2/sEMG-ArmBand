# Metadata README

## Purpose

This folder contains the subject-level metadata tables used to describe the participants in the EMG datasets. These files provide the demographic, anthropometric, and clinical context needed to understand the subjects before analyzing the signals.

## What this folder contains

The folder includes one CSV file per database:

- DB1SubjectData.csv
- DB2SubjectData.csv
- DB3SubjectData.csv
- DB4SubjectData.csv
- DB5SubjectData.csv
- DB7SubjectData.csv

Each file stores information about the participants associated with that specific database.

## Typical contents

The metadata files generally include fields such as:

- Subject identifier
- Hand condition
- Handedness
- Gender
- Age
- Height
- Weight

These variables are used in the exploratory analysis notebook to compare groups, describe the sample, and support interpretation of the EMG recordings.

## Role in the project

This folder is mainly used for:

- characterizing the study population,
- comparing intact and amputated subjects,
- preparing descriptive analyses in the notebooks,
- linking subject information to the experimental datasets.

## Notes

The files in this folder are typically smaller and easier to inspect than the signal datasets. They are especially useful for population-level summaries and metadata-based EDA.
