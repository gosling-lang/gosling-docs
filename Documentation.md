# Overview
Gosling is a declarative visualization grammar tailored for interactive genomic visualizations. In Gosling, users can create visualizations through a JSON syntax. This documentation describes how to write the JSON specification to create interactive visualizations.
You are welcome to try the [Gosling online editor](https://gosling-lang.github.io/gosling.js/)!

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
- [Genome Build](https://github.com/gosling-lang/gosling.js/wiki/Genome-Builds)
- [Data](https://github.com/gosling-lang/gosling.js/wiki/Data)
  - [CSV](https://github.com/gosling-lang/gosling.js/wiki/Data#csv)
  - [JSON](https://github.com/gosling-lang/gosling.js/wiki/Data#json)
  - [BigWig](https://github.com/gosling-lang/gosling.js/wiki/bigwig)
  - [Vector](https://github.com/gosling-lang/gosling.js/wiki/Data#vector)
  - [Multivec](https://github.com/gosling-lang/gosling.js/wiki/Data#multivec)
  - [BED](https://github.com/gosling-lang/gosling.js/wiki/Data#bed)
  - [Data Transform](https://github.com/gosling-lang/gosling.js/wiki/Data#data-transform)
- [Mark](https://github.com/gosling-lang/gosling.js/wiki/Mark)
  - [Point](https://github.com/gosling-lang/gosling.js/wiki/Mark#point)
  - [Line](https://github.com/gosling-lang/gosling.js/wiki/Mark#line)
  - [Area](https://github.com/gosling-lang/gosling.js/wiki/Mark#area)
  - [Bar](https://github.com/gosling-lang/gosling.js/wiki/Mark#bar)
  - [Rect](https://github.com/gosling-lang/gosling.js/wiki/Mark#rect)
  - [Text](https://github.com/gosling-lang/gosling.js/wiki/Mark#text)
  - [Link](https://github.com/gosling-lang/gosling.js/wiki/Mark#link)
  - [Triangle](#triangle)
- [Visual Channel](#visual-channels-of-mark)
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
  - [Semantic Zooming](#semantic-zooming)



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
        "type": "genomic"
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


As the table shown below, different marks have different visual channels.

| mark type               | supported visual channels                                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [`point`](#point)       | [`x`](#x), [`y`](#y), [`row`](#row), [`size`](#size), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity) |
| [`line`](#line)         | [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth)                                         |
| [`rect`](#rect)         | [`x`](#x), [`xe`](#xe), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity)                |
| [`bar`](#bar)           | [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth), [`opacity`](#opacity)                  |
| [`area`](#area)         | [`x`](#x), [`y`](#y), [`row`](#row), [`color`](#color), [`strokeWidth`](#strokeWidth)                                         |
| [`link`](#link)         | [`x`](#x), [`xe`](#xe), [`x1`](#x1-y1-x1e-y1e), [`x1e`](#x1-y1-x1e-y1e), [`color`](#color), [`opacity`](#opacity)             |
| [`triangle`](#triangle) | [`x`](#x), [`xe`](#xe), [`row`](#row), [`size`](#size), [`color`](#color), [`opacity`](#opacity)                              |
| [`text`](#text)         | [`x`](#x), [`xe`](#xe), [`row`](#row), [`color`](#color), [`opacity`](#opacity)                                               |

A visual channel can be either assigned a constant value or bound with a data field. When a visual channel is bound with a data field, Gosling creates a mapping from the values of the data field (e.g., [gnes, gpos25, gpos50, ...]) to the values of the visual channel (e.g., position of a bar). We call the values of data field **domain** and the values of the visual channel **range**.

**Table: Properties shared by all visual channels**

| visual channel properties | type                        | description                                                                        |
| ------------------------- | --------------------------- | ---------------------------------------------------------------------------------- |
| field                     | string                      | specify name of the data field                                                     |
| type                      | string                      | specify type of the data field. support `"genomic"`, `"nominal"`, `"quantitative"` |
| aggregate                 | string                      | support `"max"`, `"min"`, `"mean"`, `"bin"`, `"count"`                             |
| domain                    | [number, number]\| string[] | specify values of the data field                                                   |
| range                     | [number, number]\| string[] | specify values of the visual channel                                               |
| value                     | string \| number            | assign a constant value to the visual channel                                      |



For example, the code below creates a mapping from the data `field` "Stain" to the color of the `rect` mark. 
"gneg" will show as a white rect mark, "gpos100" will show as a black rect mark.
```javascript
{
  "tracks": [{
    "mark": "rect",
    "color": {
      "field": "Stain",
      "type": "nominal",
      "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
      "range": ["white", "#D9D9D9", "#979797", "#636363", "black", "#A0A0F2"]
    },
    ... // other visual channels
  }]
}
```

### x
`x` specify a mark's position in the horizontal direction.

Apart from the properties shared by all channels, `x` channel have the following unique properties:
| unique properties | type   | description                                                                                                        |
| ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| aggregate         | string | support "max", "min", "count", "mean", "bin"                                                                       |
| axis              | string | specify the axis position, support "none", "top", "bottom", "left", "right"                                        |
| linkingID         | string | a unique linkingID is needed for [linking views](#linking-views) and [Brushing and Linking](#brushing-and-linking) |


### xe
`xe` stands for the end of x axis. `xe` is usually used with `x` to specify the start position and the end position of a visual mark in the horizontal direction, respectively.

Apart from the properties shared by all channels, `xe` channel have the following unique properties:
| unique properties | type   | description                                                                 |
| ----------------- | ------ | --------------------------------------------------------------------------- |
| aggregate         | string | support "max", "min", "count", "mean", "bin"                                |
| axis              | string | specify the axis position, support "none", "top", "bottom", "left", "right" |

### y
`y` specify a mark's position in the vertical direction.

Apart from the properties shared by all channels, `y` channel have the following unique properties:
| unique properties | type             | description                                                                 |
| ----------------- | ---------------- | --------------------------------------------------------------------------- |
| axis              | string           | specify the axis position, support "none", "top", "bottom", "left", "right" |
| baseline          | string \| number |                                                                             |

### ye
`ye` stands for the end of y axis. `ye` is usually used with `x` to specify the start position and the end position of a visual mark in the vertical direction, respectively.

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

Apart from the properties shared by all channels, the `color` channel have the following unique properties:
| unique properties | type    | description                      |
| ----------------- | ------- | -------------------------------- |
| legend            | boolean | whether to show the color legend |

### stroke
Channel `stroke` defines the outline color of the mark. Gosling supports `stroke` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

### strokeWidth
Channel `strokeWidth` defines the outline thickness of the mark shape. Gosling supports `strokeWidth` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

### opacity
Channel `opacity` specifies the opacity of the mark shape.
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->



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
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L22)
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
        "outerRadius": 260;
        "innerRadius": 100;
        "startAngle": 180; // [0, 360]
        "endAngle": 360; // [0, 360]
        ...
      },
      ...
    ],
    ...//
}
```

For `circular` layout, users can specify more details about the layout using the following properties
| property    | type   | description                                  |
| ----------- | ------ | -------------------------------------------- |
| outerRadius | number | default = min(track.width, track.height) / 2 |
| innerRadius | number | default = max(outerRadius - 80, 0)           |
| startAngle  | number | default = 0                                  |
| endAngle    | number | default = 360                                |


## Arrangement

### Grid-based arrangement
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L20)  
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
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)


`superposition` enables users to superpose multiple marks on top of each other.  
`superposition` is an array of objects, each object specifies one visual mark. Each visual mark inherits the properties (e.g., `data`, `x`, `y`) defined in this track, unless these properties are redefined in this object.  

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

| style properties | type                                                   | description                              |
| ---------------- | ------------------------------------------------------ | ---------------------------------------- |
| background       | string                                                 | color of the background                  |
| dashed           | [number, number]                                       |
| linePatterns     | { "type": "triangle-l" \| "triangle-r"; size: number } |
| curve            | string                                                 | support "top", "bottom", "left", "right" |
| align            | string                                                 | support "left", "right"                  |
| dy               | number                                                 |
| outline          | string                                                 |
| outlineWidth     | number                                                 |
| circularLink     | boolean                                                |
| textFontSize     | number                                                 |
| textStroke       | string                                                 |
| textStrokeWidth  | number                                                 |
| textFontWeight   | string                                                 | support "bold", "normal"                 |

<!-- TODO: add channel.flip, channel.grid and other properties  -->



# Interactions

## Zooming and Panning
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L7)

Each visualization in Gosling supports the Zooming and Panning interaction.
Users can zoom in/out a visualization using the scrolling up/down actions.
Users can pan by clicking on the visualization and then drag it in the desired direction.

Zooming and panning are controlled through the `static` property, which has a default value of `false`.
When `static = true`, zooming and panning are disabled.
Users can set the `static` property of all tracks at the root level or specify it in a single track definition. 
```javascript
{
  "static": true, //disable zoom & pan for all tracks
  "tracks": [
    {
      "static": false, // enable zoom & pan for this track
      ...
    },
    {
      ...
    },
    ...
  ]
}
```


## Linking Views
[:link: source code](ttps://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L328)

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
        "linkingID": "a unique string" // assign a linking id for the track A
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
Users can use **brushing** to select a subset of the data items using a rectangle. Users can modify the left and right edge of the rectangle to modify the selection. The selected data items can be linked to data items in another track.

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


## Semantic Zooming
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L278)

Semantic zoom allows users to switch between different visualizations of the same data through zooming in/out. When zooming in, the same data will be represented in a different way in which more details are shown. 

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_0.png" alt="semantic_zoom_coarse" width="700">  

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_1.png" alt="semantic_zoom_fine" width="700">

**Top**: only `bar` marks are represented; **Bottom:** `text` marks are presented when zooming in.  

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'titleNExample%3A%20Semantic%20Zooming'V'subtitleNhide%25annotation%20and%20only%20show%20bar%20charts%20when%20zooming%20out'V'arrangement6(J*'directionNvertical'V*'columnSizes6800V*'rowSizes6180J)V'tracks6%5BJ*(JLdata6(5'urlNhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DWipsnEDMStahGPpRfH9adA'BQtileset'J**)VLmetadata6(5Qhiglass-multivec'B'rowNbase'B'columnN%3C'valueNcount'B'categoriesjstartNstart'B'endNend'J**)V**%20'x6(5'U%3CQ%24B'domain6KB'axisNtop'J**)VLcolor6(5'Ubase'BQnominal'B'domainjlegend6trueJ**)VLy6%3BQquantitative')VLsuperpose6%5B5(%2B)B(5*%2BB*'s%26~61)B*'stroke%3EXgtet'BY620I5L%221%235)B%2F%2F%25mark5(5*'dataTransform6(5Lfilter6%5B%3B'oneOf6%5B0%5DI'not6true)%5D5*)B*'markNtext'B*'x6(5LUstart'BLtypeN%24BLdomain6KBLaxisNtop'5*)B*'xe6('Uend'IQ%24)B*'color%3E*'y~670)BXless-than'BYN%7Cxe-x%7C'5**I'%223%23B*%20'text6('Ubase'IQnominal')B'style6(5LtextFontSize624BLtextS%2660BLtextFontWeightNbold'5)5)J**%5DJ*%20J*%20J*)J%5D%0A)*%20%205J***6!%20B%2C5I%2C%20J%0A*K('chromosomeN1'I'interval6%5B3000000I3000010%5D)L**'N6'Q'typeNUfieldNV%2CJX*'visibility6(5LoperationNYLmeasureNwidth'BLthresholdj6%5B'A'I'T'I'G'I'C'%5DB'~6('value%22transitionPadding6%230BLtargetNmark'5*)%24genomic'%25%20text%20%26trokeWidth%2B'markNbar'%3B('Ucount'I%3Cposition'B%3E~Nwhite')B%01%3E%3C%3B%2B%26%25%24%23%22~jYXVUQNLKJIB65*_>)

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_2.png" alt="semantic_zoom_coarse" height="60" width="700">  

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_3.png" alt="semantic_zoom_fine" height="60" width="700"> 

**Top**: only `rect` marks are represented; **Bottom:** `text` and `triangle` marks are presented when zooming in to show more details.  
[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%3F'titleK'Example%3A%20Semantic%20ZoomingM%3F'subtitleK'Text%20and%20triangle%20marks%20will%20show%20when%20zooming%20in%20to%20provide%20more%20detailsM%3F'layoutK'linearM%3F'arrangementK(%0AjdirectionK'verticalM%0AjcolumnSizesK800%2C%0AjrowSizesK60%3F~%3F'tracksK%5B%3F*%3F*(%3FjdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvMJ'typeK'csvMJ'c%5EFieldK'C%5EMJ'genomicFieldsK%5B'chromStartVchromEnd'%5D%3F**~%3FjsuperposeK%5BJ(J*'markK'rectMJ*%40C%5EMJ%22J*jchr1Q2Q3Q4Q5Q6Q7Q8Q9Q10Q11Q12Q13Q14Q15Q16Q17Q18Q19Q20Q21Q22QXQY'J**%5D%2C%7D'%23F6F6F6Vgray'%3D'xK(%60StartV%3CVaggregateK'min'~J*'xeK(%60EndVaggregateK'maxV%3C'~J*'strokeWidth%262~J*'stroke%26'gray'~J*%3BMJjmeasureK'zoomLevelMJjthresholdK3%2CJjtargetK'track'J*%2BtextMJ_Rtrue)%3D'textK('%24NameVtypeK'nominal'~J*%40StainMJ%22'gnegV%25%7D'blackVblackVblackVblackVwhiteVblack'%3D%3BMJjmeasureK'widthMJjthresholdK'%7Cxe-x%7CMJj%7F10%2CJjtargetK'mark'J*~J*'styleK('textStrokeWidthK0%2BrectMJ_Rtrue)%3D%40StainMJ%22'gnegV%25%7DJ*jwhiteMJ*j%23D9D9D9MJ*j%23979797MJ*j%23636363MJ*jblackMJ*j%23A0A0F2'J**%5DJ*%2Btriangle-rMJ_J***R%3E'qVnotKfalse)J**%7B1'%2Btriangle-lMJ_J***R%3E'pVnotKfalse)J**%7B1')J)%3F**%5D%2C%3FjxK(J%60StartMJ'%3CMJ'domainK('c%5EK'1'~J'axisK'top'%3F**~%3FjxeK(%60EndV%3C'~%3Fjsize%2620~%3Fjstroke%26'gray'~%3FjstrokeWidth%260.5~%3FjstyleK('outlineK'white'~%3FjvisibilityK(J'operationK'greater-thanMJ'measureK'widthMJ'thresholdK3%2CJ'%7F5%2CJ'targetK'mark'%3F**)%3F*)%3F%5D%0A)*%20%20J%3F***K!%20M'%2CQMJ*jchrR('%24StainVoneOfK%5B'acen'%5D%2C%20'notKVM%20'_*'dataTransformK(JjfilterK%5Bj**'~)%2C%22jtypeK'nominalMJjdomainK%5B%24fieldK'%25gpos25Vgpos50Vgpos75Vgpos100Vgvar'%5D%2C%26K('valueK%2B)J~J(J*'markK'%3B'visibilityK(JjoperationK'less-than%3CtypeK'genomic%3D%5DJ*~J*%3Efalse~J***('%24NameVincludeK%3F%0A*%40'colorK(Jj%24%5Ehromosome%60'%24chrom%7B%3D'color%26'%23B4010%7DJjrangeK%5B%7FtransitionPaddingK%01%7F%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_VRQMKJ*_>)


Semantic zoom through `superpose` and `visibility`.
[`superpose`](#superposition) overlaps multiple marks on top of one other, thus allowing users to create different visualizations for the same data.
`visibility` controls the visibility of visual marks, thus allowing the switch between different visualizations based on the zoom level.

`visibility` is an object with the following properties:
| properties  | type  | description|   
|---|---|---|
|target| string| **required**, support "track" \| "mark" |
| measure | string | **required**, support "width"\|"height"\|"zoomLevel".|
| threshold | "\|xe-x\|" \| number | **required**, when using `number`, the unit of a number is pixel with `width` and `height` measures while it is a base pair (bp) with `zoomLevel` |
| operation |  string | **required**, specify the logical operation to conduct between `threshold` and the `measure` of `target`<br/> > :"greater-than", "gt", "GT",<br/> < : "less-than", "lt", "LT", <br/> ≥ : "greater-than-or-equal-to", "gtet", "GTET"), <br/> ≤ : "less-than-or-equal-to", "ltet", "LTET"  |
  | conditionPadding | number | buffer px size of width or height when calculating the visibility, default = 0 |
| transitionPadding | number | buffer px size of width or height for smooth transition, default = 0 |

The `visibility` of corresponding marks are decided by whether the `measure` of `target` and the `threshold` satisfy the `operation`.

For example, in the code below, text marks only show when the width (`measure`) of the mark (`target`) is great-than (`operation`) 20 (`threshold`).

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
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L168) -->
