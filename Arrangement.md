A single visualization is called a 'track' in Gosling, and multiple tracks can be specified as an array in a `tracks` property.

```javascript
{
  "tracks":[
    {...}, // each object specifies a track 
    {...},
    ...
  ]
}
```

Using arrangement options supported in Gosling, you can juxtapose and superpose tracks in a flexible way.

# Grid-Based Arrangement
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L20)  

Using a `arrangement` property, you can specify a grid arrangement of multiple tracks. Each track listed in a `tracks` property will be positioned in a cell one by one. You can use a `span` property in a track definition to make the track being positioned across multiple cells in the grid. For example, `span: 2` make a track positioned across two cells.

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

# Superposition
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)


A `superpose` property enables you to overlay multiple tracks/marks on top of each other. `superpose` is an array of objects, and each object specifies one visual mark. Each visual mark inherits the properties (e.g., `data`, `x`, and `y`) defined in the corresponding track definition unless these properties are redefined in this object.  

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

<!-- TODO: add channel.flip, channel.grid and other properties  -->

