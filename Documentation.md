- [Overview](#Overview)
- [Data](#Data)
    - [Multivec (HiGlass)](#Multivec-HiGlass)
    - [BED (HiGlass)](#BED-HiGlass)
    - [BED](#BED)
    - [Vector (HiGlass)](#Vector-HiGlass)
    - [CSV](#CSV)
    - ...
- [Data Transform](#Data-Transform) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L98-->
- [Mark](#Mark)
    - [Point](#Point)
    - [Line](#Line)
    - [Area](#Area)
    - [Bar](#Bar)
    - [Rect](#Rect)
    - [Text](#Text)
    - [Link](#Link)
    - [Rule](#Rule)
    - [Triangle](#Triangle)
    - [Brush](#Brush)
    - [Glyph](#Glyph)
- [Encoding](#tracks)
    - [title](#tracktitle)
    - [x](#trackx)
    - [xe](#trackxe)
    - [y](#tracky)
    - [ye](#trackye)
    - [row](#trackrow)
    - [color](#trackcolor)
    - [stroke](#trackstroke)
    - [strokeWidth](#trackstrokewidth)
    - [opacity](#trackopacity)
    - [style](#trackstyle)
    - [superpose](#tracksuperpose) <!--I think this can be moved to Arrangement section-->
    - [innerRadius](#trackinnerradius) <!--I think this can be moved to Circular Layout section-->
    - [outterRadius](#trackoutterradius) <!--I think this can be moved to Circular Layout section-->
- [Layout](#Layout) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L22-->
    - [Linear Layout](#Linear-Layout)
    - [Circular Layout](#Circular-Layout)
- [Arrangement](#Arrangement)
    - [Grid-based Arrangement](#Grid-based-Arrangement) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L20-->
    - [Superposition](#Superposition) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L213-->
- [Semantic Zoom](#Semantic-Zoom) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L203-->
- [Interaction](#Interaction)
    - [Zooming and Panning](#Zooming-and-Panning) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L7-->
    - [Linking Views](#Linking) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L328-->
    - [Tooltip](#Tooltip) <!--https://github.com/sehilyi/geminid/blob/00a7b5c6a95528dbabdb2444ef469a1448689d3b/src/core/geminid.schema.ts#L168-->

# Overview

# Data

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

# Mark
### Point
### Line
### Area
### Bar
### Rect
### Text
### Link
### Rule
### Triangle
### Brush
### Glyph
<!-- This will cover the `superpose`, mostly in the perspective of making a glyph (e.g., gene annotation) -->

# Layout
This determines the layout of a track, either `circular` or `linear`.

|  property | type | description |  
|---        |---   |     ---   |  
| layout    | `string`  |**Required**, specify the type of layout (`linear` or `circular`)|

# Arrangement
`object`  
specify the arrangement of tracks

|  property | type | description |  
|---        |---   |     ---   |  
| arrangement.direction | `string`| **Required**, the layout direction of tracks (`vertical`   or `horizontal`)|  
| arrangement.wrap | `number` | specify the number of tracks at each row (when `direction:horizontal`) or at each column (when `direction:vertical`). default value = infinite |  
| arrangement.rowSizes | `number` \| `Array<number>` |  |  
| arrangement.rowGaps | `number` \| `Array<number>` |  |  
| arrangement.columnSizes | `number` \| `Array<number>` |  |  
| arrangement.columnGaps |`number` \| `Array<number>`  |  |  

<img src="https://github.com/sehilyi/geminid/wiki/images/layout_demo.png" alt="layout demo" width="400">

<!-- is it possible that several tracks under one layout have different type (linear and circular) -->

# tracks

<!-- it seems that, based on the value of mark, a track has different options, i am not sure whether this is confusing -->

an `array` of single tracks  
one single track is defined by the following options
### track.title
`string`, 

### track.x
### track.xe
### track.y
### track.ye
### track.row



<!-- a little bit confusing that x, y indicate both the axes and the encoding of the mark, even though vega lite employs the same strategy -->

<!-- Another question, how can I rotate a chart, for example, the area chart in basic marks, 90 degree? (maybe this is a rare case in gemonic visualization?)
 -->

---

### track.color
<!-- I didn't see the legend (when set legend: true) of color when {"type": "quantitative"} -->
### track.stroke
### track.strokeWidth
### track.opacity
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->
### track.style

---

### track.superpose
overlay another track on the original track. 
Superpose share the same options as the original track unless it is specified.

---

only useful when `{"type": "circular"}`

### track.innerRadius
### track.outterRadius