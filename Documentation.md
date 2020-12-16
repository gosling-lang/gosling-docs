- [Data](#Data)
- [layout](#layout)
- [tracks](#tracks)
    - [track.title](#tracktitle)
    - [track.data](#trackdata)
    - [track.metadata](#trackmetadata)
    - [track.mark](#trackmark)
    - [track.x](#trackx)
    - [track.xe](#trackxe)
    - [track.y](#tracky)
    - [track.ye](#trackye)
    - [track.row](#trackrow)
    - [track.color](#trackcolor)
    - [track.stroke](#trackstroke)
    - [track.strokeWidth](#trackstrokewidth)
    - [track.opacity](#trackopacity)
    - [track.style](#trackstyle)
    - [track.superpose](#tracksuperpose)
    - [track.innerRadius](#trackinnerradius)
    - [track.outterRadius](#trackoutterradius)

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
### CSV

# layout
`object`  
specify the layout of tracks

|  property | type | description |  
|---        |---   |     ---   |  
| layout.type  | `string`  |**Required**, specify the type of layout (`linear` or `circular`)|
| layout.direction | `string`| **Required**, the layout direction of tracks (`vertical`   or `horizontal`)|  
| layout.wrap | `number` | specify the number of tracks at each row (when `direction:horizontal`) or at each column (when `direction:vertical`). default value = infinite |  
| layout.rowSizes | `number` \| `Array<number>` |  |  
| layout.rowGaps | `number` \| `Array<number>` |  |  
| layout.columnSizes | `number` \| `Array<number>` |  |  
| layout.columnGaps |`number` \| `Array<number>`  |  |  

<img src="https://github.com/sehilyi/geminid/wiki/images/layout_demo.png" alt="layout demo" width="400">

<!-- is it possible that several tracks under one layout have different type (linear and circular) -->

# tracks

<!-- it seems that, based on the value of mark, a track has different options, i am not sure whether this is confusing -->

an `array` of single tracks  
one single track is defined by the following options
### track.title
`string`, 
### track.data
- url
- type
### track.metadata
<!-- this is most confusing part -->
### track.mark
<!-- it is a littel bit confusing for me to understand the difference between rect and bar. Also confused about the encoding of width and height-->

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