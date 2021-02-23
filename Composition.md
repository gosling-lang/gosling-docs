
## Overlayed Tracks
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)


Gosling enables you to overlay multiple tracks/marks on top of each other. There are two ways for overlaying: specifying all overlayed marks/tracks in `overlay`, overlaying one `track` to previous `track` using `track.overlayOnPreviousTrack: true`.

One `overlay` is composed of an array of objects, in which each object specifies one visual mark. Each visual mark inherits the properties (e.g., `data`, `x`, and `y`) defined in the corresponding track definition unless these properties are redefined in this object.  

```javascript
{
  "tracks": [
    {
      "data": ... , // specify data
      "x": ...,
      "y": ...,
      "color":...,
      "overlay": [
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

When ``track.overlayOnPreviousTrack: true`, a `track` is overlayed on its previous track.
```javascript
{
  "tracks": [
    //first track
    {...},
    // second track that is overlayed on the first track
    {
      ...,
      "overlayOnPreviousTrack": true
    }
  ]
}
```

Try it in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'jtleXExample%3A%20overlayd%20TracksCJ'layoutXlinearCJ'arrangementB(J*'direcjonXverjcalCJ*'columnSizesB800%2CJ*'rowSizesB450J)%2CJ'tracksZJ*(9'dataB(9*'urlXhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Fjleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQWIjleset'9M'metadataB(9*Ihiglass-muljvecW'rowBGW'columnXposijonW'valueXpeakW'categoriesZ~1O~2O~3O~4'%5D9M'overlayZ9*('markXline'M*(9**'markXpointW*'sizeKO'rangeZ0%2C%206%5D)9*)9%5D%2C9'xB(9*bXposijonWIgenomicW'domainB('chromosomeX1O'intervalZ1%2C%203000500%5DM*'axisXtop'9M'yK'M'rowNM'colorN)J*)J%5D%0A)*%20%209J**B!%20C'%2CG'sampleI'typeXJ%0A*KB(bXpeakOIquanjtajveM)%2C9NB(bBGOInominal'OC%20WC9*XB'ZB%5Bb'fieldjti~G%20%01~jbZXWONMKJIGCB9*_>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0A*'titleG'Example%3A%20overlayd%20Tracks'%25*'layoutG'linear'%25*'arrangementG(%0AQ'directionG'vertical'%25Q'columnSizesG800%25Q'rowSizesG200%0A*)%25*'tracksY%0A*%20%0AQ(C'dataG(C*'urlG'https%3A%2F%2Fcgap-higlass.com%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3Dclinvar_20200824_hg38'A%24tileset'CjmetadataG(C*%24higlass-bed'A'%3EFieldsYCQ%3B1%3Cstart')A*%3B2%3Cend')CqA'valueFieldsY%3B7%3CIZO)%5DCjoverlayYC*%5Ebar'A*'strokeG(CQ*XIAQOAQ~YC%7BHQ'HQRQ*'JQV%2FJ%40CQ*KQKQKQ%2BQMAQMAQMCQqCQ)A*'strokeWidth%220.5)%601)C*)A%5Epoint'%605)A*'colorG(CQ*XIAQOAQ~YC%7BHQ'HQRQ*'JQV%2FJ%40CQ*KQKQKQ%2BQMAQMAQMCQqAQ'legendGtrueCQ)C*)C%5D%2CC'xG(C*Xstart'A%24%3E'A~G('chromosomeG'3')A'axisG'top'CjxeG(Xend'Z%24%3E'jyG(C*XIAOA~YC*N'AN%2FH'HR*'JV%2FJV'CqA'baselineGR%26150Z20%5DA'gridGtrueCjcolorG(C*XIAOA~YC*N'AN%2FH'HR*'JV%2FJV'CqA%26C*KKK%2BMAMAMCqCjopacity%220.6)%0AQ)%0Aq%0A)*%20%20A%2CC*C%0AQ*G!%20HLikely_pathogenic'A*Isignificance'JLikely_benign'A*K*'%23D45E00'AM*'%23029F73'N*'PathogenicO%24nominal'Q**R'Uncertain_IAV'BenignX'fieldG'YG%5BZ%2C%20j)%2CC'q*%5D~'domain%22G('valueG%24'typeG'%25%2C%0A%26'rangeY%2B*'black'A%3B('indexG%3CZ'nameG'%3Egenomic%40QV'CQqAQ%26%5E(CQ'markG'%60A*'size%22%7BQ*N'AQN%2F%01%7B%60%5E%40%3E%3C%3B%2B%26%25%24%22~qjZYXVRQONMKJIHGCA*_>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(V'titleK'Example%3A%20overlayd%20Tracks'_'layoutK'linear'_'arrangementK(V*'directionK'vertical'_*'columnSizesK800_*'rowSizesK80V)_'tracksK%5BV*(VXdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csv'Q'typeK'csv'Q'c%3CFieldK'C%3C'Q'genomicFieldsK%5B'%60LchromEnd'%5DV**)_XoverlayK%5BJ%7Dtext'QRMtrue)~textK('YNameL%25)Q*'%3BX%25QXZ%22'%40L%40L%40L%40LwhiteL%40'~visibilityK(JXoperationK'less-than'QXconditionK('widthK'%7Cxe-x%7CLtransitionPaddingK10)QXtargetK'mark'J*)Q*'styleK('textS%7BK0%26rect'QRMtrue)~%3BX%25QXZ%22J*Xwhite%3DD9D9D9%3D979797%3D636363'Q*X%40%3DA0A0F2'J**%5DJ*%5E-r'QRJ***M%24'q%3F~%2B%5E-l'QRJ***M%24'p%3F~%2B)J)V**%5D_XxK(J'Y%60'Q'%3EQ'domainK('c%3CK'1')Q'axisK'top'V**)_XxeK('YchromEndL%3E)_Xsizej20)_Xstrokej'gray')_Xs%7Bj0.5)_XstyleK('outlineK'white')V*)V%5D%0A)*%20%20JV***K!%20L'%2C%20'M('YStainLoneOfK%5B'acen'%5D%2C%20'notKQ%2CJR*'dataTransformK(JXfilterK%5BV%0A*X**'YfieldK'ZdomainK%5B'gnegLgpos25Lgpos50Lgpos75Lg_%2CVjK('valueK~%5DJ*)Q*'%22pos100Lgvar'%5DQXrangeK%5B%24false)Q***('YNameLincludeK%25typeK'nominal'%26)J)Q%7D%2Bcolorj'%23B40101'%3BcolorK(JXYStain'Q%3Chromosome%3D'Q*X%23%3EtypeK'genomic'%3FLnotKfalse)J**%40black%5E%26triangle%60chromStart%7BtrokeWidth%7D(J*'markK'%01%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_ZYXVRQMLKJ*_>)


## Multiple Tracks
Each track of the `tracks` share the same `layout` preporty and are vertically concantenated.
<table>
    <tr>
        <td>  
        <pre>
<code>
{
  "layout": "linear",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/},
    {/**track_3**/}
  ]   
}
</code>
        </pre>
        </td>
        <td>
        <pre>
<code>
{
  "layout": "circular",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/},
    {/**track_3**/}
  ]   
}
</code>
        </pre>
        </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tracks_linear.png" alt="linear tracks" width="400"/> </td>
        <td> <img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tracks_circular.png" alt="circular tracks" width="200"/></td>
    </tr>
</table>

`tracks` compose one single `view`, which has the following properties:
|property|type|description|
|--|--|--|
| layout | string | specify the layout type, either "linear" or "circular" |
| spacing | number | specify the space between tracks|
| static | boolean | whether to disable [Zooming and Panning](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#zooming-and-panning), default=false. | 
| assembly | string | currently support "hg38", "hg19", "hg18", "hg17", "hg16", "mm10", "mm9"| 
| xLinkID | string | specify an ID for [linking multiple views](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#linking-views)|
| centerRadius | number | specify the proportion of the radius of the center white space. A number between [0,1], default=0.3|


## Multiple Views
Goslings supports multi-view visualizations. How multiple views are arranged is controlled by the `arrangement` property.
```javascript
{
  "arrangement": "parallel",
  "views": [
    // one view is composed of tracks that share the same layout property (linear or circular)
    {
      "layout": "linear",
      "tracks": [...]
    },
    // One view can have a hierarchical structure. 
    // For example, the view below is composed of two sub-views
    {
      "arrangement": "serial",
      "views": [
        {
          "tracks": [...]
        },
        {
          "tracks": [...]
        }
      ]
    }
  ]
}
```

Gosling supports four types of arrangemet: "parallel", "serial", "vertical", "horizontal".
<img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/multi_views.png" alt="arrangement of multiple views" width="700"/> </td>