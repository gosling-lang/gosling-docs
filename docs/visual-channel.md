---
title: Visual Channel
---
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

- [x](#x)
- [xe](#xe)
- [y](#y)
- [ye](#ye)
- [x1 x1e y1 y1e](#x1-x1e-y1-y1e)
- [row](#row)
- [size](#size)
- [text](#text)
- [color](#color)
- [stroke](#stroke)
- [strokeWidth](#strokewidth)
- [opacity](#opacity)
- [Style](#style)


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

## x
`x` specify a mark's position in the horizontal direction.

Apart from the properties shared by all channels, `x` channel have the following unique properties:

| unique properties | type   | description                                                                                                        |
| ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| aggregate         | string | support "max", "min", "count", "mean", "bin"                                                                       |
| axis              | string | specify the axis position, support "none", "top", "bottom", "left", "right"                                        |
| linkingId         | string | a unique linkingId is needed for [linking views](#linking-views) and [Brushing and Linking](#brushing-and-linking) |


## xe
`xe` stands for the end of x axis. `xe` is usually used with `x` to specify the start position and the end position of a visual mark in the horizontal direction, respectively.

Apart from the properties shared by all channels, `xe` channel have the following unique properties:

| unique properties | type   | description                                                                 |
| ----------------- | ------ | --------------------------------------------------------------------------- |
| aggregate         | string | support "max", "min", "count", "mean", "bin"                                |
| axis              | string | specify the axis position, support "none", "top", "bottom", "left", "right" |

## y
`y` specify a mark's position in the vertical direction.

Apart from the properties shared by all channels, `y` channel have the following unique properties:

| unique properties | type             | description                                                                 |
| ----------------- | ---------------- | --------------------------------------------------------------------------- |
| axis              | string           | specify the axis position, support "none", "top", "bottom", "left", "right" |
| baseline          | string \| number |                                                                             |

## ye
`ye` stands for the end of y axis. `ye` is usually used with `x` to specify the start position and the end position of a visual mark in the vertical direction, respectively.

## x1 x1e y1 y1e
The four channels are used together only in `link` mark. In this case, `x` and `xe` are used with `x1` and `x1e` to specify a pair of genomic intervals that needs to be connected using band representations. Similarly, `y` and `ye` can be used with `y1` and `y1e` to show band connection along vertical axis.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/x_x1_example.png" width="400" alt="x x1 example"/>  



## row

Channel `row` is used with channel `y` to stratify a visualization with categorical values.

Without specifying `row`:

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/without_row.png" width="500" alt="with row example"/>  

Line charts are stratified with sample names.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/with_row.png" width="500" alt="without row example"/>  

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

## size
Channel `size` indicates the size of the visual mark. It determines either the radius of a circle (`mark: point`), the vertical length of a triangle (`mark: triangleRight`, `mark: triangleLeft`, `mark: triangleBottom`), the vertical length of a rectangle (`mark: rect`), the thickness of a line (`mark: line`).

## text

`text` channel is used only in `text` mark to specify what textual information to display.

## color
Channel `color` specifies the filling color of the mark. Binding `color` with categorical values in `bar` and `area` marks stack marks that are positioned in the same genomic intervals to better show their cumulative values.

Apart from the properties shared by all channels, the `color` channel have the following unique properties:

| unique properties | type    | description                      |
| ----------------- | ------- | -------------------------------- |
| legend            | boolean | whether to show the color legend |

## stroke
Channel `stroke` defines the outline color of the mark. Gosling supports `stroke` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

## strokeWidth
Channel `strokeWidth` defines the outline thickness of the mark shape. Gosling supports `strokeWidth` in the following marks: `rect`, `area`, `point`, `bar`, `link`.

## opacity
Channel `opacity` specifies the opacity of the mark shape.
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->



## Style

`style` specifies the visual appearances of a track that are not bound with data fields.

| style properties | type                                                   | description                              |
| ---------------- | ------------------------------------------------------ | ---------------------------------------- |
| background       | string                                                 | color of the background                  |
| dashed           | [number, number]                                       |
| linePatterns     | { "type": "triangleLeft" \| "triangleRight"; size: number } |
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
