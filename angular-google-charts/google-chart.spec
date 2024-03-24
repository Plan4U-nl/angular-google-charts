{
    "name": "angular-google-charts-google-chart",
    "displayName": "Google Chart",
    "version": 1,
    "libraries": [],
    "model": {
        "type": {
            "type": "string",
            "doc": "The type of chart to draw",
            "values": [
                "AnnotationChart",
                "AreaChart",
                "Bar",
                "BarChart",
                "BubbleChart",
                "Calendar",
                "CandlestickChart",
                "ColumnChart",
                "ComboChart",
                "PieChart",
                "Gantt",
                "Gauge",
                "GeoChart",
                "Histogram",
                "Line",
                "LineChart",
                "Map",
                "OrgChart",
                "Sankey",
                "Scatter",
                "ScatterChart",
                "SteppedAreaChart",
                "Table",
                "Timeline",
                "TreeMap",
                "WordTree"
            ]
        },
        "data": {
            "type": "object",
            "doc": "Data used to initialize the table",
            "scope": "runtime"
        },
        "columns": {
            "type": "object[]",
            "doc": "The names of the columns in the table"
        },
        "title": {
            "type": "string",
            "doc": "The title of the chart",
            "optional": true
        },
        "width": {
            "type": "int",
            "doc": "The width of the chart",
            "optional": true
        },
        "height": {
            "type": "int",
            "doc": "The height of the chart",
            "optional": true
        },
        "dynamicResize": {
            "type": "boolean",
            "doc": "If set to true, the chart will resize itself when the window resizes",
            "default": false,
            "optional": true
        }
    }
}