## Data
### JSONData
The JSON data format allows users to include data directly in the Gosling's JSON specification.
**properties of JSONData**
| property | type | description |
|----|----|-----|
|type| string | **required**. must be `"json"`. define data type |
|values| array | **required**. values in the form of JSON |
|chromosomeField| string | specify the name of chromosome data fields |
|genomicFields| array of string | specify the name of genomic data fields |
|quantitativeFields| array of string | specify the name of quantitative data fields |
|sampleLength| number | specify the number of rows loaded from the url. default=1000 |

### CSVData
Any small enough tabular data files, such as tsv, csv, BED, BEDPE, and GFF, can be loaded using "csv" data specification.
**properties of CSVData**
| property | type | description |
|----|----|-----|
|type| string | **required**. must be `"csv"` |
|url| string | **required**. specify the URL address of the data file |
|chromosomeField| string | specify the name of chromosome data fields |
|genomicFields| array of string | specify the name of genomic data fields |
|headerNames| array of string | specify the names of data fields if a CSV file is headerless |
|quantitativeFields| array of string | specify the name of quantitative data fields |
|sampleLength| number | specify the number of rows loaded from the url. default=1000 |
|separator| string | specify file separator, default=',' |

### BIGWIGData
**properties of BIGWIGData**
| property | type | description |
|----|----|-----|
|column| string | **required**. assign a field name of the middle position of genomic intervals |
|type| string | **required**. must be `"bigwig"` |
|url| string | **required**. specify the URL address of the data file |
|value| string | **required**. assign a field name of quantitative values |
|binSize| number | Binning the genomic interval in tiles (unit size: 256) |
|end| string | assign a field name of the end position of genomic intervals |
|start| string | assign a field name of the start position of genomic intervals |

### MultivecData
Two-dimensional quantitative values, one axis for genomic coordinate and the other for different samples, can be converted into HiGlass' `"multivec"` data. For example, multiple BigWig files can be converted into a single multivec file. You can also convert sequence data (FASTA) into this format where rows will be different nucleotide bases (e.g., A, T, G, C) and quantitative values represent the frequency. Find out more about this format at [HiGlass Docs](https://docs.higlass.io/data_preparation.html#multivec-files).
**properties of MultivecData**
| property | type | description |
|----|----|-----|
|column| string | **required**. assign a field name of the middle position of genomic intervals |
|row| string | **required**. assign a field name of samples |
|type| string | **required**. must be `"multivec"` |
|url| string | **required**. specify the URL address of the data file |
|value| string | **required**. assign a field name of quantitative values |
|binSize| number | Binning the genomic interval in tiles (unit size: 256) |
|categories| array of string | assign names of individual samples |
|end| string | assign a field name of the end position of genomic intervals |
|start| string | assign a field name of the start position of genomic intervals |

### BEDDBData
Regular BED or similar files can be pre-aggregated for the scalable data exploration. Find our more about this format at [HiGlass Docs](https://docs.higlass.io/data_preparation.html#bed-files).
**properties of BEDDBData**
| property | type | description |
|----|----|-----|
|genomicFields| array of object | **required**. specify the name of genomic data fields. . Each object in the array follows the format {"index": "number", "name": "string"} |
|type| string | **required**. must be `"beddb"` |
|url| string | **required**. specify the URL address of the data file |
|valueFields| array of object | specify the column indexes, field names, and field types. . Each object in the array follows the format {"index": "number", "name": "string", "type": "string"} |

### VectorData
One-dimensional quantitative values along genomic position (e.g., bigwig) can be converted into HiGlass' `"vector"` format data. Find out more about this format at [HiGlass Docs](https://docs.higlass.io/data_preparation.html#bigwig-files).
**properties of VectorData**
| property | type | description |
|----|----|-----|
|column| string | **required**. assign a field name of the middle position of genomic intervals |
|type| string | **required**. must be `"vector"` |
|url| string | **required**. specify the URL address of the data file |
|value| string | **required**. assign a field name of quantitative values |
|binSize| number | Binning the genomic interval in tiles (unit size: 256) |
|end| string | assign a field name of the end position of genomic intervals |
|start| string | assign a field name of the start position of genomic intervals |

### MatrixData
**properties of MatrixData**
| property | type | description |
|----|----|-----|
|type| string | **required**. must be `"matrix"` |
|url| string | **required** |

### BAMData
Binary Alignment Map (BAM) is the comprehensive raw data of genome sequencing; it consists of the lossless, compressed binary representation of the Sequence Alignment Map-files.
**properties of BAMData**
| property | type | description |
|----|----|-----|
|indexUrl| string | **required**. URL link to the index file of the BAM file |
|type| string | **required**. must be `"bam"` |
|url| string | **required**. URL link to the BAM data file |

