# Gene/Protein Recognition and Excel Highlighting Tool

🧬 AI-powered tool for automatic recognition and highlighting of gene/protein names in Excel files using scispaCy.

## Features

- **Automatic Recognition**: Detects genes, proteins, chemicals, and diseases in biomedical text
- **Excel Integration**: Processes Excel files and highlights recognized entities
- **Color-coded Results**: Different colors for different entity types
- **Interactive Demo**: Run without arguments to see recognition capabilities
- **Flexible Processing**: Target specific columns or entire files

## Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Download scispaCy model
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bionlp13cg_md-0.5.4.tar.gz
```

### 2. Demo Run

```bash
python gene_highlighter.py
```

This will show:
- Analysis of 5 sample biomedical texts
- Recognition results with entity positions
- Statistics summary
- Excel file preview (if sample_data.xlsx exists)

### 3. Process Excel Files

```bash
# Process entire file
python gene_highlighter.py your_file.xlsx

# Process specific columns
python gene_highlighter.py your_file.xlsx -c "Abstract" "Title"

# Specify output file
python gene_highlighter.py input.xlsx -o highlighted_results.xlsx
```

## Entity Types & Colors

| Entity Type | Color | Description | Examples |
|-------------|-------|-------------|----------|
| **GENE_OR_GENE_PRODUCT** | 🟡 Yellow | Genes and gene products | BRCA1, p53, EGFR |
| **PROTEIN** | 🟢 Green | Proteins | Various protein names |
| **CHEMICAL** | 🟠 Orange | Chemical compounds | Drug names, chemicals |
| **DISEASE** | 🩷 Pink | Diseases and conditions | Cancer types, disorders |

## Usage Examples

### Command Line Options

```bash
python gene_highlighter.py [input_file] [options]

Options:
  -o, --output     Output Excel file path
  -c, --columns    Target column names (space-separated)
  -s, --sheet      Sheet name to process
  -m, --model      scispaCy model name
```

### Example Commands

```bash
# Basic usage
python gene_highlighter.py research_papers.xlsx

# Process only Abstract column
python gene_highlighter.py papers.xlsx -c Abstract

# Multiple columns with custom output
python gene_highlighter.py data.xlsx -c "Title" "Abstract" "Methods" -o results.xlsx

# Specific sheet
python gene_highlighter.py workbook.xlsx -s "Research Data"
```

## Sample Output

When you run the demo (`python gene_highlighter.py`), you'll see:

```
============================================================
DEMO: Gene/Protein Recognition Test
============================================================

1. Text Analysis Results:
----------------------------------------
Sample 1:
Text: BRCA1 mutations are associated with p53 pathway...
Found: 2 entities
  -> 'BRCA1' [GENE_OR_GENE_PRODUCT] (pos: 0-5)
  -> 'p53' [GENE_OR_GENE_PRODUCT] (pos: 36-39)

2. Summary Statistics:
----------------------------------------
Total entities found: 7
GENE_OR_GENE_PRODUCT: 7 total, 7 unique
```

## Requirements

- Python 3.7+
- pandas
- openpyxl
- spacy
- scispacy
- en_ner_bionlp13cg_md model

## Files Structure

```
gene-protein-highlighter/
├── gene_highlighter.py      # Main application
├── requirements.txt         # Python dependencies
├── create_sample_data.py    # Sample data generator
├── sample_data.xlsx         # Demo data
└── README.md               # This file
```

## Technical Details

- **NLP Model**: Uses scispaCy's `en_ner_bionlp13cg_md` for biomedical NER
- **Entity Recognition**: Identifies genes, proteins, chemicals, diseases
- **Excel Processing**: Uses openpyxl for cell highlighting
- **Color Coding**: PatternFill for visual distinction
- **Legend**: Automatically adds color legend to Excel files

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [scispaCy](https://allenai.github.io/scispacy/) for biomedical NLP models
- [spaCy](https://spacy.io/) for natural language processing
- Allen Institute for AI for the biomedical models