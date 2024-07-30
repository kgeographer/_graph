## The Linked Places format (LPF)
*v1.3, 24 June 2024 changes*:

```
{
  "type": "FeatureCollection",
  "@context": "https://raw.githubusercontent.com/LinkedPasts/linked-places/master/linkedplaces-context-v1.1.jsonld",
  "features": [
    { "@id": "http://mygaz.org/places/p_12345",
      "type": "Feature",
      "properties":{
        "title": "Abingdon (UK)",
        "ccodes": ["GB"],
        "fclasses": ["P"]
      },
      "when": {
        "timespans": [{"start": {"in":"0676"},"end": {"in":"1066"}}],
        "periods": [
          { "name": "Anglo-Saxon Period, 449-1066",
            "@id": "periodo:p06c6g3whtg"},
          { "name": "Anglo-Saxon (culture or style)",
            "@id": "http://chronontology.dainst.org/period/O5r960WKERYr"}
        ],
        "label": "sample 'when' w/timespans, periods, duration",
        "duration": "P100Y",
        "certainty": "less-certain"
      },
      "names": [
        { "toponym":"Abingdon",
          "lang":"en",
          "citations": [
            {"label": "Ye Olde Gazetteer (1635)",
             "year": 1635,
             "@id":"http://archive.org/details/yeoldegazetteer"}],
          "when": { "timespans":[{"start":{"in":"1600"}}]}
        },
        { "toponym":"Abingdon-on-Thames", "lang":"en",
          "when": {
          	"timespans":[{"start":{"in":"1600"}}],
          	"certainty":"certain"
          }
        }
      ],
      "types": [
        { "identifier": "aat:300008375",
          "label": "town",
          "sourceLabels": [{"label":"Market Town","lang":"en"}],
          "when": {"timespans":[{"start":{"in":"1600"}}]} }
      ],
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
            { "type": "Point",
              "coordinates": [-1.2879,51.6708],
              "when": {"timespans":[
                {"start":{"in":"1600"},"end":{"in":"1699"}}]},
              "citations": [
                {"label": "Getty TGN (retrieved 4 May 2018)",
                 "@id":"tgn:7011944"}],
              "certainty": "certain"
            },
            { "type": "Point",
              "coordinates": [-1.31,51.64],
              "geowkt": "POLYGON ((-1.3077 51.6542, -1.2555 51.6542, -1.2555 51.6908, -1.3077 51.6908, -1.3077 51.6542))",
              "when": {"timespans":[{"start":{"in":"1700"}}]},
              "certainty": "uncertain"
            }
        ]
      },
      "links": [
        {"type": "exactMatch", "identifier": "http://vocab.getty.edu/tgn/7011944"},
        {"type": "exactMatch", "identifier": "http://www.geonames.org/2657780/"},
        {"type": "closeMatch", "identifier": "http://somegaz.org/places/39847"},
        {"type": "primaryTopicOf", "identifier": "https://en.wikipedia.org/wiki/Abingdon-on-Thames"},
        {"type": "subjectOf", "identifier": "http://www.visionofbritain.org.uk/travellers/Camden/11#pn_3"},
        {"type": "seeAlso", "identifier": "https://en.wikipedia.org/wiki/%C3%86bbe_of_Coldingham"}
      ],
      "relations": [
        { "relationType": "gvp:broaderPartitive",
          "relationTo": "http://mygaz.org/places/p_9876",
          "label": "part of Berkshire (UK)",
          "when": {"timespans":[
            {"start":{"in":"1600"},"end":{"in":"1974"}}
          ]}
        },
        { "relationType": "gvp:broaderPartitive",
          "relationTo": "http://mygaz.org/places/p_3456",
          "label": "part of Oxfordshire (UK)",
          "when": {"timespans":[{"start":{"in":"1974"}}]}
        },
        { "relationType": "gvp:tgn3000_related_to",
          "relationTo": "http://mygaz.org/places/p_98765",
          "label": "Linked to Semington by Kennet and Avon Canal",
          "when":{"timespans":[
            {"start":{"in":"1790"} }]},
          "citations": [
            {"label": "Harrumph (1923)",
             "year": 1923,
             "@id": "doi:10.1109/5.771073"}],
          "certainty": "certain"
        }
      ],
      "descriptions": [
        { "@id": "https://en.wikipedia.org/wiki/Abingdon-on-Thames",
          "value": "...a historic market town and civil parish...",
          "lang": "en"
        }
      ],
      "depictions": [
        { "@id": "https://commons.wikimedia.org/wiki/File:ThamesAtAbingdon.jpg",
          "title": "The River Thames at Abingdon, Oxfordshire",
          "license": "cc:by-sa/3.0/"
        }
      ]
    }
  ]
}

```

### Linked Places Feature elements

Feature elements are either ***required***, ***encouraged***, or ***optional***. The encouraged elements will facilitate reconciliation and/or provide richer search results and record displays in World-Historical Gazetteer.

#### **`@context`** (_required_)

In JSON-LD, labels for object elements are aliases for terms formally defined in linked ontologies. For Linked Places, those mappings are listed in [this context document](http://linkedpasts.org/assets/linkedplaces-context.jsonld).

e.g. `"@context": "http://linkedpasts.org/assets/linkedplaces-context-v1.jsonld"`

#### **`@id`** (_required_)

A unique and permanent URI pointing to the contributor's published record of the place. All place records contributed to World-Historical Gazetteer will have a minimal landing page, so it can serve as publisher for smaller projects.

e.g. `"@id": "http://mygaz.org/places/p_12345"`

#### **`properties{}`** (_required_)

A **properties** element holding at least one key:value pair is required by GeoJSON. For Linked Places format, **title** is required and one or more **ccodes** are encouraged. Properties are typically displayed in popup windows upon clicking markers in web maps.

e.g. ```"properties":{ "title": "Abingdon (UK)", "ccodes": ["GB"], "fclasses": ["P"]}```

#### **`title`** (_required_)

A label for the record, usually a 'preferred name' from among the toponyms associated with a place. The **title** is necessary for ordering records in some list displays. Note that for Pelagios and World-Historical Gazetteer interfaces, place records always include *all* available attested name variants and spellings.

#### **`fclasses[]`** (_required_)

A set (list) of one or more single-letter codes, classifying the place type, or class:

**A: Administrative entities** (e.g. countries, provinces, municipalities); 
**H: Water bodies** (e.g. rivers, lakes, bays, seas); 
**L: Regions, landscape areas** (cultural, geographic, historical); 
**P: Populated places** (e.g. cities, towns, hamlets); 
**R: Roads, routes, rail**; 
**S: Sites** (e.g. archaeological sites, buildings, complexes); 
**T: Terrestrial landforms** (e.g. mountains, valleys, capes)

#### **`ccodes[]`** (_encouraged_)

A set (list) of one or more two-letter codes ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)) indicating modern countries whose bounds contains or overlap the place. Invaluable for reconciliation against modern place name authority resources like Getty TGN, Wikidata, and GeoNames.

#### **`when{}`** (_required_)

A **when** element can be used to temporally scope a) an entire Feature; b) a **name**; c) a **geometry** (representative point or extent); d) a **type**; or e) a **relation**, i.e. an instance of a *part-of* relation with another place. Each Feature must include at least one **when** element, which can be in any of those locations.

A **when** element, where used, must include one or more **timespan**. One or more named **period**, referenced with a name and URI, is optional. Examples shown reference records from [PeriodO](http://perio.do/) and [Chronontology](http://chronontology.dainst.org/).

A **when** element, wherever used, can include an optional **certainty** attribute, allowed values for which are one of "certain", "less-certain", or "uncertain".

A **timespan** must have a start; if end is omitted, the timespan is interpreted as the interval described by the start. For example, ```{"start":{"in":"1832"}``` indicates "during 1832," and ```{"start":{"in":"1832-08-01"}``` indicates "on that day."

Valid values for "in," "earliest," and "latest" are ISO 8601 expressions as described by the [OWL-Time ontology](https://www.w3.org/TR/owl-time/).

Valid values for "duration" are strings wtih the letter 'P' followed by an integer, followed by one of Y, M, W, or D to indicate years, months, weeks, or days. E.g. **P100Y** indicates one century with unspecified bounds within an accompanying timespan.

The following annotated example indicates possible options:

```
"when": {
  "timespans": [
    { "start": { "in": "yyyy-mm" },
      "end": {
          "earliest": "-yyyy",
          "latest": "yyyy-mm-dd" }
    }
  ],
  "periods": [
    { "name": "Anglo-Saxon Period, 449-1066",
      "uri": "http://n2t.net/ark:/99152/p06c6g3whtg" }
  ],
  "label": "for a century during the Anglo-Saxon period",
  "certainty": "certain",
  "duration": "P100Y"
}

```

#### **`names[]`** (_required_)

A set (list) of one or more attested toponyms. At least one must have a citation. Temporal scoping with an associated 'when' element is optional, as are citations for all but the first. This allows for lists of uncited named variants. A Linked Places record _must_ have either a record-level "when" element, or a citation year for at least one of its names. It _can_ have both, as well as any number of "when" elements in names, geometries, types, and relations.

For example:

```
"names": [
  { "toponym":"Abingdon",
    "lang":"en",
    "citations": [{
      "label": "Hookland Travels (1635)",
      "year": 1635,
      "@id":"http://somearchive.org/hookland_travels"
    }],
    "when": {"timespans":[{"start":{"in":"1600"}}]}
  },
  { "toponym":"Abingdon-on-Thames", "lang":"en",
    "when": {"timespans":[{"start":{"in":"1600"}}]}
  }
],
```
#### **`types[ ]`** (_encouraged_*)
A set (list) of one or more place types, where `"identifier"` and `"label"` refer to a concept in a published vocabulary. This example indicates a term from the Getty Institute Art and Architecture Thesaurus (AAT). The `"sourceLabels"` attribute can be used for terms from the original source (or the contributor's internal vocabulary). [NOTE: World Historical Gazetteer has developed a subset list of 176 AAT place type concepts for use in that platform ([tsv](feature-types-AAT_20230609.tsv); [xlsx showing hierarchy](feature-types-AAT_20230609.xlsx).]

*`sourceLabels` and `when` are optional

```
"types": [
  { "identifier": "http://vocab.getty.edu/aat/300008375",
    "label": "town",
    "sourceLabels": [{"label":"Market Town","lang":"en"}],
    "when": {"timespans":[{"start":{"in":"1600"}}]}
  }
],

```

#### **`geometry{}`** (_required_)
One or more GeoJSON geometries. If only one, `type` can be any of `Point`, `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, `MultiPolygon` as shown. The `geowkt` [1], `when`, and `certainty` properties are optional.

```
"geometry": {
    "type": "Point",
    "coordinates": [-1.2879,51.6708],
    "geowkt": "POINT(-1.2879 51.6708)",
    "when": {"timespans":[
        {"start":{"earliest": "1600"},"end":{"in":"1699"}}
    ]},
    "certainty": "less-certain"
}
```

If a Feature has multiple geometries with distinct `when`, and/or `certainty` properties, its type should be `GeometryCollection` as shown below.

```
"geometry": {
  "type": "GeometryCollection",
  "geometries": [
      { "type": "Point",
        "coordinates": [-1.2879,51.6708],
        "geowkt": "POINT(-1.2879 51.6708)",
        "when": {"timespans":[
            {"start":{"earliest": "1600"},"end":{"in":"1699"}}
        ]},
        "certainty": "less-certain"
      },
      { "geowkt": "POLYGON ((-1.3077 51.6542, -1.2555 51.6542,
            -1.2555 51.6908, -1.3077 51.6908, -1.3077 51.6542))",
        "when": {"timespans":[{"start":"1700"}]},
        "certainty": "certain"
      }
  ]
}
```
NOTES

[1] A [Well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text)  representation of geometry ("geowkt") can be supplied in place of a "coordinates" element (e.g. geometry #2 below) , but in this case *the entire dataset will not validate as GeoJSON*. It will however index successfully in Pelagios and World Historical Gazetteer and render in the maps of those projects.

[2] Values for the optional `certainty` attribute can be one of "certain", "less-certain" and "uncertain".

[3] In the event the location for a place is unknown, the geometry element's value should be null. This is compatible with the Leaflet.js, MapBox.js, and MapLibre.js libraries e.g.

```"geometry": null```

#### **`links[]`** (_encouraged_)
Linked Places format supports four types of linked resources, as shown here. Close matches are the principal means of linking places and gazetteer datasets and are therefore at least one of these is ***highly encouraged***. The reconciliation service of World Historical Gazetteer can facilitate identifying closeMatch relations with place name authorities like Wikidata and the Getty Thesaurus of Geographic Names.

```
"links": [
  {"type": "closeMatch",
   "identifier": "https://www.wikidata.org/wiki/Q321381"},
  {"type": "primaryTopicOf",
   "identifier": "https://wikipedia.org/wiki/Abingdon-on-Thames"},
  {"type": "subjectOf",
   "identifier": "http://www.visionofbritain.org.uk/travellers/Camden/11#pn_3"},
  {"type": "seeAlso",
   "identifier": "https://en.wikipedia.org/wiki/%C3%86bbe_of_Coldingham"}
],

```
World Historical Gazetteer supports the name resources listed here; the aliases indicated (short URI prefixes) should be used in place of the URI base, e.g. `wd:Q321381` in the above example.

```

    {"bnf": Bibliothèque nationale de France, "https://data.bnf.fr/"}
    {"cerl": Consortium of European Research Libraries, "https://data.cerl.org/thesaurus/"}
    {"dbp": DBpedia, "http://dbpedia.org/resource/"}
    {"gn": GeoNames, "http://www.geonames.org/"}
    {"gnd": Deutschen Nationalbibliothek, "http://d-nb.info/gnd/"}
    {"gov": The Geneaological Gazetteer, "http://gov.genealogy.net/" }
    {"loc": Library of Congress, "http://id.loc.gov/authorities/subjects/"}
    {"pl": Pleiades, "https://pleiades.stoa.org/places/"}
    {"tgn": Getty Thesaurus of Geographic Names, "http://vocab.getty.edu/page/tgn/"}
    {"viaf": Virtual International Authority File, "http://viaf.org/viaf/"}
    {"wd": Wikidata, "https://www.wikidata.org/wiki/"}
    {"wp": Wikipedia, "https://wikipedia.org/wiki/"}

```

#### **`relations[]`** (_optional_)
A set (list) of one or more attestation of relation. The relationType property must be de-referenceable to an existing vocabulary or ontology. E.g., in the [Getty Vocabulary Ontology](http://vocab.getty.edu/ontology), **broaderPartitive** relations are used to represent 'parents' in an administrative hierarchy; **tgn3317\_member\_of** and **tgn3318\_member\_is** relations can be used to represent political unions, empires, and regions. In this example Abingdon is shown as having been an administrative part of two counties over time; also, using the generic **tgn3000\_related_to**, as having been linked by canal to Semington.

* Values for the optional `certainty` attribute can be one of "certain", "less-certain" and "uncertain".

```
"relations": [
  { "relationType": "gvp:broaderPartitive",
    "relationTo": "mygaz:places/p_9876",
    "label": "part of Berkshire (UK)",
    "when": {"timespans":[
      {"start":{"in":"1600"},"end":{"in":"1974"}}
    ]}
  },
  { "relationType": "gvp:broaderPartitive",
    "relationTo": "mygaz:places/p_3456",
    "label": "part of Oxfordshire (UK)",
    "when": {"timespans":[{"start":{"in":"1974"}}]}
  },
  { "relationType": "gvp:tgn3000_related_to",
    "relationTo": "http://mygaz.org/places/p_98765",
    "label": "Linked to Semington by Kennet and Avon Canal",
    "when":{"timespans":[{"start":{"in":"1790"}}]},
    "citations": [{
      "label": "Harrumph (1923)",
      "year": 1923,
      "@id": "doi:10.1109/5.771073"
    }],
    "certainty": "certain"
  }
]
```


#### **`descriptions[]`** (_encouraged_)
A set (list) of one or more brief descriptions.

e.g.

```
"descriptions": [
  {
    "value": "...a historic market town and civil parish in the ceremonial county of Oxfordshire, England",
    "lang": "en",
    "source": "https://en.wikipedia.org/wiki/Abingdon-on-Thames"
  }
]
```


#### **`depictions[]`** (_optional_)
A set (list) of one or more images of some part or aspect of the place.

```
"depictions": [
  {
    "@id": "https://commons.wikimedia.org/wiki/File:ThamesAtAbingdon.jpg",
    "title": "The River Thames at Abingdon, Oxfordshire",
    "license": "cc:by-sa/3.0/"
  }
]
```
