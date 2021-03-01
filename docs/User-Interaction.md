# Zooming and Panning
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

<!-- ## Tooltip
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L168) -->

# Linking Views
[:link: source code](ttps://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L328)

When two tracks are linked, the zooming and panning performed in one track will be automatically applied to the linked track. 

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0AOlayout!6linear%5E%0AOarrangementC('direction!6vertical%5E6columnSizesC800%2C6rowSizesC200)%2C%0AOtracksC%5B%24E%22Gj%2Bb%40M3%5E%23%204%3Eline%25bNX*OaxKa%26*GZGrowBGcolorB%2C6%3CT%3B%2C%24E%22Gj%2Bb%40M2%3Earea%25bNX*OaxKthe%20same%26%20as%20the%20first%20track*GZGrowBGcolorB~%3CT%3B%0A%20%20%5D%0A)*J%20O%20'9%5E*OBC('field!%23%5E6Nnominal'C!%20Ehttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHuG)%2C*'J%0A%20%20%20%20Kis!6top9linkingId!6link1'%20%2F%2F%20assign%20Mpeak9categoriesC%5B'sample%201%5E%23%20Ntype!6O%206TstrokeC('%40white'GstrokeWidthC('Xgenomic9domainC('chromosome!62')%2CZyC('field!6peak%5E6Nquantitative'b!6position9jmetadataC(*ONhiglass-multivec%22RDiYA3qwFlm7xQ9Ntileset'*%236sample%24J(*'dataC(*Ourl!6%25%5E*'xC(*Ofield%26%20linking%20id%2B9row!%239column%3BvalueC0.5)J)%3ClegendCtrueG%3E'%5D*Gmark!6%40value!6%5E'%2C%01%5E%40%3E%3C%3B%2B%26%25%24%23%22jbZXTONMKJGECB96*_>)

Users can link two tracks by assigning the same `linkingId` to the `x` channel of the two tracks.
```javascript
{
  "tracks":[
    // track A
    {
      "data": ...,
      "mark": "rect",
      "x": {
        ..., // other properties of x channel
        "linkingId": "a unique string" // assign a linking id for the track A
      }
    },
    // track B
    {
      "data": ...,
      "mark": "point",
      "x": {
        ..., // other properties of x channel
        "linkingId": "a unique string" // the same linking id links track A and track B
      }
    },
    ... // other tracks
  ]
}
```

# Brushing and Linking
Users can use **brushing** to select a subset of the data items using a rectangle. Users can modify the left and right edge of the rectangle to modify the selection. The selected data items can be linked to data items in another track.

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(W'title~Example%3A%20Brushing%20and%20Linking'%2CW'layout~linear'%2CW'arrangement5('direction~vertical'O'columnSizes5800O'rowSizes5200ZW'tracks5%5B%229uRN*JXM%23G%24MK1'%25*Z*C**%2F%2F%20create%20a%20rectangle%20brush*'superpose5%5B*4()O%2F%2F%20this%20dummy%20object%20cannot%20be%20removed*4('mark~rect-brush'O*4'x5('T)6color5('value!'steelBlue')*4)*%5DW4Z%229uRN*JXM%23G%24MK1'O'interval5%5B200000000O220000000%5D%256T*Z*C*'opacity!('value51)W4)W%5D%0A)*W444%20%205!%206%2C*4'9'https%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHC'y5('field~peak'O'type~quantitative'ZGories5%5B'sample%201'%5D*Z*'mark~line'%2CJ'metadata5(*4'type~higlass-multivec'Ktype~genomic'6domain5('chromosome~M~position'6NDiYA3qwFlm7xQ'6type~tileset'*ZO%2C%20TlinkingId~linking-with-brush'W%0A4X6row~sample'6columnZ)%2C~5'%22W4(*'data5(*4'url5%23value~peak'6categ%24*'x5(*4'field%25)6axis~top'%01%25%24%23%22~ZXWTONMKJGC9654*_>)

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
          "x": {"linkingId": "linking-with-brush"}, // assign a unique id to the brush
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
        "linkingId": "a unique string" // the same linking id links track B and the brush in track A
      }
    },
    ... // other tracks
  ]
}
```