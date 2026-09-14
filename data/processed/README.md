# Mixed Features README

## Purpose

This document explains how the mixed feature files are built from NoEnvelope and Hilbert feature sets, which files were used for each database, and how to interpret columns in the final mixed CSV files.

## Processing Summary

Mixed files were regenerated using:
- NoEnv source for: MNF, mDWT, ZC, SSC, TD, WL, MAVS
- Hilbert source for all other signal feature suffixes

Final mixed files generated:
- preprocessed_data/features_mixed_NinaProDB1_200ms.csv
- preprocessed_data/features_mixed_NinaProDB2_200ms.csv
- preprocessed_data/features_mixed_NinaProDB3_200ms.csv
- preprocessed_data/features_mixed_NinaProDB4_200ms.csv
- preprocessed_data/features_mixed_NinaProDB5_200ms.csv
- preprocessed_data/features_mixed_NinaProDB7_200ms.csv

Feature-source mapping report generated:
- preprocessed_data/feature_source_map_DB1_DB2_DB3_DB4_DB5_DB7.csv

## What Is NoEnv vs Hilbert

NoEnv
- Features extracted directly from raw-window signals without Hilbert envelope processing.
- Better for sign and transition dependent features and other morphology-sensitive descriptors.

Hilbert
- Features extracted after Hilbert envelope processing.
- Better for envelope/amplitude stability features.

## Feature Source Assignment in Mixed Files

From NoEnv
- MAVS
- MNF
- SSC
- TD
- WL
- ZC
- mDWT

From Hilbert
- CoV
- Energy
- IAV
- Kurtosis
- MAV
- Max
- Mean
- Median
- Min
- RMS
- Range
- Skewness
- VAR

## Input and Output Files by Database

DB1
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB1_200ms.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB1_200ms.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB1_200ms.csv

DB2
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB2_200ms.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB2_200ms.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB2_200ms.csv

DB3
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB3_200ms.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB3_200ms.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB3_200ms.csv

DB4
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB4_200ms.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB4_200ms.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB4_200ms.csv

DB5
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB5_200ms.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB5_200ms.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB5_200ms.csv

DB7
- Hilbert input: preprocessed_data/features_Hilbert_NinaProDB7_200ms_20260410_153051.csv
- NoEnv input: preprocessed_data/features_NoEnvelope_NinaProDB7_200ms_20260410_172342.csv
- Mixed output: preprocessed_data/features_mixed_NinaProDB7_200ms.csv

Note
- DB7 inputs are timestamped. The mixing script resolves the newest matching file automatically when exact non-timestamped names are not present.

## Final Column Structure

Each mixed CSV contains metadata columns plus per-channel feature columns.

Metadata columns (all DBs)
- window_size_samples
- window_size_ms
- window_index
- stimulus
- subject

Signal feature column naming
- Channel N_FeatureSuffix
- Example format: Channel 4_RMS

Per-database column layout

DB1
- Total columns: 213
- Signal columns: 208
- Metadata columns: 5
- Channels present: 1 to 8

DB2
- Total columns: 213
- Signal columns: 208
- Metadata columns: 5
- Channels present: 1 to 8

DB3
- Total columns: 213
- Signal columns: 208
- Metadata columns: 5
- Channels present: 1 to 8

DB4
- Total columns: 317
- Signal columns: 312
- Metadata columns: 5
- Channels present: 1 to 12

DB5
- Total columns: 213
- Signal columns: 208
- Metadata columns: 5
- Channels present: 1 to 8

DB7
- Total columns: 213
- Signal columns: 208
- Metadata columns: 5
- Channels present: 1 to 8

## Merge Keys Used to Build Mixed Files

Rows are aligned between Hilbert and NoEnv using:
- subject
- stimulus
- window_index
- window_size_samples
- window_size_ms

Only aligned rows are kept in output.

## Scripts Used

- utilities/mix_features_db2_db4_db7.py
  - Generates mixed files for any list of DB ids with argument --dbs
- utilities/report_feature_sources.py
  - Generates a feature-to-source mapping CSV and prints a quick summary
