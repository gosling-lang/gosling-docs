## Create your first visualization using Gosling ＼（＾▽＾）／

This tutorial will guide you step by step in writing the JSON specification to create an interactive visualization in Gosling.

## Loading Data
In this tutorial, we use a CSV data ([the complete data file](https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv)).


|Chromosome|chromStart|chromEnd|Name|Stain|
|---|---|---|---|--|
|chr1|0|2300000|p36.33|gneg|
|chr1|2300000|5300000|p36.32|gpos25|
|chr1|5300000|7100000|p36.31|gneg|
|...|


To start with, we load this data through URL to the visualization (i.e., a `track`).
```json
{
    "tracks":[{
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        }
    }]
}
```

## Encoding Data with Marks
In this tutorial, we use a `rect` mark to encode the start and end position of 

## Superposing Multiple Marks

## Data Transform

## Customize Style

## More Examples