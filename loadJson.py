import json

jsonText = '''
{
  "search-results": {
    "opensearch:totalResults": "999996",
    "opensearch:startIndex": "0",
    "opensearch:itemsPerPage": "25",
    "opensearch:Query": {
      "@role": "request",
      "@searchTerms": "chromatography",
      "@startPage": "0"
    },
    "link": [
      {
        "@_fa": "true",
        "@ref": "self",
        "@href": "https://api.elsevier.com/content/search/sciencedirect?start=0&count=25&query=chromatography&apiKey=69691fd2a98b018877fe90d4d922b315&insttoken=7b239acf049df2b930f8fe8fc331d0d2",
        "@type": "application/json"
      },
      {
        "@_fa": "true",
        "@ref": "first",
        "@href": "https://api.elsevier.com/content/search/sciencedirect?start=0&count=25&query=chromatography&apiKey=69691fd2a98b018877fe90d4d922b315&insttoken=7b239acf049df2b930f8fe8fc331d0d2",
        "@type": "application/json"
      },
      {
        "@_fa": "true",
        "@ref": "next",
        "@href": "https://api.elsevier.com/content/search/sciencedirect?start=25&count=25&query=chromatography&apiKey=69691fd2a98b018877fe90d4d922b315&insttoken=7b239acf049df2b930f8fe8fc331d0d2",
        "@type": "application/json"
      },
      {
        "@_fa": "true",
        "@ref": "last",
        "@href": "https://api.elsevier.com/content/search/sciencedirect?start=5975&count=25&query=chromatography&apiKey=69691fd2a98b018877fe90d4d922b315&insttoken=7b239acf049df2b930f8fe8fc331d0d2",
        "@type": "application/json"
      }
    ],
    "entry": [
      {
        "@_fa": "true",
        "load-date": "2023-08-23T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005472"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005472?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464322",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005472",
        "dc:title": "Retention correlation and orthogonality between reversed phase countercurrent chromatography and liquid chromatography based on solvent strength",
        "dc:creator": "Tingting Lin",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1707",
        "prism:coverDate": "2023-09-27",
        "prism:startingPage": "464322",
        "prism:doi": "10.1016/j.chroma.2023.464322",
        "openaccess": false,
        "pii": "S0021967323005472",
        "authors": {
          "author": [
            {
              "$": "Tingting Lin"
            },
            {
              "$": "Beibei Zhu"
            },
            {
              "$": "Shengqiang Tong"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-28T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0003267023010760"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0003267023010760?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.aca.2023.341855",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0003267023010760",
        "dc:title": "Two-dimensional chromatography for the analysis of valorisable biowaste: A review",
        "dc:creator": "Eliise Tammekivi",
        "prism:publicationName": "Analytica Chimica Acta",
        "prism:coverDate": "2023-09-28",
        "prism:startingPage": "341855",
        "prism:doi": "10.1016/j.aca.2023.341855",
        "openaccess": false,
        "pii": "S0003267023010760",
        "authors": {
          "author": [
            {
              "$": "Eliise Tammekivi"
            },
            {
              "$": "Christophe Geantet"
            },
            {
              "$": "Karine Faure"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-09T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005186"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005186?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464293",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005186",
        "dc:title": "Development of tandem cation exchange chromatography for high purity extracellular vesicle isolation: The effect of ligand steric availability",
        "dc:creator": "Heikki Saari",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1707",
        "prism:coverDate": "2023-09-27",
        "prism:startingPage": "464293",
        "prism:doi": "10.1016/j.chroma.2023.464293",
        "openaccess": true,
        "pii": "S0021967323005186",
        "authors": {
          "author": [
            {
              "$": "Heikki Saari"
            },
            {
              "$": "Reetta Pusa"
            },
            {
              "$": "Saara Laitinen"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-16T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S2772753X23002368"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S2772753X23002368?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.focha.2023.100415",
        "prism:url": "https://api.elsevier.com/content/article/pii/S2772753X23002368",
        "dc:title": "Ion chromatography and ion chromatography / mass spectrometry as a complementary analysis technique for amino acid analysis in food, a review",
        "dc:creator": "H. S. A. Yates",
        "prism:publicationName": "Food Chemistry Advances",
        "prism:volume": "3",
        "prism:coverDate": "2023-12-31",
        "prism:startingPage": "100415",
        "prism:doi": "10.1016/j.focha.2023.100415",
        "openaccess": true,
        "pii": "S2772753X23002368",
        "authors": {
          "author": [
            {
              "$": "H. S. A. Yates"
            },
            {
              "$": "J. F. Carter"
            },
            {
              "$": "M. T. Fletcher"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-18T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323006179"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323006179?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464392",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323006179",
        "dc:title": "Unified chromatography in drug development: Exploiting chaotropic/kosmotropic salts for an accelerated method development",
        "dc:creator": "Gioacchino Luca Losacco",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1709",
        "prism:coverDate": "2023-10-25",
        "prism:startingPage": "464392",
        "prism:doi": "10.1016/j.chroma.2023.464392",
        "openaccess": false,
        "pii": "S0021967323006179",
        "authors": {
          "author": [
            {
              "$": "Gioacchino Luca Losacco"
            },
            {
              "$": "Zachary S. Breitbach"
            },
            {
              "$": "Leon Van Haandel"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-10-03T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0959943623002729"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0959943623002729?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.mencom.2023.09.044",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0959943623002729",
        "dc:title": "Column chromatography separation of lanthanide(III) bisphthalocyaninate and phthalocyanine ligand",
        "dc:creator": "Anna A. Botnar",
        "prism:publicationName": "Mendeleev Communications",
        "prism:volume": "33",
        "prism:coverDate": "2023-10-31",
        "prism:startingPage": "729",
        "prism:endingPage": "731",
        "prism:doi": "10.1016/j.mencom.2023.09.044",
        "openaccess": false,
        "pii": "S0959943623002729",
        "authors": {
          "author": [
            {
              "$": "Anna A. Botnar"
            },
            {
              "$": "Tatyana V. Tikhomirova"
            },
            {
              "$": "Arthur S. Vashurin"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-17T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005307"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005307?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464305",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005307",
        "dc:title": "Biomimetic affinity chromatography for antibody purification: Host cell protein binding and impurity removal",
        "dc:creator": "Haotian Huang",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1707",
        "prism:coverDate": "2023-09-27",
        "prism:startingPage": "464305",
        "prism:doi": "10.1016/j.chroma.2023.464305",
        "openaccess": false,
        "pii": "S0021967323005307",
        "authors": {
          "author": [
            {
              "$": "Haotian Huang"
            },
            {
              "$": "Xiaoyan Dong"
            },
            {
              "$": "Qinghong Shi"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-07-22T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323004636"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323004636?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464238",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323004636",
        "dc:title": "Multi-dimensional preparation of <ce:italic>Thymus quinquecostatus</ce:italic> Celak. by normal-phase flash chromatography coupled to counter-current chromatography",
        "dc:creator": "Jinxing Guo",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1706",
        "prism:coverDate": "2023-09-13",
        "prism:startingPage": "464238",
        "prism:doi": "10.1016/j.chroma.2023.464238",
        "openaccess": false,
        "pii": "S0021967323004636",
        "authors": {
          "author": [
            {
              "$": "Jinxing Guo"
            },
            {
              "$": "Luqi Li"
            },
            {
              "$": "Zhi Yang"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-07-02T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S002196732300420X"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S002196732300420X?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464194",
        "prism:url": "https://api.elsevier.com/content/article/pii/S002196732300420X",
        "dc:title": "Continuous multi-membrane chromatography of large viral particles",
        "dc:creator": "Tiago Matos",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1705",
        "prism:coverDate": "2023-08-30",
        "prism:startingPage": "464194",
        "prism:doi": "10.1016/j.chroma.2023.464194",
        "openaccess": false,
        "pii": "S002196732300420X",
        "authors": {
          "author": [
            {
              "$": "Tiago Matos"
            },
            {
              "$": "David Hoying"
            },
            {
              "$": "Joseph Joyce"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-04-26T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S002196732300256X"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S002196732300256X?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464030",
        "prism:url": "https://api.elsevier.com/content/article/pii/S002196732300256X",
        "dc:title": "Optimization of fluid flow in membrane chromatography devices using computational fluid dynamic simulations",
        "dc:creator": "Roxana Roshankhah",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1699",
        "prism:coverDate": "2023-06-21",
        "prism:startingPage": "464030",
        "prism:doi": "10.1016/j.chroma.2023.464030",
        "openaccess": false,
        "pii": "S002196732300256X",
        "authors": {
          "author": [
            {
              "$": "Roxana Roshankhah"
            },
            {
              "$": "Robert Pelton"
            },
            {
              "$": "Raja Ghosh"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-20T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323006271"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323006271?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464402",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323006271",
        "dc:title": "Mechanistic study of ultrasound-assisted chromatography using plastic and stainless steel columns",
        "dc:creator": "Nguyen Van Kien",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1710",
        "prism:coverDate": "2023-11-08",
        "prism:startingPage": "464402",
        "prism:doi": "10.1016/j.chroma.2023.464402",
        "openaccess": false,
        "pii": "S0021967323006271",
        "authors": {
          "author": [
            {
              "$": "Nguyen Van Kien"
            },
            {
              "$": "Young Han Jeong"
            },
            {
              "$": "Jae Jeong Ryoo"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-25T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005587"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005587?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464333",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005587",
        "dc:title": "Applicability of supercritical fluid chromatography for oligonucleotide analysis: A proof-of-concept study",
        "dc:creator": "Momoka Hayashida",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1708",
        "prism:coverDate": "2023-10-11",
        "prism:startingPage": "464333",
        "prism:doi": "10.1016/j.chroma.2023.464333",
        "openaccess": true,
        "pii": "S0021967323005587",
        "authors": {
          "author": [
            {
              "$": "Momoka Hayashida"
            },
            {
              "$": "Risa Suzuki"
            },
            {
              "$": "Satoshi Obika"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-20T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S016599362300393X"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S016599362300393X?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.trac.2023.117306",
        "prism:url": "https://api.elsevier.com/content/article/pii/S016599362300393X",
        "dc:title": "Recent approaches to the liquid chromatography-mass spectrometry analysis of modified deoxynucleosides as biomarkers in clinical research",
        "dc:creator": "Rafał Różalski",
        "prism:publicationName": "TrAC Trends in Analytical Chemistry",
        "prism:volume": "168",
        "prism:coverDate": "2023-11-30",
        "prism:startingPage": "117306",
        "prism:doi": "10.1016/j.trac.2023.117306",
        "openaccess": false,
        "pii": "S016599362300393X",
        "authors": {
          "author": [
            {
              "$": "Rafał Różalski"
            },
            {
              "$": "Fabian Leśniewski"
            },
            {
              "$": "Daniel Gackowski"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-03T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0045206823004960"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0045206823004960?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.bioorg.2023.106835",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0045206823004960",
        "dc:title": "Two-dimensional chromatography for enantiomeric analysis of mitotane and its metabolite o,p′-DDA in patients with adrenocortical carcinoma indicates enantioselective metabolism",
        "dc:creator": "Gabriela Stadler",
        "prism:publicationName": "Bioorganic Chemistry",
        "prism:volume": "141",
        "prism:coverDate": "2023-12-31",
        "prism:startingPage": "106835",
        "prism:doi": "10.1016/j.bioorg.2023.106835",
        "openaccess": false,
        "pii": "S0045206823004960",
        "authors": {
          "author": [
            {
              "$": "Gabriela Stadler"
            },
            {
              "$": "Alan de Almeida Veiga"
            },
            {
              "$": "Lauro Mera de Souza"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-03-31T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S1359644623000922"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S1359644623000922?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.drudis.2023.103576",
        "prism:url": "https://api.elsevier.com/content/article/pii/S1359644623000922",
        "dc:title": "Advances in receptor chromatography for drug discovery and drug–receptor interaction studies",
        "dc:creator": "Jia Fu",
        "prism:publicationName": "Drug Discovery Today",
        "prism:volume": "28",
        "prism:coverDate": "2023-06-30",
        "prism:startingPage": "103576",
        "prism:doi": "10.1016/j.drudis.2023.103576",
        "openaccess": false,
        "pii": "S1359644623000922",
        "authors": {
          "author": [
            {
              "$": "Jia Fu"
            },
            {
              "$": "Wei Qin"
            },
            {
              "$": "Hui-Ling Cao"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-06-15T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0003267023007171"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0003267023007171?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.aca.2023.341496",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0003267023007171",
        "dc:title": "Recent development of chiral ionic liquids for enantioseparation in liquid chromatography and capillary electrophoresis: A review",
        "dc:creator": "Huifeng Liu",
        "prism:publicationName": "Analytica Chimica Acta",
        "prism:volume": "1274",
        "prism:coverDate": "2023-09-15",
        "prism:startingPage": "341496",
        "prism:doi": "10.1016/j.aca.2023.341496",
        "openaccess": false,
        "pii": "S0003267023007171",
        "authors": {
          "author": [
            {
              "$": "Huifeng Liu"
            },
            {
              "$": "Jia Chen"
            },
            {
              "$": "Hongdeng Qiu"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-06T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005885"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005885?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464363",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005885",
        "dc:title": "Predicting sample injection profiles in liquid chromatography: A modelling approach based on residence time distributions",
        "dc:creator": "Monica Tirapelle",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1708",
        "prism:coverDate": "2023-10-11",
        "prism:startingPage": "464363",
        "prism:doi": "10.1016/j.chroma.2023.464363",
        "openaccess": true,
        "pii": "S0021967323005885",
        "authors": {
          "author": [
            {
              "$": "Monica Tirapelle"
            },
            {
              "$": "Maximilian O. Besenhard"
            },
            {
              "$": "Eva Sorensen"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-06-02T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323003436"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323003436?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464117",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323003436",
        "dc:title": "Microfluidic paper and thread-based separations: Chromatography and electrophoresis",
        "dc:creator": "Bahram Hemmateenejad",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1704",
        "prism:coverDate": "2023-08-16",
        "prism:startingPage": "464117",
        "prism:doi": "10.1016/j.chroma.2023.464117",
        "openaccess": false,
        "pii": "S0021967323003436",
        "authors": {
          "author": [
            {
              "$": "Bahram Hemmateenejad"
            },
            {
              "$": "Elmira Rafatmah"
            },
            {
              "$": "Zahra Shojaeifard"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-05-18T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S1046592823000682"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S1046592823000682?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.pep.2023.106297",
        "prism:url": "https://api.elsevier.com/content/article/pii/S1046592823000682",
        "dc:title": "Resin and loading condition screening for effective and robust byproducts removal by anion exchange chromatography: A case study",
        "dc:creator": "Wei Chen",
        "prism:publicationName": "Protein Expression and Purification",
        "prism:volume": "210",
        "prism:coverDate": "2023-10-31",
        "prism:startingPage": "106297",
        "prism:doi": "10.1016/j.pep.2023.106297",
        "openaccess": false,
        "pii": "S1046592823000682",
        "authors": {
          "author": [
            {
              "$": "Wei Chen"
            },
            {
              "$": "Peter K. Wang"
            },
            {
              "$": "Yan Wan"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-12T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0969804323003330"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0969804323003330?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.apradiso.2023.110980",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0969804323003330",
        "dc:title": "Separation of cyclotron-produced cobalt-55/58m from iron targets using cation exchange chromatography with non-aqueous solvents and extraction chromatography",
        "dc:creator": "Wilson Lin",
        "prism:publicationName": "Applied Radiation and Isotopes",
        "prism:volume": "200",
        "prism:coverDate": "2023-10-31",
        "prism:startingPage": "110980",
        "prism:doi": "10.1016/j.apradiso.2023.110980",
        "openaccess": false,
        "pii": "S0969804323003330",
        "authors": {
          "author": [
            {
              "$": "Wilson Lin"
            },
            {
              "$": "Eduardo Aluicio-Sarduy"
            },
            {
              "$": "Jonathan W. Engle"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-09T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S002196732300571X"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S002196732300571X?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464346",
        "prism:url": "https://api.elsevier.com/content/article/pii/S002196732300571X",
        "dc:title": "Physics-informed neural networks to solve lumped kinetic model for chromatography process",
        "dc:creator": "Si-Yuan Tang",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1708",
        "prism:coverDate": "2023-10-11",
        "prism:startingPage": "464346",
        "prism:doi": "10.1016/j.chroma.2023.464346",
        "openaccess": false,
        "pii": "S002196732300571X",
        "authors": {
          "author": [
            {
              "$": "Si-Yuan Tang"
            },
            {
              "$": "Yun-Hao Yuan"
            },
            {
              "$": "Dong-Qiang Lin"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-08-16T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323005277"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323005277?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464302",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323005277",
        "dc:title": "Model-assisted process development, characterization and design of continuous chromatography for antibody separation",
        "dc:creator": "Yan-Na Sun",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1707",
        "prism:coverDate": "2023-09-27",
        "prism:startingPage": "464302",
        "prism:doi": "10.1016/j.chroma.2023.464302",
        "openaccess": false,
        "pii": "S0021967323005277",
        "authors": {
          "author": [
            {
              "$": "Yan-Na Sun"
            },
            {
              "$": "Wu-Wei Chen"
            },
            {
              "$": "Dong-Qiang Lin"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-12T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323006039"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323006039?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464378",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323006039",
        "dc:title": "An online preparative high-performance liquid chromatography system with enrichment and purification modes for the efficient and systematic separation of <ce:italic>Panax notoginseng</ce:italic> saponins",
        "dc:creator": "Shuai Li",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1709",
        "prism:coverDate": "2023-10-25",
        "prism:startingPage": "464378",
        "prism:doi": "10.1016/j.chroma.2023.464378",
        "openaccess": false,
        "pii": "S0021967323006039",
        "authors": {
          "author": [
            {
              "$": "Shuai Li"
            },
            {
              "$": "Han Zhang"
            },
            {
              "$": "Junjie Zhang"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-09-10T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323006015"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323006015?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464376",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323006015",
        "dc:title": "Use and abuse of retention indices in gas chromatography",
        "dc:creator": "Humberto R. Bizzo",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1708",
        "prism:coverDate": "2023-10-11",
        "prism:startingPage": "464376",
        "prism:doi": "10.1016/j.chroma.2023.464376",
        "openaccess": true,
        "pii": "S0021967323006015",
        "authors": {
          "author": [
            {
              "$": "Humberto R. Bizzo"
            },
            {
              "$": "Nathália S. Brilhante"
            },
            {
              "$": "Philip J. Marriott"
            }
          ]
        }
      },
      {
        "@_fa": "true",
        "load-date": "2023-05-18T00:00:00.000Z",
        "link": [
          {
            "@_fa": "true",
            "@ref": "self",
            "@href": "https://api.elsevier.com/content/article/pii/S0021967323003072"
          },
          {
            "@_fa": "true",
            "@ref": "scidir",
            "@href": "https://www.sciencedirect.com/science/article/pii/S0021967323003072?dgcid=api_sd_search-api-endpoint"
          }
        ],
        "dc:identifier": "DOI:10.1016/j.chroma.2023.464081",
        "prism:url": "https://api.elsevier.com/content/article/pii/S0021967323003072",
        "dc:title": "Behavior of host-cell-protein-rich aggregates in antibody capture and polishing chromatography",
        "dc:creator": "Chase E. Herman",
        "prism:publicationName": "Journal of Chromatography A",
        "prism:volume": "1702",
        "prism:coverDate": "2023-08-02",
        "prism:startingPage": "464081",
        "prism:doi": "10.1016/j.chroma.2023.464081",
        "openaccess": false,
        "pii": "S0021967323003072",
        "authors": {
          "author": [
            {
              "$": "Chase E. Herman"
            },
            {
              "$": "Lie Min"
            },
            {
              "$": "Abraham M. Lenhoff"
            }
          ]
        }
      }
    ]
  }
}
'''

jsonObject = json.loads(jsonText)
for eachEntry in jsonObject['search-results']['entry']:
    print(eachEntry['pii'])
