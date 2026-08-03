# Folder Structure

## Folder structure v1.0

```mermaid
flowchart TD
    A[superstore-analytics]

    A --> B[data]
    B --> B1[raw]
    B1 --> B2[superstore_clean.csv]
    B  --> B3[processed]
    B3 --> B4[superstore_clean.csv]

    A --> C[notebooks]
    C --> C1[00_questions.ipynb]
    C --> C2[01_sample.ipynb]

    A --> D[scripts]

    A --> E[db]
    E --> E1[(superstore.db)]
    E --> E2[db_connection.py]

    A --> F[dashboards]
  

    A --> G[reports]
    G --> G2[figures]

    A --> H[docs]
    H --> H1[diagrams]
    H1 --> H2[folder_structure.md]


    A --> I[README.md]
    A --> J[requirements.txt]
```