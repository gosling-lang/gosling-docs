- [layout](#layout)
- [tracks](#tracks)
    - [track.title](#tracktitle)
    - [track.data](#trackdata)
    - [track.metadata](#trackmetadata)
    - [track.x](#trackx)
    - [track.y](#tracky)
    - [track.row](#trackrow)
    - [track.mark](#trackmark)
    - [track.color](#trackcolor)
    - [track.stroke](#trackstroke)
    - [track.strokeWidth](#trackstrokewidth)
    - [track.opacity](#trackopacity)
    - [track.superpose](#tracksuperpose)

# layout
`object`

|  property | type | description |  
|---        |---   |     ---   |  
| layout.type  | `string`  |**Required**, specify the type of layout (`linear` or `circular`)|
| layout.direction | `string`| **Required**, the layout direction of tracks (`vertical`   or `horizontal`)|  
| layout.wrap | `number` |  |  
| layout.rowSizes | `number|Array<number>` |  |  
| layout.rowGaps | `number|Array<number>` |  |  
| layout.columnSizes | `number|Array<number>` |  |  
| layout.columnGaps | `number|Array<number>` |  |  


<!-- https://github.com/sehilyi/geminid/blob/3f8e6db2fa80945de95266f4ea70a26387603d53/src/core/geminid.schema.ts -->
# tracks
`array`
one track is defined by the following options
### track.title
`string`, 
### track.data
- url
- type
### track.metadata
### track.x
### track.y
### track.row
<!-- is there also a track.column? -->
### track.mark
<!-- it is a littel bit confusing for me to understand the difference between rect and bar. Also confused about the encoding of width and height-->

<!-- a little bit confusing that x, y indicate both the axes and the encoding of the mark, even though vega lite employs the same strategy -->

<!-- Another question, how can I rotate a chart, for example, the area chart in basic marks, 90 degree? (maybe this is a rare case in gemonic visualization?)
 -->
### track.color
<!-- I didn't see the legend (when set legend: true) of color when {"type": "quantitative"} -->
### track.stroke
### track.strokeWidth
### track.opacity
<!-- will it be better if we merge stroke, strokeWidth, background, opacity into a style option? -->
### track.superpose
overlay another track on the original track. 
Superpose share the same options as the original track unless it is specified.