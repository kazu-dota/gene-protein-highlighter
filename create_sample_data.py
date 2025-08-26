#!/usr/bin/env python3
"""
サンプルテストデータ作成スクリプト
"""
import pandas as pd

# サンプルデータの作成
sample_data = {
    'Title': [
        'BRCA1 mutations in breast cancer',
        'p53 pathway analysis', 
        'EGFR targeted therapy',
        'Oncogene expression study',
        'Alzheimer\'s disease biomarkers'
    ],
    'Abstract': [
        'BRCA1 mutations are associated with p53 pathway disruption in breast cancer. The EGFR protein shows overexpression in lung cancer patients.',
        'Investigation of p53 tumor suppressor gene mutations in colorectal cancer. TP53 mutations lead to loss of DNA damage response.',
        'EGFR overexpression in non-small cell lung cancer patients responds to erlotinib treatment. HER2 protein levels correlate with prognosis.',
        'MYC oncogene amplification drives tumor cell proliferation. KRAS mutations are frequently found in pancreatic adenocarcinoma.',
        'Amyloid beta plaques and tau protein aggregation are hallmarks of Alzheimer\'s disease. ApoE4 allele increases disease risk.'
    ]
}

# DataFrameに変換
df = pd.DataFrame(sample_data)

# Excelファイルとして保存
df.to_excel('sample_data.xlsx', index=False)

print("Sample data sample_data.xlsx created successfully")
print(f"  - Rows: {len(df)}")
print(f"  - Columns: {list(df.columns)}")