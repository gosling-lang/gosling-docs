# Overview
Gosling is a declarative visualization grammar tailored for interative genomic visualizations. In Gosling, users can create interactive visualizations through a JSON syntax. This documentation describes how to write the JSON specification language to create interactive visualizations.   You are welcome to try the [Gosling online edtior](https://gosling-lang.github.io/gosling.js/).

  <!-- "title": "title of the visualizations",
  "subtitile": "subtitile of the visualizations",
  "description": "a detailed description of the visualizations",
  "width": 800,
  "height": 200,
  "static":  false -->

```javascript
// Gosling generates visualizations through a JSON specification language

{
  // each track represent a single visualization
  "tracks":[
    {
      // specify the data source and data format of this track
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
  // specify the arrangement of multiple tracks
  "arrangement":{
    ...
  }
}
```

# List of Contents


- [Overview](#overview)
- [List of Contents](#list-of-contents)
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
    - [Triangle](#triangle)
  - [Visual Channels of Mark](#visual-channels-of-mark)
    - [x](#x)
    - [xe](#xe)
    - [y](#y)
    - [ye](#ye)
    - [x1 x1e y1 y1e](#x1-x1e-y1-y1e)
    - [row](#row)
    - [size](#size)
    - [text](#text-1)
    - [color](#color)
    - [stroke](#stroke)
    - [strokeWidth](#strokewidth)
    - [opacity](#opacity)
- [Tracks](#tracks)
  - [Layout](#layout)
  - [Arrangement](#arrangement)
    - [Grid-based arrangement](#grid-based-arrangement)
    - [Superposition](#superposition)
  - [Style](#style)
- [Interactions](#interactions)
  - [Zooming and Panning](#zooming-and-panning)
  - [Linking Views](#linking-views)
  - [Brushing and Linking](#brushing-and-linking)
  - [Semantic Zoom](#semantic-zoom)

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
[source code](https://github.com/gosling-lang/gosling.jstree/master/src/core/mark)

Marks (e.g., points, lines, and bars) are the basic graphical elements of a visualization (we call one visualization a `track` in Gosling).
The core of constructing a visualization is to bind selected **data fields** to the **visual channels** (e.g., size, color, and position) of a chosen **mark type**.

## Types of Mark
The `mark` property of a track is defined by a string that describes the mark type.
```javascript
{
    "tracks":[
      {
        "mark": "rect",
        ... // other track properties
      },
      {
        "mark": "line",
        ... // other track properties
      }
    ],
    ... // other visualization properties
}
```
Gosling supports the following primitive `mark` types: `point`, `line`, `area`, `bar`, `rect`, `text`, `link`, `rule`, `triangle`. Composite mark (i.e., glyph) is also supported through the [`superpose`](#superposition) property.


### Point
[source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/point.ts)

The mark `point` represents one data point using a circular shape. Visual channels of the circle, such as radius, color, and vertical/horizontal position, are used to represent values of the data point. Popular charts such as scatter plots and bubble charts use `point` mark.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/point_example.png" width="800" alt="point_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(6'ZtleJBasic%20Marks%3A%20Point'NsubZtleJTutorial%20ExOs'NlayoutJlinear'Narrangement4('direcZonJverZcal'G'rowSizes4180G'columnSizes4800)Ntracks4%5B6*(K'~'urlJhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FZleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQXIZleset'Kjmeta~Ihiglass-mulZvecX'rowJsOX'columnJposiZonX'valueJpeakX'categories4%5B'sO%201'%5DKjmarkJpoint'2'x4(K*WposiZonXIgenomicX'domain4('chromosomeJ1'G'interval4%5B1G3000500%5D)2*'axisJtop'Kjy4Csize4Ccolor4(WsO'GInominal'G'legend4truejopacity4('value40.9)6*)6%5D%0A)*%20%202%2CK4!%206%0A*C(Wpeak'GIquanZtaZve'jG%2C%20I'typeJJ4'K6**N%2C6'OampleW'fieldJX'2*Ztij)2'~data4(K*%01~jZXWONKJIGC642*_>)

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

The mark `line` represents a set of data points using a line that connects these points.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/line_example.png" width="800" alt="line_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9'NtleJBasic%20Marks%3A%20Line'4'subNtleJTutorial%20ExWs'4'layoutJlinear'4'arrangement~direcNonJverNcal'G'rowSizes6180G'columnSizes6800)4'tracksj9*(9CdataXurlJhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FNleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQIKNleset'OmetadataXKhiglass-mulNvecIrowJsWIcolumnZvalueJpeakIcategoriesj'sW%201'%5DOmarkJline'4CxXfieldZKgenomicIdomain~chromosomeJ1'G'intervalj1G3000500%5D)4*CaxisJbottom'Oy~fieldJpeak'G'KquanNtaNve')4Csize~value62)9*)9%5D%0A)*%20%204%2C96!%209%0A*C**'G%2C%20I'4*CJ6'KtypeJNtiO9**)4CWampleX6(9*CZJposiNonIj6%5B~6('%01~jZXWONKJIGC964*_>)

```javascript
// an example of using line marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // specify mark type
        "mark": "line",
        // specify mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top" // position of the x axis 
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
The mark `area` represents a set of data points as an area shape. The upper edge of the area shape is a line that connects all the points and the bottom edge is the x axis.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/area_example.png" width="800" alt="area_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9'NtleJBasic%20Marks%3A%20Area'4'subNtleJTutorial%20ExWs'4'layoutJlinear'4'arrangement6('direcNonJverNcal'G'rowSiz~6180G'columnSiz~6800)4'tracksj9*(9CdataXurlJhttps%3A%2F%2Fr~gen.io%2Fapi%2Fv1%2FNl~et_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQIKNl~et'OmetadataXKhiglass-mulNvecIrowJsWIcolumnZvalueJpeakIcategori~j'sW%201'%5DOmarkJarea'4CxXfieldZKgenomicIdomain6('chromosomeJ1'G'intervalj2000500G3000500%5D)4*CaxisJbottom'Oy6('fieldJpeak'G'KquanNtaNve')9*)9%5D%0A)*%20%204%2C96!%209%0A*C**'G%2C%20I'4*CJ6'KtypeJNtiO9**)4CWampleX6(9*CZJposiNonIj6%5B~es%01~jZXWONKJIGC964*_>)

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
        "color": ...,
        ... // other encodings and styles
    }]
}
```

### Bar

The `bar` mark is designed for drawing bar charts. Each bar shows the value of one data point through its height.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/bar_example.png" width="800" alt="bar_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(C'OtleKBasic%20Marks%3A%20Bar'4'subOtleKTutorial%20ExXs'4'layoutKlinear'4'arrangement6('direcOonKverOcal'I'rowSizes6180I'columnSizes6800)4'tracks~C*(CGdataZurlKhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FOleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQJNOleset'WmetadataZNhiglass-mulOvecJrowKsXJcolumnjvalueKpeakJcategories~'sX%201'%5DWmarkKbar'4GxZfieldjNgenomicJdomain6('chromosomeK1'I'interval~2900500I3000500%5D)4*GaxisKbottom'Wy6('fieldKpeak'I'NquanOtaOve')C*)C%5D%0A)*%20%204%2CC6!%20C%0A*G**'I%2C%20J'4*GK6'NtypeKOtiWC**)4GXampleZ6(C*GjKposiOonJ~6%5B%01~jZXWONKJIGC64*_>)

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
        // y indicates the visual encoding of the bar height
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```

### Rect
The `rect` mark is designed for representing genomic intervals using reactangular shapes. Left and right edge of the rectangle indicate the start and end genomic positions, respectively.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/rect_example.png" width="800" alt="rect_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(K%20'titleZBasic%20Marks%3A%20Rect'_'subtitleZTutorial%20Examples'_'layoutZlinear'_'arrangementJ(K*'directionZvertical'_*'columnSizesJ800_*'rowSizesX60L180L180L180%5DK)_'tracksXK*(Q'dataJ(KNurlZhttps%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvV'~csvVPosomeFjZChromosomeV'%22FjsXPStart'LPEnd'%5DQ)4K*NmarkZrectV*'dataTransformJ(QNfilterX('fjZStain'L'oneOfX'acen'%5DL'notJtrue)%5DQ**)4**'colorJ(QNfjZStain'4N~nominal'4NdomainX'gnegY25Y50Y75Y100'L'gvar'%5D4NrangeXQ*NwhiteVN%23D9D9D9VN%23979797VN%23636363VNblackVN%23A0A0F2'Q***%5DQ**)Q*4'xJ(KNfjJPStartV'~%22V'domainJ(PosomeZ1')4*'axisZtop'Q)4'xeJ('fjJPEnd'L'~%22')4'sizeqJ20)4'strokeqZgray')4'strokeWidthqJ0.5)4'styleJ('outlineZwhite')K*)K%5D%0A)*%20%204%2CQJ!%20K%0A*L%2C%20N***'P'chromQK**V'4*XJ%5BY'L'gposZJ'_%2CKjieldqJ('value~typeZ%22genomic%01%22~qj_ZYXVQPNLKJ4*_>)

```javascript
// an example of rect marks
{
    "traks":[
    {
        "data": ...,
        // specify the type of mark
        "mark": "rect", 
        // bind the color of each rect mark to the data field: Stain
        "color": { 
            "field": "Stain",
            "type": "nominal",,
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["white", "#D9D9D9", "#979797", "#636363", "black", "#A0A0F2"]
          },
        // bind the start position of each rect mark to the data field: chromStart 
        "x": { 
            "field": "chromStart",
            "type": "genomic",
            "axis": "top"
        },
        // bind the end position of each rect mark to the data field: chromEnd 
        "xe": { 
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

The `text` mark is designed to display textual labels. For example, gene names and nucleobases can be displayed with a `text` mark.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/text_example.png" width="800" alt="text_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0A%205~tleZBasic%20Marks%3A%20Text4%0A5sub~tleZTutorial%20Examples4%0A5layoutZlinear4%0A5arrangement9('direc~onZver~cal42columnSizes9800)%2C%0A5tracks9%5Bj%20jI(**'data9(*5urlZhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2F~leset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQXJ~leset'*Nmetadata9(*5Jhiglass-mul~vecXrowZbaseXcolumnZposi~onXvalueZcountXcategoriesO%2C*5startZstartXendZendXbin916*)%2C**'markZtext4*'yKcount42Jquan~ta~ve'Nstyle9('textStrokeWidth90Nstretch9true%2C*'xKstart%2242axisZtop'NxeKend%22'Ncolor9(*5fieldZbaseXJnominalXdomainO*NtextKbase42Jnominal')jI)j%5D%0A)*jI%205%20'4'%2C5%2029!%20I%20%20JtypeZK9('fieldZN)%2C*'O9%5B'A42T42G42C'%5DX4*5Z!2j%0AI~ti%2242Jgenomic%01%22~jZXONKJI9542*_>)

```javascript
{
    "tracks":[{
      "data": ...,
      
      // specify the type of mark
      "mark": "text", 
      
      // specify styles of the mark
      "style": {"textStrokeWidth": 0},

      // bind visual channels to corresponding data fields
      "x": {"field": "start", "type": "genomic", "axis": "top"},
      "xe": {"field": "end", "type": "genomic"},
      "y": {"field": "count", "type": "quantitative"},
      "color": {
        "field": "base",
        "type": "nominal",
        "domain": ["A", "T", "G", "C"]
      },

      // specify the text content
      "text": {"field": "base", "type": "nominal"} 
    }]
}
```

### Link

The `link` mark is designed to show connections between chromosomes using an arc that connects two genomic intervals.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/link_example.png" width="800" alt="link_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9%20'YBasic%20MXks%3A%20LRkjsubYTutorial%20ExamplesjlayoutHlReXjXrangementQ'directionHverticalD'columnSizes4800A9'track_9*(UNQq'urlHhttps%3AJraw.githubusercontent.cZ%2Fsehilyi%2FgemRi-Nsets%2Fmaster%2FN%2Fcircos-segdup-edited.txtI'VHcsvIKFOHc2I'WFO_'s1D'e1D's2D'e2'%5D3A%0AUmXkHlRkDGP%20V%0A3J%20bRd%20visual%20channels%20to%20correspondRg%20N%20fOsUxQqCs1I7I63~eQCe1D7'~1QqCs2I7I63~1eQCe2D7'A%0A3Gstyles%20of%20PUstrokeQ'valueHsteelblue'AUstyleQ'circulXLRk4true)9*)9%5D%0A)*%20%2039**4!%205'%2C6'dZaRQKH1'Aq'axisHtop'7'VHW9%0A*A)%2CC'fOHD5%20GJ%20specify%20H4'I5qJ%2F%2FK'chrZosZeNdataOieldPthe%20mXkQ4(RinU3'VtypeWgenZicXarYtitleHZom_s4%5Bj59'q3*~AUx%01~qj_ZYXWVURQPONKJIHGDCA976543*_>)


```javascript
{
  "tracks": [
      {
        "data": ...,

        "mark": "link", // specify the mark type

        // bind visual channels to corresponding data fields

        // x and xe indiates the start point of the arc  
        "x": {
          "field": "s1",
          "type": "genomic",
          "domain": {"chromosome": "1"},
          "axis": "top"
        },
        "xe": {"field": "e1", "type": "genomic"},

        // x and xe indiates the end point of the arc  
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

### Triangle
[source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/triangle.ts)  
Support three types of triangle marks: `triangle-l`, `triangle-r`, `triangle-d`

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=>)

<!-- ### Brush
### Glyph -->


## Visual Channels of Mark  
The visual appearance of a mark is controlled by a set of visual channels (e.g., size, position, and color). One visual channel can be bound with either a data field or just a constant value.

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


Overall, different marks have different visual channels, and different visual channels have different properties.

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
| [`point`](#point) | [`x`](#x), [`y`](#y), [`row`](#row), [`size`](#size), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity) |
| [`line`](#line) |  [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth)|
| [`rect`](#rect)| [`x`](#x), [`xe`](#xe), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity) |
| [`bar`](#bar)| [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity)|
| [`area`](#area)| [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth) |
| [`link`](#link)| [`x`](#x), [`xe`](#xe), [`x1`](#x1-y1-x1e-y1e), [`x1e`](#x1-y1-x1e-y1e), [`color`](#color), [`opacity`](#opacity) |
| [`triangle`](#triangle)| [`x`](#x), [`xe`](#xe), [`row`](#row), [`size`](#size), [`color`](#color), [`opacity`](#opacity) |
| [`text`](#text)| [`x`](#x), [`xe`](#xe), [`row`](#row), [`color`](#color), [`opacity`](#opacity) |

A visual channel can be either assigned a constant value or bound with a data field. When a visual channel is bound with a data field, Gosling creates a mapping from the values of the data field (**domain**, e.g., [12, 0, ..., 9]) to the values of the visual channel (**range**, e.g., height of a bar)

Table: Properties shared by all visual channels 
| visual channel properties | type    | description |
| --------------------- | ------- | ---------- |
| field                 | string  | specify name of the data field |
| type                  | string  | specify type of the data field. support `"genomic"`, `"nominal"`, `"quantitative"`|
| aggregate             | string  | support `"max"`, `"min"`, `"mean"`, `"bin"`, `"count"` |
| domain                | [number, number]\| string[]  | specify values of the data field |
| range                 |   [number, number]\| string[]      |   specify values of the visual channel     |
| value | string \| number| assign a constant value to the visual channel |


### x
`x` specify a mark's position in the horizontal direction.


### xe
`xe` stands for the end of x axis. `xe` is usually used with `x` to specify the start position and the end position of a visual mark in the horizontal direction, respectively.

### y
`y` specify a mark's position in the vertical direction.

### ye
`ye` stands for the end of y axis. `ye` is usually used with `x` to specify the sstart position and the end position of a visual mark in the vertical direction, respectively.

### x1 x1e y1 y1e
The four channels are used together only in `link` mark. In this case, `x` and `xe` are used with `x1` and `x1e` to specify a pair of genomic intervals that needs to be connected using band representations. Similarly, `y` and `ye` can be used with `y1` and `y1e` to show band connection along vertical axis.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/x_x1_example.png" width="400" alt="x x1 example">  

### row

Channel `row` is used with channel `y` to stratify a visualization with categorical values.

Without specifying `row`:

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/without_row.png" width="500" alt="with row example">  

Line charts are stratified with sample names.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/with_row.png" width="500" alt="without row example">  

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
Channel `size` indicates the size of the visual mark. It determines either the radius of a circle (`mark: point`), the vertical length of a triangle (`mark: triangle-r`, `mark: triangle-l`, `mark: triangle-d`), the vertical length of a rectangle (`mark: rect`), the thickness of a line (`mark: line`).

### text

`text` channel is used only in `text` mark to specify what textual information to display.

### color
Channel `color` specifies the filling color of the mark. Binding `color` with categorical values in `bar` and `area` marks stack marks that are positioned in the same genomic intervals to better show their cumulative values.
<!-- I didn't see the legend (when set legend: true) of color when {"type": "quantitative"} -->

### stroke
Channel `stroke` defines the outline color of the mark. Gosling supports `stroke` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

### strokeWidth
Channel `strokeWidth` defines the outline thickness of the mark shape. Gosling supports `strokeWidth` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

### opacity
Channel `opacity` specifies the opacity of the mark shape.
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->




properties that are only used by certain visual channels 
| visual channel properties | type    | supported in channels | description |
| --------------------- | ------- | ---------- | ---|
| axis                  | string  |`x`, `y` | specify the position of the axis. Support `"none"`, `"top"`, `"bottom"`, `"left"`, `"right"` |
| baseline              |         |         |
| legend | | |

<!-- ### superpose
overlay another track on the original track. 
Superpose share the same options as the original track unless it is specified.

---

only useful when `{"type": "circular"}`

### innerRadius
### outerRadius -->


# Tracks
In Gosling, we call one visualization a track. A Gosling configuration specifies an array of `tracks`.

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
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L22)
In each track, genomic coordinate can be represented in either a `circular` or `linear` layout.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/linear_circular.png" alt="linear vs circular" width="600">    

Figure: **Top:** a `linear` layout; **Bottom:** a `circular` layout.

Users can either specify the layout of all tracks on the root level

```javascript
{
    "layout": "linear", //specify the layout of all tracks
    "tracks":[...]
}
```

or specify the layout of a certain track in each track definition.

```javascript
{
    "tracks"[
      {
        "layout": "linear", // specify the layout of this track
        ...
      },
      {
        "layout": "circular",
        ...
      },
      ...
    ],
    ...//
}
```

## Arrangement

### Grid-based arrangement
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L20)  
specify the grid arrangement of multiple tracks

| property                | type                        | description                                                                                                                                    |
| ----------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| arrangement.direction   | `string`                    | **Required**, the layout direction of all tracks (either `vertical`   or `horizontal`)                                                         |
| arrangement.wrap        | `number`                    | specify the number of tracks at each row (when `direction:horizontal`) or at each column (when `direction:vertical`). default value = infinite |
| arrangement.rowSizes    | `number` \| `Array<number>` | specify the height of each row in pixels                                                                                                       |
| arrangement.rowGaps     | `number` \| `Array<number>` | specify the gap between two rows in pixels                                                                                                     |
| arrangement.columnSizes | `number` \| `Array<number>` | specify the width of each column in pixels                                                                                                     |
| arrangement.columnGaps  | `number` \| `Array<number>` | specify the gap between columns in pixels                                                                                                      |

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/layout_demo.png" alt="layout demo" width="400">

<!-- is it possible that several tracks under one layout have different type (linear and circular) -->

### Superposition
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)


`superposition` enables users to superpose multiple marks on top of each other.  
`superpostion` is an array of objects, each object specifies one visual mark. This visual mark inherit the properties (e.g., `data`, `x`, `y`) defined in this track, unless these properies are redefined in the object.  

```javascript
{
  "tracks": [
    {
      "data": ... , // specify data
      "x": ...,
      "y": ...,
      "color":...,
      "superpose": [
        // point mark and line mark have the same data, x, y, color encoding
        {
          "mark": "line", 
        },
        {
          "mark": "point", 
          // specify the size of point mark
          "size": {"field": "peak", "type": "quantitative", "range": [0, 6]} 
        }
      ]
    }
  ]
}
```

Try it in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'jtleXExample%3A%20Superposed%20TracksCJ'layoutXlinearCJ'arrangementB(J*'direcjonXverjcalCJ*'columnSizesB800%2CJ*'rowSizesB450J)%2CJ'tracksZJ*(9'dataB(9*'urlXhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Fjleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQWIjleset'9M'metadataB(9*Ihiglass-muljvecW'rowBGW'columnXposijonW'valueXpeakW'categoriesZ~1O~2O~3O~4'%5D9M'superposeZ9*('markXline'M*(9**'markXpointW*'sizeKO'rangeZ0%2C%206%5D)9*)9%5D%2C9'xB(9*bXposijonWIgenomicW'domainB('chromosomeX1O'intervalZ1%2C%203000500%5DM*'axisXtop'9M'yK'M'rowNM'colorN)J*)J%5D%0A)*%20%209J**B!%20C'%2CG'sampleI'typeXJ%0A*KB(bXpeakOIquanjtajveM)%2C9NB(bBGOInominal'OC%20WC9*XB'ZB%5Bb'fieldjti~G%20%01~jbZXWONMKJIGCB9*_>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0A*'titleG'Example%3A%20Superposed%20Tracks'%25*'layoutG'linear'%25*'arrangementG(%0AQ'directionG'vertical'%25Q'columnSizesG800%25Q'rowSizesG200%0A*)%25*'tracksY%0A*%20%0AQ(C'dataG(C*'urlG'https%3A%2F%2Fcgap-higlass.com%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3Dclinvar_20200824_hg38'A%24tileset'CjmetadataG(C*%24higlass-bed'A'%3EFieldsYCQ%3B1%3Cstart')A*%3B2%3Cend')CqA'valueFieldsY%3B7%3CIZO)%5DCjsuperposeYC*%5Ebar'A*'strokeG(CQ*XIAQOAQ~YC%7BHQ'HQRQ*'JQV%2FJ%40CQ*KQKQKQ%2BQMAQMAQMCQqCQ)A*'strokeWidth%220.5)%601)C*)A%5Epoint'%605)A*'colorG(CQ*XIAQOAQ~YC%7BHQ'HQRQ*'JQV%2FJ%40CQ*KQKQKQ%2BQMAQMAQMCQqAQ'legendGtrueCQ)C*)C%5D%2CC'xG(C*Xstart'A%24%3E'A~G('chromosomeG'3')A'axisG'top'CjxeG(Xend'Z%24%3E'jyG(C*XIAOA~YC*N'AN%2FH'HR*'JV%2FJV'CqA'baselineGR%26150Z20%5DA'gridGtrueCjcolorG(C*XIAOA~YC*N'AN%2FH'HR*'JV%2FJV'CqA%26C*KKK%2BMAMAMCqCjopacity%220.6)%0AQ)%0Aq%0A)*%20%20A%2CC*C%0AQ*G!%20HLikely_pathogenic'A*Isignificance'JLikely_benign'A*K*'%23D45E00'AM*'%23029F73'N*'PathogenicO%24nominal'Q**R'Uncertain_IAV'BenignX'fieldG'YG%5BZ%2C%20j)%2CC'q*%5D~'domain%22G('valueG%24'typeG'%25%2C%0A%26'rangeY%2B*'black'A%3B('indexG%3CZ'nameG'%3Egenomic%40QV'CQqAQ%26%5E(CQ'markG'%60A*'size%22%7BQ*N'AQN%2F%01%7B%60%5E%40%3E%3C%3B%2B%26%25%24%22~qjZYXVRQONMKJIHGCA*_>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(V'titleK'Example%3A%20Superposed%20Tracks'_'layoutK'linear'_'arrangementK(V*'directionK'vertical'_*'columnSizesK800_*'rowSizesK80V)_'tracksK%5BV*(VXdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csv'Q'typeK'csv'Q'c%3CFieldK'C%3C'Q'genomicFieldsK%5B'%60LchromEnd'%5DV**)_XsuperposeK%5BJ%7Dtext'QRMtrue)~textK('YNameL%25)Q*'%3BX%25QXZ%22'%40L%40L%40L%40LwhiteL%40'~visibilityK(JXoperationK'less-than'QXconditionK('widthK'%7Cxe-x%7CLtransitionPaddingK10)QXtargetK'mark'J*)Q*'styleK('textS%7BK0%26rect'QRMtrue)~%3BX%25QXZ%22J*Xwhite%3DD9D9D9%3D979797%3D636363'Q*X%40%3DA0A0F2'J**%5DJ*%5E-r'QRJ***M%24'q%3F~%2B%5E-l'QRJ***M%24'p%3F~%2B)J)V**%5D_XxK(J'Y%60'Q'%3EQ'domainK('c%3CK'1')Q'axisK'top'V**)_XxeK('YchromEndL%3E)_Xsizej20)_Xstrokej'gray')_Xs%7Bj0.5)_XstyleK('outlineK'white')V*)V%5D%0A)*%20%20JV***K!%20L'%2C%20'M('YStainLoneOfK%5B'acen'%5D%2C%20'notKQ%2CJR*'dataTransformK(JXfilterK%5BV%0A*X**'YfieldK'ZdomainK%5B'gnegLgpos25Lgpos50Lgpos75Lg_%2CVjK('valueK~%5DJ*)Q*'%22pos100Lgvar'%5DQXrangeK%5B%24false)Q***('YNameLincludeK%25typeK'nominal'%26)J)Q%7D%2Bcolorj'%23B40101'%3BcolorK(JXYStain'Q%3Chromosome%3D'Q*X%23%3EtypeK'genomic'%3FLnotKfalse)J**%40black%5E%26triangle%60chromStart%7BtrokeWidth%7D(J*'markK'%01%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_ZYXVRQMLKJ*_>)




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

## Zooming and Panning
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L7)

Each visualization in Gosling, by default, supports the Zooming and Panning interaction.
Users can zoom in/out a visualization using the scrolling up/down actions.
Users can pan by clicking on the visualization and then drag it in the desired direction.



## Linking Views
[source code](ttps://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L328)

When two tracks are linked, the zooming and panning performed in one track will be automatically applied to the linked track. 

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0AOlayout!6linear%5E%0AOarrangementC('direction!6vertical%5E6columnSizesC800%2C6rowSizesC200)%2C%0AOtracksC%5B%24E%22Gj%2Bb%40M3%5E%23%204%3Eline%25bNX*OaxKa%26*GZGrowBGcolorB%2C6%3CT%3B%2C%24E%22Gj%2Bb%40M2%3Earea%25bNX*OaxKthe%20same%26%20as%20the%20first%20track*GZGrowBGcolorB~%3CT%3B%0A%20%20%5D%0A)*J%20O%20'9%5E*OBC('field!%23%5E6Nnominal'C!%20Ehttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHuG)%2C*'J%0A%20%20%20%20Kis!6top9linkingID!6link1'%20%2F%2F%20assign%20Mpeak9categoriesC%5B'sample%201%5E%23%20Ntype!6O%206TstrokeC('%40white'GstrokeWidthC('Xgenomic9domainC('chromosome!62')%2CZyC('field!6peak%5E6Nquantitative'b!6position9jmetadataC(*ONhiglass-multivec%22RDiYA3qwFlm7xQ9Ntileset'*%236sample%24J(*'dataC(*Ourl!6%25%5E*'xC(*Ofield%26%20linking%20id%2B9row!%239column%3BvalueC0.5)J)%3ClegendCtrueG%3E'%5D*Gmark!6%40value!6%5E'%2C%01%5E%40%3E%3C%3B%2B%26%25%24%23%22jbZXTONMKJGECB96*_>)

Users can link two tracks by assigning the same `linkingID` to the `x` channel of the two tracks.
```javascript
{
  "tracks":[
    // track A
    {
      "data": ...,
      "mark": "rect",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // assing a linking id for the track A
      }
    },
    // track B
    {
      "data": ...,
      "mark": "point",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // the same linking id links track A and track B
      }
    },
    ... // other tracks
  ]
}
```

## Brushing and Linking
Users can use **brushing** to select a subset of the data items using a recatangle. User can modify the left and right edge of the rectangle to modify the selection. The selected data items can be linked to data items in another track.

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(W'title~Example%3A%20Brushing%20and%20Linking'%2CW'layout~linear'%2CW'arrangement5('direction~vertical'O'columnSizes5800O'rowSizes5200ZW'tracks5%5B%229uRN*JXM%23G%24MK1'%25*Z*C**%2F%2F%20create%20a%20rectangle%20brush*'superpose5%5B*4()O%2F%2F%20this%20dummy%20object%20cannot%20be%20removed*4('mark~rect-brush'O*4'x5('T)6color5('value!'steelBlue')*4)*%5DW4Z%229uRN*JXM%23G%24MK1'O'interval5%5B200000000O220000000%5D%256T*Z*C*'opacity!('value51)W4)W%5D%0A)*W444%20%205!%206%2C*4'9'https%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHC'y5('field~peak'O'type~quantitative'ZGories5%5B'sample%201'%5D*Z*'mark~line'%2CJ'metadata5(*4'type~higlass-multivec'Ktype~genomic'6domain5('chromosome~M~position'6NDiYA3qwFlm7xQ'6type~tileset'*ZO%2C%20TlinkingID~linking-with-brush'W%0A4X6row~sample'6columnZ)%2C~5'%22W4(*'data5(*4'url5%23value~peak'6categ%24*'x5(*4'field%25)6axis~top'%01%25%24%23%22~ZXWTONMKJGC9654*_>)

```javascript
{
  "tracks":[
    // track A
    {
      "data": ...,
      "mark": "line",
      ..., 

      // create a rectangle brush
      "superpose": [
        {}, // this dummy object cannot be removed
        {
          "mark": "rect-brush", 
          "x": {"linkingID": "linking-with-brush"}, // assign a unique id to the brush
          "color": {"value":"steelBlue"}
        }
      ]
    },
    // track B
    {
      "data": ...,
      "mark": "point",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // the same linking id links track B and the brush in track A
      }
    },
    ... // other tracks
  ]
}
```


## Semantic Zoom
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L278)

Semantic zoom allows users to switch between different visualizations of the same data through zooming in/out. When zooming in, the same data will be represented in a different way in which more details are shown. 

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_0.png" alt="semantic_zoom_coarse" width="400">  

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_1.png" alt="semantic_zoom_fine" width="400">

**Top**: only `bar` marks are represented; **Bottom:** `text` marks are presented when zooming in.  

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'titleNExample%3A%20Semantic%20Zooming'V'subtitleNhide%25annotation%20and%20only%20show%20bar%20charts%20when%20zooming%20out'V'arrangement6(J*'directionNvertical'V*'columnSizes6800V*'rowSizes6180J)V'tracks6%5BJ*(JLdata6(5'urlNhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DWipsnEDMStahGPpRfH9adA'BQtileset'J**)VLmetadata6(5Qhiglass-multivec'B'rowNbase'B'columnN%3C'valueNcount'B'categoriesjstartNstart'B'endNend'J**)V**%20'x6(5'U%3CQ%24B'domain6KB'axisNtop'J**)VLcolor6(5'Ubase'BQnominal'B'domainjlegend6trueJ**)VLy6%3BQquantitative')VLsuperpose6%5B5(%2B)B(5*%2BB*'s%26~61)B*'stroke%3EXgtet'BY620I5L%221%235)B%2F%2F%25mark5(5*'dataTransform6(5Lfilter6%5B%3B'oneOf6%5B0%5DI'not6true)%5D5*)B*'markNtext'B*'x6(5LUstart'BLtypeN%24BLdomain6KBLaxisNtop'5*)B*'xe6('Uend'IQ%24)B*'color%3E*'y~670)BXless-than'BYN%7Cxe-x%7C'5**I'%223%23B*%20'text6('Ubase'IQnominal')B'style6(5LtextFontSize624BLtextS%2660BLtextFontWeightNbold'5)5)J**%5DJ*%20J*%20J*)J%5D%0A)*%20%205J***6!%20B%2C5I%2C%20J%0A*K('chromosomeN1'I'interval6%5B3000000I3000010%5D)L**'N6'Q'typeNUfieldNV%2CJX*'visibility6(5LoperationNYLmeasureNwidth'BLthresholdj6%5B'A'I'T'I'G'I'C'%5DB'~6('value%22transitionPadding6%230BLtargetNmark'5*)%24genomic'%25%20text%20%26trokeWidth%2B'markNbar'%3B('Ucount'I%3Cposition'B%3E~Nwhite')B%01%3E%3C%3B%2B%26%25%24%23%22~jYXVUQNLKJIB65*_>)

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_2.png" alt="semantic_zoom_coarse" height="60" width="700">  

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_3.png" alt="semantic_zoom_fine" height="60" width="700"> 

**Top**: only `rect` marks are represented; **Bottom:** `text` and `triangle` marks are presented when zooming in to show more details.  
[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%3F'titleK'Example%3A%20Semantic%20ZoomingM%3F'subtitleK'text%20and%20triangle%20marks%20will%20show%20when%20zooming%20in%20to%20prove%20more%20detailsM%3F'layoutK'linearM%3F'arrangementK(%0AjdirectionK'verticalM%0AjcolumnSizesK800%2C%0AjrowSizesK100%3F~%3F'tracksK%5B%3F*%3F*(%3FjdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvMJ'typeK'csvMJ'c%5EFieldK'C%5EMJ'genomicFieldsK%5B'chromStartVchromEnd'%5D%3F**~%3FjsuperposeK%5BJ(J*'markK'rectMJ*%40C%5EMJ%22J*jchr1Q2Q3Q4Q5Q6Q7Q8Q9Q10Q11Q12Q13Q14Q15Q16Q17Q18Q19Q20Q21Q22QXQY'J**%5D%2C%7D'%23F6F6F6Vgray'%3D'xK(%60StartV%3CVaggregateK'min'~J*'xeK(%60EndVaggregateK'maxV%3C'~J*'strokeWidth%262~J*'stroke%26'gray'~J*%3BMJjmeasureK'zoomLevelMJjthresholdK3%2CJjtargetK'track'J*%2BtextMJ_Rtrue)%3D'textK('%24NameVtypeK'nominal'~J*%40StainMJ%22'gnegV%25%7D'blackVblackVblackVblackVwhiteVblack'%3D%3BMJjmeasureK'widthMJjthresholdK'%7Cxe-x%7CMJj%7F10%2CJjtargetK'mark'J*~J*'styleK('textStrokeWidthK0%2BrectMJ_Rtrue)%3D%40StainMJ%22'gnegV%25%7DJ*jwhiteMJ*j%23D9D9D9MJ*j%23979797MJ*j%23636363MJ*jblackMJ*j%23A0A0F2'J**%5DJ*%2Btriangle-rMJ_J***R%3E'qVnotKfalse)J**%7B1'%2Btriangle-lMJ_J***R%3E'pVnotKfalse)J**%7B1')J)%3F**%5D%2C%3FjxK(J%60StartMJ'%3CMJ'domainK('c%5EK'1'~J'axisK'top'%3F**~%3FjxeK(%60EndV%3C'~%3Fjsize%2620~%3Fjstroke%26'gray'~%3FjstrokeWidth%260.5~%3FjstyleK('outlineK'white'~%3FjvisibilityK(J'operationK'greater-thanMJ'measureK'widthMJ'thresholdK3%2CJ'%7F5%2CJ'targetK'mark'%3F**)%3F*)%3F%5D%0A)*%20%20J%3F***K!%20M'%2CQMJ*jchrR('%24StainVoneOfK%5B'acen'%5D%2C%20'notKVM%20'_*'dataTransformK(JjfilterK%5Bj**'~)%2C%22jtypeK'nominalMJjdomainK%5B%24fieldK'%25gpos25Vgpos50Vgpos75Vgpos100Vgvar'%5D%2C%26K('valueK%2B)J~J(J*'markK'%3B'visibilityK(JjoperationK'less-than%3CtypeK'genomic%3D%5DJ*~J*%3Efalse~J***('%24NameVincludeK%3F%0A*%40'colorK(Jj%24%5Ehromosome%60'%24chrom%7B%3D'color%26'%23B4010%7DJjrangeK%5B%7FtransitionPaddingK%01%7F%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_VRQMKJ*_>)


Semantic zoom through `superpose` and `visibility`.
[`superpose`](#superposition) overlaps multiple marks on top of one other, thus allowing users to create different visualizations for the same data.
`visibility` controls the visibility of visual marks, thus allowing the switch between different visualizations based on the zoom level.

`visibility` is an object with the following properties:
| properties  | type  | description|   
|---|---|---|
|target| string| **required**, support "track" \| "mark" |
| measure | string | **required**, support "width"\|"height"\|"zoomLevel".<br/> Note that "zoomLevel" is only supported when `target="track"` |
| threshold | "\|xe-x\|" \| number | **required**|
| operation |  string | **required**, specify the logical operation to conduct between `threshold` and the `measure` of `target`<br/> > :"greater-than", "gt", "GT",<br/> < : "less-than", "lt", "LT", <br/> ≥ : "greater-than-or-equal-to", "gtet", "GTET"), <br/> ≤ : "less-than-or-equal-to", "ltet", "LTET"  |
| conditionPadding | number | buffer px size of width or height when calculating the visibility, default = 0 |
| transitionPadding | number | buffer px size of width or height for smooth transition, default = 0 |

The `visibility` of corresponding marks are decided by whether the `measure` of `target` and the `threshold` satisfy the `operation`.

For example, in the code below, text marks only show when the width (`measure`) of mark (`target`) is great-than (`peration`) 20 (`threshold`).

```javascript
{
  // example of semantic zoom: show text marks when zooming in

  "tracks":[{
    "data":...,
    "x": ...,
    "y": ...,
    // superpose overlaps bar marks and text marks for the same data
    "superpose":[
      //bar marks always show
      {"mark": "bar"},
      //text marks only show when the width of mark is great than 20 
      {
        "mark": "text",
        "visibility": {
          "operation": "greater-than",
          "measure": "width",
          "threshold": "20",
          "target": "mark",
          
        }  
      }
    ]
  }]
}
```

<!-- ## Tooltip
[source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L168) -->
