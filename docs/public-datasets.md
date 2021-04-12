---
title: Public Datasets
---
To help using Gosling for the first time, this document provides some useful datasets that can be directly used in Gosling.

For the flexible data exploration, Gosling supports two different kinds of datasets:

1. **Plain Datasets**: For the convenience, Gosling allows to use several data formats directly in the system without requiring to preprocess data or set up a dedicated server (i.e., HiGlass server).

<!--This includes BigWig, BED, BEDPE, and we will be supporting more genomic file formats in the near future.-->
2. **Pre-aggregated Datasets**: To allow scalable data exploration, Gosling supports using HiGlass' preprocessed datasets which requires the dedicated HiGlass server.

In this document, we provide a list of public datasets in those two classes. For the pre-aggregated ones listed below, we provide them in our Gosling's server, so you do not need to set up your own HiGlass server to visualize them.

> **Tip.** When you are using online editor, you can check out a "Data Preview" panel on the right-bottom part of the interface to see how the actual data looks like.

## List of Plain Datasets
- Type: CSV
- URL: https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv
- Description: hg38 cytoband
- Soruce: UCSC
---
- Type: BigWig
- URL: https://s3.amazonaws.com/gosling-lang.org/data/4DNFIMPI5A9N.bw
- Source: 4DN (https://data.4dnucleome.org/files-processed/4DNFIMPI5A9N/#file-overview)
---
- Type: CSV
- URL: https://s3.amazonaws.com/gosling-lang.org/data/COVID/NC_045512.2-Genes.csv
- Description: Gene Annotations of SARS-CoV-2 in NC_045512.2
- Source: https://genome.ucsc.edu/covid19.html
---
- Type: CSV
- URL: https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/circos-segdup-edited.txt
- Description: Circos Segmental Duplication
- Source: https://github.com/nicgirault/circosJS/blob/master/demo/data/segdup.csv
## List of Pre-aggregated Datasets
- Type: BEDDB (Originally, a bed file)
- URL: https://server.gosling-lang.org/api/v1/tileset_info/?d=gene-annotation
- Description: hg38 gene annotation
- Source: http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/

---
- Type: Multivec (Originally, multiple bigwig files)
- URL: https://server.gosling-lang.org/api/v1/tileset_info/?d=cistrome-multivec
- Description: Multiple samples of ChIP-seq and DNase-seq analysis
- Source: Cistrome Browser (http://cistrome.org/db/#/)

---

- Type: Multivec (Originally, a FASTA file)
- URL: https://server.gosling-lang.org/api/v1/tileset_info/?d=sequence-multivec
- Description: hg38 sequence
- Source: UCSC (https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/)

---

- Type: BEDDB (Originally, a VCF file)
- URL: https://server.gosling-lang.org/api/v1/tileset_info/?d=clinvar-beddb
- Description: hg38 ClinVar data
- Source: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

---
- Type: Multivec (Originally, a VCF file)
- URL: https://server.gosling-lang.org/api/v1/tileset_info/?d=clinvar-multivec
- Description: Density of ClinVar data by seven pathogenicity categories 
- Source: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/

```ts
categories: [
    'Benign',
    'Benign/Likely_benign',
    'Likely_benign',
    'Uncertain_significance',
    'Likely_pathogenic',
    'Pathogenic/Likely_pathogenic',
    'Pathogenic',
    'risk_factor',
    'Conflicting_interpretations_of_pathogenicity'
]
```
