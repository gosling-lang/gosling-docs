---
title: User Interaction
---
- [Zooming and Panning](#zooming-and-panning)
- [Linking Views](#linking-views)
- [Brushing and Linking](#brushing-and-linking)

## Zooming and Panning
<!-- [:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L7) -->

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
<!-- [:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L328) -->

When views/tracks are linked, the zooming and panning performed in one view/track will be automatically applied to the linked views/tracks. 

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/362d370f31379a6d9f367d1c33adfc31>)

Views and tracks can be linked through an user-assigned id.
This id is assigned to a `track` through the `x.linkingId` property, and assigned to a `view` through the `linkingId` property.

```javascript
// linking serveral tracks
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

```javascript
// linking views and tracks
{
  "views": [
    {
      // view A
      "linkingId": "detail",
      ....
    },
    {
      // view B
      "linkingId": "detail",
      ....
    },
    {
      // view C
      "tracks":[
        {
          // this track wil be linked to view A and view B
          "x": {"linkingId": "detail", ...}, 
          ...
        },
        {...} // without the linkingId, this track will not be linked
      ]
    }
  ]
}
```

## Brushing and Linking
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
      "alignment": "overlay",
      "tracks": [
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