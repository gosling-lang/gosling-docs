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

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/362d370f31379a6d9f367d1c33adfc31>)

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

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/5f48d40b8f2335abe40c289ae85cb4ae>)

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