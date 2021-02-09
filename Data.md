# Data
Users can specify the data of each visualization (i.e., `track`) through a `track.data` property.
```javascript
{
  "tracks":[{
    "data": {...}, // specify the data used in this track
    "mark": "rect",
    "color": ...,
    ...
  }]
}
```



## Supported Data Formats

<!-- Gosling currently supports six types of data formats: [CSV](#csv), [JSON](#json), [BigWig](#bigwig), [Multivec](#multivec), [BED](#bed), [Vector](#vector).-->


### CSV
```javascript
{
  "tracks": [
    {
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      ...,
  }]
}

```


| property           | type     | description                                                  |
| ------------------ | -------- | ------------------------------------------------------------ |
| type               | string   | **required**, `"csv"` for CSV files                          |
| url                | string   | **required**, specify the URL address of the data file       |
| separator          | string   | specify file separator, default=','                          |
| sampleLength       | number   | specify the number of rows loaded from the url. default=1000 |
| quantitativeFields | string[] | specify the name of quantitative data fields                 |
| chromosomeField    | string   | specify the name of chromosome data fields                   |
| genomicFields      | string[] | specify the name of genomic data fields                      |

### JSON

```javascript
{
  "tracks":[{
    "data": {
      "type": "json",
      "chromosomeField": "Chromosome",
      "genomicFields": [
          "chromStart",
          "chromEnd"
      ]
      "values": [
        {
          "Chromosome": "chr1",
          "chromStart": 0,
          "chromEnd": 2300000,
          "Name": "p36.33",
          "Stain": "gneg"
        },
        {
          "Chromosome": "chr1",
          "chromStart": 2300000,
          "chromEnd": 5300000,
          "Name": "p36.32",
          "Stain": "gpos25"
        }
        .....
        ]
    },
    ... // other configurations of this track
  }]
}
```

| property           | type                              | description                                                  |
| ------------------ | --------------------------------- | ------------------------------------------------------------ |
| type               | string                            | **required**, `"json"` for JSON files                        |
| values             | {[key:string]:number \| string}[] | **required**, values in the form of JSON                     |
| sampleLength       | number                            | specify the number of rows loaded from the url. default=1000 |
| quantitativeFields | string[]                          | specify the name of quantitative data fields                 |
| chromosomeField    | string                            | specify the name of chromosome data fields                   |
| genomicFields      | string[]                          | specify the name of genomic data fields                      |

### BigWig

```javascript
{
  "tracks":[{
    "data": {
      "url": 'https://s3.amazonaws.com/gosling-lang.org/data/4DNFIMPI5A9N.bw',
      "type": "bigwig",
      "column": "position",
      "value": "peak"
    },
    ... // other configurations of this track
  }]
}
```


| property | type   | description                                            |
| -------- | ------ | ------------------------------------------------------ |
| type     | string | **required**, `"bigwig"`                               |
| url      | string | **required**, specify the URL address of the data file |
| column   | string | **required**                                           |
| value    | string | **required**                                           |
| bin      | number | bin the genomic interval in tiles                      |
| start    | string |                                                        |
| end      | string |                                                        |

### Vector

```javascript
{
  "tracks":[{
    "data": {
      "url": 'https://resgen.io/api/v1/tileset_info/?d=VLFaiSVjTjW6mkbjRjWREA',
      "type": "vector",
      "column": "position",
      "value": "peak"
    },
    ... // other configurations of this track
  }]
}
```


| property | type   | description                                            |
| -------- | ------ | ------------------------------------------------------ |
| type     | string | **required**, `"vector"`                               |
| url      | string | **required**, specify the URL address of the data file |
| column   | string | **required**                                           |
| value    | string | **required**                                           |
| bin      | number | bin the genomic interval in tiles                      |
| start    | string |                                                        |
| end      | string |                                                        |

### Multivec


```javascript
{
  "tracks":[{
    "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "multivec",
        "row": "sample",
        "column": "position",
        "value": "peak",
        "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
    },
    ...// other configurations of this track
  }]
}
```

| property   | type     | description                                            |
| ---------- | -------- | ------------------------------------------------------ |
| type       | string   | **required**, `"multivec"`                             |
| url        | string   | **required**, specify the URL address of the data file |
| column     | string   | **required**                                           |
| row        | string   | **required**                                           |
| value      | string   | **required**                                           |
| categories | string[] |                                                        |
| bin        | number   | bin the genomic interval in tiles                      |
| start      | string   |                                                        |
| end        | string   |                                                        |

### BED
```javascript
{
  "tracks":[{
    "data": {
      "url": "https://higlass.io/api/v1/tileset_info/?d=OHJakQICQD6gTD7skx4EWA",
      "type": "bed",
      "genomicFields": [
          {"index": 1, "name": "start"},
          {"index": 2, "name": "end"}
      ],
      "valueFields": [
          {"index": 5, "name": "strand", "type": "nominal"},
          {"index": 3, "name": "name", "type": "nominal"}
      ],
      "exonIntervalFields": [
          {"index": 12, "name": "start"},
          {"index": 13, "name": "end"}
      ]
    },
    ... // other configurations of this track
  }]
}
```

| property           | type                                                                 | description                                            |
| ------------------ | -------------------------------------------------------------------- | ------------------------------------------------------ |
| type               | string                                                               | **required**, `"bed"`                                  |
| url                | string                                                               | **required**, specify the URL address of the data file |
| genomicFields      | { index: number; name: string }[]                                    | **required**, specify the name of genomic data fields  |
| valueFields        | { index: number; name: string; type: 'nominal' \| 'quantitative' }[] |                                                        |
| exonIntervalFields | [{ index: number; name: string }, { index: number; name: string }]   |                                                        |




## Data Transform
Gosling supports data transform through a set of data filters.  
Only data points that pass the tests in all filters will be visualized.  


```javascript
{
  "tracks":[{
    "data": ...,
    // only use data whose type is 'gene' and whose strand is NOT '+' 
    "dataTransform": {
      filter: [
          { field: 'type', oneOf: ['gene'] },
          { field: 'strand', oneOf: ['+'], not: true }
      ]
  },
    "mark": "rect",
    ...,
  }]
}
```

Users can apply three types of filters: `oneOf`, `inRange`, `include`.
One filter has the following properties:
| property | type                 | description                                                                          |
| -------- | -------------------- | ------------------------------------------------------------------------------------ |
| field    | string               | **required**, a filter is applied based on the values of the specified data field    |
| inRange  | number[]             | check whether the value is in a number range                                         |
| oneOf    | string[] \| number[] | check whether the value is an element in the provided list                           |
| include  | string               | check whether the value includes a substring                                         |
| not      | boolean              | when `not = true`, apply a NOT logical operation to the filter test. default = false |

Apart from filters, users can aggregate data values (min, max, bin, mean, and count). [Read more about data aggregation](#x)