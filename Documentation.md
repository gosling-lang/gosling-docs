# Overview
Geminid is a declarative visualization grammar tailored for interative genomic visualizations.  
In Geminid, users construct visualizations through a JSON syntax.  
This documentation describes how to write the JSON specification language to create interactive visualizations.  
You are welcome to try the [Geminid online edtior](https://sehilyi.github.io/geminid/). 

  <!-- "title": "title of the visualizations",
  "subtitile": "subtitile of the visualizations",
  "description": "a detailed description of the visualizations",
  "width": 800,
  "height": 200,
  "static":  false -->

```javascript
// Geminid generates visualizations through a JSON specification language

{
  // one track is one visualization
  "tracks":[
    {
      // specify the data source and format of this track
      "data": {
        "url": ...,
        "type":...
      },
      // specify the mark types and visual encodings
      "mark": ...,
      "x": ...,
      ...
    },
    {
      ... // another track
    },
    ...
  ],
  // specify the layout and the grid-based arrangement of multiple tracks
  "layout":{
    ...
  }
}
```

# Table of Contents


- [Overview](#overview)
- [Table of Contents](#table-of-contents)
- [Data](#data)
  - [Supported Data Formats](#supported-data-formats)
    - [Multivec (HiGlass)](#multivec-higlass)
    - [BED (HiGlass)](#bed-higlass)
    - [BED](#bed)
    - [Vector (HiGlass)](#vector-higlass)
    - [CSV](#csv)
  - [Data Transform](#data-transform)
- [Mark](#mark)
  - [Types of Mark](#types-of-mark)
    - [Point](#point)
    - [Line](#line)
    - [Area](#area)
    - [Bar](#bar)
    - [Rect](#rect)
    - [Text](#text)
    - [Link](#link)
    - [Rule](#rule)
    - [Triangle](#triangle)
    - [Glyph](#glyph)
  - [Visual Channels of Mark](#visual-channels-of-mark)
    - [x](#x)
    - [xe](#xe)
    - [y](#y)
    - [ye](#ye)
    - [row](#row)
    - [size](#size)
    - [text](#text-1)
    - [color](#color)
    - [stroke](#stroke)
    - [strokeWidth](#strokewidth)
    - [opacity](#opacity)
    - [style](#style)
- [Tracks](#tracks)
  - [Layout](#layout)
  - [Arrangement](#arrangement)
    - [Grid-based arrangement](#grid-based-arrangement)
    - [Superposition](#superposition)
  - [Style](#style-1)
- [Interactions](#interactions)
  - [Linking Views](#linking-views)
  - [Zooming and Panning](#zooming-and-panning)
  - [Semantic Zoom](#semantic-zoom)
  - [Tooltip](#tooltip)





# Data

## Supported Data Formats

### Multivec (HiGlass)

```json
...
"data": {
    "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
    "type": "tileset"
},
"metadata": {
    "type": "higlass-multivec",
    "row": "sample",
    "column": "position",
    "value": "peak",
    "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
},
...
```
### BED (HiGlass)
```json
...
"data": {
    "url": "https://higlass.io/api/v1/tileset_info/?d=OHJakQICQD6gTD7skx4EWA",
    "type": "tileset"
},
"metadata": {
    "type": "higlass-bed",
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
...
```
### BED
### Vector (HiGlass)
### CSV

## Data Transform

# Mark
[source code](https://github.com/sehilyi/geminid/tree/master/src/core/mark)

Marks (e.g., points, lines) are the basic graphical elements of a visualization (we call one visualization a `track` in Geminid).
The core of constructing a visualization is to bind selected **data fields** to the **visual channels** (e.g., size, color, position) of a chosen **mark type**.

## Types of Mark
The `mark` property of a track is defined by a string that describe the mark type.
```javascript
// an example

{
    "tracks":[{
        "mark":"rect",
        ... // other track properties
    }],
    ... // other visualization properties
}
```
Geminid supports the following primitive `mark` types: `point`, `line`, `area`, `bar`, `rect`, `text`, `link`, `rule`, `triangle`. Composite mark (i.e., glyph) is also supported through the `"superpose"` property.


### Point
[source code](https://github.com/sehilyi/geminid/blob/master/src/core/mark/point.ts)

<img src="https://github.com/sehilyi/geminid/wiki/images/point_example.png" width="800" alt="point_example">  

[open the example in online editor](??)

```javascript
// an example of point marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "point",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```
### Line

<img src="https://github.com/sehilyi/geminid/wiki/images/line_example.png" width="800" alt="line_example">  

[open the example in online editor](??)

```javascript
// an example of line marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "line",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```
### Area


<img src="https://github.com/sehilyi/geminid/wiki/images/area_example.png" width="800" alt="area_example">  

[open the example in online editor](??)

```javascript
// an example of area marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "area",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```

### Bar

In Geminid, the `bar` mark is designed to draw bar charts.
Each bar mark show the value of one data point through the height of the bar.

<img src="https://github.com/sehilyi/geminid/wiki/images/bar_example.png" width="800" alt="bar_example">  

[open the example in online editor](??)

```javascript
// an example of area marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "bar",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```

### Rect
In Geminid, the `rect` mark is designed for representing genomic intervals.

<img src="https://github.com/sehilyi/geminid/wiki/images/rect_example.png" width="800" alt="rect_example">  

[open the example in online editor](??)

```javascript
// an example of react marks
{
    "traks":[
    {
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "chromosomeField": "Chromosome",
            "genomicFields": ["chromStart", "chromEnd"]
        },
        "mark": "rect", // specify the type of mark
        "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
        "color": { // bind the color of each rect mark to the data field: Stain
            "field": "Stain",
            "type": "nominal",,
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["white", "#D9D9D9", "#979797", "#636363", "black", "#A0A0F2"]
          },
        "x": { // bind the start position of each rect mark to the data field: chromStart 
            "field": "chromStart",
            "type": "genomic",
            "axis": "top"
        },
        "xe": { // bind the end position of each rect mark to the data field: chromEnd 
            "field": "chromEnd", "type": "genomic"
        },
        "size": {
            "value": 30 // specify the constant height of each rect mark
        }
    }, 
    ... // other encodings and styles of the rect mark
    ],
}

```

### Text
<img src="https://github.com/sehilyi/geminid/wiki/images/text_example.png" width="800" alt="text_example">  

[open the example in online editor](??)

```javascript
{
    "tracks":[{
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "tileset"
      },
      "metadata": {
        "type": "higlass-multivec",
        "row": "base",
        "column": "position",
        "value": "count",
        "categories": ["A", "T", "G", "C"],
        "start": "start",
        "end": "end",
        "bin": 16
      },
      "mark": "text", // specify the type of mark

      // specify styles of the mark
      "style": {"textStrokeWidth": 0},
      "stretch": true,

      // bind visual channels to corresponding data fields
      "x": {"field": "start", "type": "genomic", "axis": "top"},
      "xe": {"field": "end", "type": "genomic"},
      "y": {"field": "count", "type": "quantitative"},
      "color": {
        "field": "base",
        "type": "nominal",
        "domain": ["A", "T", "G", "C"]
      },
      "text": {"field": "base", "type": "nominal"} 
    }]
}
```

### Link

The link mark is designed to show the connections between genomes.  
<img src="https://github.com/sehilyi/geminid/wiki/images/link_example.png" width="800" alt="link_example">  

[open the example in online editor](??)


```javascript
{
"tracks": [
    {
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/circos-segdup-edited.txt",
        "type": "csv",
        "chromosomeField": "c2",
        "genomicFields": ["s1", "e1", "s2", "e2"]
      },

      "mark": "link", // specify the mark type

      // bind visual channels to corresponding data fields
      "x": {
        "field": "s1",
        "type": "genomic",
        "domain": {"chromosome": "1"},
        "axis": "top"
      },
      "xe": {"field": "e1", "type": "genomic"},
      "x1": {
        "field": "s2",
        "type": "genomic",
        "domain": {"chromosome": "1"},
        "axis": "top"
      },
      "x1e": {"field": "e2", "type": "genomic"},

      // specify styles of the mark
      "stroke": {"value": "steelblue"},
      "style": {"circularLink": true}
    }
  ]
}
```
### Rule

### Triangle
[source code](https://github.com/sehilyi/geminid/blob/master/src/core/mark/triangle.ts)  
Support three types of triangle marks: `triangle-l`, `triangle-r`, `triangle-d`

<!-- ### Brush -->
### Glyph
<!-- This will cover the `superpose`, mostly in the perspective of making a glyph (e.g., gene annotation) -->

## Visual Channels of Mark  
The visual appearance of a mark is controlled by a set of visual channels (e.g., size, position, color hue).
One visual channel can be either binded with a data field or assigned a constant value.



```javascript
// an example configuration for a line chart (x and y are encoded)

{
    "tracks":[{
      "data": {
        "url": ...,
        "type": ...
      },
      // specify the mark type
      "mark": "line",
      // visual channel x is bound with the data field genomic
      "x": {
        "field": "position",
        "type": "genomic",
        "axis": "top"
      },
      // visual channel y is bound with the data field peak
      "y": {
          "field": "peak", 
          "type": "quantitative"
          },
      // visual channel color is assigned a constant value
      "color": {"value": "steelblue"}
    }]
}

```


Overall, different marks have different visual channels and different visual channels have different properties.

<!-- 
| mark type | [`x`](#x)|[`xe`](#xe)| [`y`](#y)|[`ye`](#ye)|  [`size`](#size)| [`row`](#row)| 
|----| ----|---|---|---|--|--|---|
| [`point`](#point) | | | radius of the point |
| [`line`](#line) | | | |
| [`rect`](#rect)| position of the left edge | - |
| [`bar`](#bar)| | height of the bar | |
| [`area`](#area)| | |  | 
-->


| mark type |supported visual channels| 
|----| ----|
| [`point`](#point) | [`x`](#x), [`y`](#y), `size`, `color`, `strokeWidth`, `opacity` |
| [`line`](#line) |  [`x`](#x), [`y`](#y), `color`, `strokeWidth`, `opacity`|
| [`rect`](#rect)| [`x`](#x), `xe`, `color`, `strokeWidth`, `opacity` |
| [`bar`](#bar)| [`x`](#x), [`y`](#y) |
| [`area`](#area)| [`x`](#x), [`y`](#y) |


### x
### xe
### y
### ye
### row

<img src="https://github.com/sehilyi/geminid/wiki/images/without_row.png" width="500" alt="with row example">  
<img src="https://github.com/sehilyi/geminid/wiki/images/with_row.png" width="500" alt="without row example">  

**Left**: without specifying rows; **Right**: rows are bound with the sample field

```javascript
{
  "tracks":[
    {
      // specify data source
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "tileset"
      },
      "metadata": {
        "type": "higlass-multivec",
        "row": "sample",
        "column": "position",
        "value": "peak",
        "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
      },
      // specify the mark type
      "mark": "line",
      // specify visual channels
      "x": {
        "field": "position",
        "type": "genomic",
        "domain": {"chromosome": "1", "interval": [1, 3000500]},
        "axis": "top"
      },
      "y": {"field": "peak", "type": "quantitative"},
      "color": {"field": "sample", "type": "nominal", "legend": true},
      // visual channel row is bound with the data field: sample
      "row": {"field": "sample", "type": "nominal"}
    }
  ]
      
}
```




### size
### text


### color
<!-- I didn't see the legend (when set legend: true) of color when {"type": "quantitative"} -->
### stroke
### strokeWidth
### opacity
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->
### style

properties shared by all visual channels 
| visual channel properties | type    | description |
| --------------------- | ------- | ---------- |
| field                 | string  | the data field name |
| type                  | string  | specify type of the data field. support `"genomic"`, `"nominal"`, `"quantitative"`|
| aggregate             | string  | support `"max"`, `"min"`, `"mean"`, `"bin"`, `"count"` |
| domain                | |  |
| range                 |         |        |

properties that are only used by certain visual channels 
| visual channel properties | type    | description |
| --------------------- | ------- | ---------- |
| axis                  | string  | This property is only used for visual channels `x` and `y`. It specifies the position of the axis. Support `"none"`, `"top"`, `"bottom"`, `"left"`, `"right"` |
| baseline              |         |         |

<!-- ### superpose
overlay another track on the original track. 
Superpose share the same options as the original track unless it is specified.

---

only useful when `{"type": "circular"}`

### innerRadius
### outerRadius -->


# Tracks
In Geminid, we call one visualization a track.
A Geminid configuration specifies an array of `tracks`.

```javascript
{
  "tracks":[
    {...}, // each object specifies a track 
    {...},
    ...
  ]
}
```


## Layout
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L22)  
In geminid, each track is in either `circular` or `linear` layout.


<img src="https://github.com/sehilyi/geminid/wiki/images/linear_circular.png" alt="linear vs circular" width="600">    

**Top:** a `linear` layout; **Bottom:** a `circular` layout.

Users can either specify the layout of all tracks using 
```javascript
{
    "layout":{
        "type": "linear", //specify the layout of all tracks
    },
    "tracks":[...]
}
```
or overwrite the layout of one track using
```javascript
{
    "tracks"[
      {
        "circularLayout": false, // specify the layout of this track
        ...
      },
      {
        "circularLayout": true,
        ...
      },
      ...
    ],
    ...//
}
```

## Arrangement
How to arrange multiple tracks?

### Grid-based arrangement
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L20)  
specify the grid arrangement of multiple tracks

| property                | type                        | description                                                                                                                                    |
| ----------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| arrangement.direction   | `string`                    | **Required**, the layout direction of all tracks (either `vertical`   or `horizontal`)                                                         |
| arrangement.wrap        | `number`                    | specify the number of tracks at each row (when `direction:horizontal`) or at each column (when `direction:vertical`). default value = infinite |
| arrangement.rowSizes    | `number` \| `Array<number>` | specify the height of each row in pixels                                                                                                       |
| arrangement.rowGaps     | `number` \| `Array<number>` | specify the gap between two rows in pixels                                                                                                     |
| arrangement.columnSizes | `number` \| `Array<number>` | specify the width of each column in pixels                                                                                                     |
| arrangement.columnGaps  | `number` \| `Array<number>` | specify the gap between columns in pixels                                                                                                      |

<img src="https://github.com/sehilyi/geminid/wiki/images/layout_demo.png" alt="layout demo" width="400">

<!-- is it possible that several tracks under one layout have different type (linear and circular) -->

### Superposition
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L213)

## Style

`style` specifies the visual appearances of a track that are not bound with data fields.

style properties | type | description
-- | -- | --
background | string | color of the background
dashed | [number, number] |
linePatterns| { "type": "triangle-l" \| "triangle-r"; size: number } | 
curve| string | support "top", "bottom", "left", "right" 
align| string | support "left", "right"
dy | number | 
outline | string |
outlineWidth | number |
circularLink | boolean |
textFontSize | number |
textStroke | string |
textStrokeWidth | number |
textFontWeight| string | support "bold", "normal"



# Interactions



## Linking Views
[source code](ttps://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L328)


## Zooming and Panning
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L7)

## Semantic Zoom
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L203)

## Tooltip
[source code](https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L168)
