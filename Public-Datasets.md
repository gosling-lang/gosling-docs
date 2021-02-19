*********This Page Is WIP*********

# Overview
To help using Gosling for the first time, this document provides some useful datasets that can be directly used in Gosling.

For the flexible data exploration, Gosling supports two different kinds of datasets:

1. **Plain Datasets**: For the convenience, Gosling allows to use several data formats directly in the system without requiring to preprocess data or set up a dedicated server (i.e., HiGlass server).

<!--This includes BigWig, BED, BEDPE, and we will be supporting more genomic file formats in the near future.-->
2. **Pre-aggregated Datasets**: To allow scalable data exploration, Gosling supports using HiGlass' preprocessed datasets which requires the dedicated HiGlass server.

In this document, we provide a list of public datasets in those two classes. For the pre-aggregated ones listed below, we provide them in our Gosling's server, so you do not need to set up your own HiGlass server to visualize them.

> **Tip.** When you are using online editor, you can check out a "Data Preview" panel on the right-bottom part of the interface to see how the actual data looks like.

## List of Plain Datasets
> Add as a table
- Type: CSV
- URL: 
- Description: hg38 cytoband
- Soruce: UCSC
---
> Support multiple of bigwigs
- Type: BigWig
- URL: https://s3.amazonaws.com/gosling-lang.org/data/4DNFIMPI5A9N.bw
- Source: 4DN (https://data.4dnucleome.org/files-processed/4DNFIMPI5A9N/#file-overview)
- [Start visualizing this data in the editor]()

## List of Pre-aggregated Datasets
- Type: Aggregated BED
- URL: 
- Description: hg38 gene annotation
- Source: 

---

> Need to confirm how many samples this data contains
- Type: Multivec (Originally, multiple bigwig files)
- URL: 
- Description: Multiple samples of ChIP-seq and DNase-seq analysis
- Source: Cistrome Browser (http://cistrome.org/db/#/)

---

- Type: Multivec (Originally, a FASTA file)
- URL: 
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