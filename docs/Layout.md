---
title: Layout
---
In each track, genomic coordinate can be represented in either a circular or linear layout. 

In the following figure the upper track is using a linear layout while the bottom one is a circular layout.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/linear_circular.png" alt="linear vs circular" width="600"/>    

[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L22)

Users can either specify the layout of entire tracks on the root level

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
    ...
}
```

For `circular` layout, you can modify the following visual parameters:

| property    | type   | description                                  |
| ----------- | ------ | -------------------------------------------- |
| outerRadius | number | default = min(track.width, track.height) / 2 |
| innerRadius | number | default = max(outerRadius - 80, 0)           |
| startAngle  | number | default = 0                                  |
| endAngle    | number | default = 360                                |

