---
title: Getting Started
slug: /
---
We currently support the following ways of using Gosling.
- [Create Your Visualization in Gosling Online Editor](#create-your-visualization-in-gosling-online-editor)
- [Load a Gosling Spec From Your Github Gist](#load-a-gosling-spec-from-your-github-gist)
- [Embed Gosling Component in a HTML File](#embed-gosling-component-in-a-html-file)
- [Use Gosling.js in React App](#use-goslingjs-in-react-app)
- [Resources](#resources)

## Create Your Visualization in Gosling Online Editor
You can visit [Online Editor](https://gosling.js.org) to visualize your data directly in the website.

## Load a Gosling Spec From Your Github Gist
1. To load a spec you first have to create a gist with a file named gosling.js* that specifies the spec.
1. You can additionally specify a readme.md file to describe your spec.
1. Also be sure to give your gist a fabulous title. It'll be shown in the gosling editor.
You can then open your visualization at <a>http://<editor_url>/?gist=<github_username>/<gist_id></a>. 
For example, https://gosling.js.org/?gist=flekschas/e6e388332814886d4d714efd0e88093b

## Embed Gosling Component in a HTML File
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="lightgray" />
        <link rel="stylesheet" href="https://unpkg.com/higlass@1.11.3/dist/hglib.css">
    </head>

    <body>
        <div id="root"/>
        <script crossorigin type="text/javascript" src="https://unpkg.com/react@16/umd/react.development.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/pixi.js@5/dist/pixi.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/gosling.js@0.0.26/dist/gosling.js"></script>
    </body>
    <script>
      gosling.embed(
        document.getElementById('root'),
        {
          "tracks": [
            {
              "data": {
                "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
                "type": "multivec",
                "row": "sample",
                "column": "position",
                "value": "peak",
                "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
              }
            }
          ]
        }
      );
    </script>
</html>
```

## Use Gosling.js in React App

Install `gosling.js` and its dependent libraries:

```sh
yarn add gosling.js pixi.js react@16.13.1 react-dom@16.13.1
```

Add the following style sheets to your base `html` file:
```html
<head>
  ...
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://unpkg.com/higlass@1.11.3/dist/hglib.css">
</head>
```

Use the Gosling.js' react component to visualize your data:

```js
import { validateGoslingSpec, GoslingComponent } from "gosling.js";

...

// validate the spec
const validity = validateGoslingSpec(EXMAPLE_GOSLING_SPEC);

if(validity.state === 'error') {
    console.warn('Gosling spec is invalid!', validity.message);
    return;
}

...

function App() {
  
  ...

  return (
    <GoslingComponent
      spec={EXAMPLE_GOSLING_SPEC}
      compiled={(spec, vConf) => { /* Callback function when compiled */ }}
    />
  );
}
```

Please visit [gosling-react](https://github.com/gosling-lang/gosling-react) for more detailed instruction. Also, visit [gosling-api-example](https://github.com/gosling-lang/gosling-api-example) to learn more about Gosling.js APIs, such as quick navigation to particular genes with animated transition.

## Resources
- How to set up your own HiGlass server for private data exploration?
   - HiGlass Server: https://github.com/higlass/higlass-server
   - HiGlass Docker: https://github.com/higlass/higlass-docker
- How to prepare your own HiGlass data?
   - HiGlass docs for data preparation: https://docs.higlass.io/data_preparation.html
