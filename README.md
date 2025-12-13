# Ultimate Free APIs Collection

This is a curated, community-inspired collection of **free public APIs** compiled from various awesome lists (e.g., awesome-security-apis and public-apis). I've deduplicated entries, prioritized free or freemium options (noting commercial tiers where relevant), and organized them into clear categories. Each table includes key details: **API Name** (with link), **Description**, **Auth** (e.g., `apiKey`, `OAuth`, or `No`), **HTTPS**, and **CORS** support (where available).

Focus is on APIs that are **free to use** (with rate limits or basic tiers) and relevant for developers, security pros, and hobbyists. Commercial-only APIs are excluded unless they have a free tier. For full docs, visit the linked sites.

## Index

- [Security](#security)
- [Animals](#animals)
- [Anime](#anime)
- [Anti-Malware](#anti-malware)
- [Art & Design](#art--design)
- [Books](#books)
- [Business](#business)
- [Calendar](#calendar)
- [Cloud Storage & File Sharing](#cloud-storage--file-sharing)
- [Continuous Integration](#continuous-integration)
- [Cryptocurrency](#cryptocurrency)
- [Currency Exchange](#currency-exchange)
- [Data Validation](#data-validation)
- [Development](#development)
- [Shopping](#shopping)
- [Social](#social)
- [Sports & Fitness](#sports--fitness)
- [Test Data](#test-data)
- [Text Analysis](#text-analysis)
- [Transportation](#transportation)
- [URL Shorteners](#url-shorteners)
- [Vehicle](#vehicle)
- [Video](#video)

---

## Security

Free APIs for threat intel, malware analysis, vulnerability scanning, and more. Subsections for clarity.

### Online Threat Intel & Scanning

| API                                                                     | Description                                              | Auth     | HTTPS | CORS    | Free Tier       |
| ----------------------------------------------------------------------- | -------------------------------------------------------- | -------- | ----- | ------- | --------------- |
| [ANY.RUN](https://any.run/api-documentation/)                           | Interactive malware analysis service                     | `apiKey` | Yes   | Unknown | Freemium        |
| [BinaryEdge.io](https://binaryedge.io/)                                 | Search engine for internet-connected devices & honeypots | `apiKey` | Yes   | Unknown | Free/Commercial |
| [Censys.io](https://censys.io/api)                                      | Free threat intel for researchers                        | `apiKey` | Yes   | Unknown | Free            |
| [CIRCL CVE Search](https://cve.circl.lu/api/)                           | CVE search                                               | `none`   | Yes   | Unknown | Free            |
| [CIRCL Hashlookup](https://hashlookup.circl.lu/)                        | File hash lookup                                         | `none`   | Yes   | Unknown | Free            |
| [DShield](https://www.dshield.org/api/)                                 | Internet Storm Center API                                | `apiKey` | Yes   | Unknown | Free            |
| [EmailRep](https://blog.sublimesecurity.com/emailrep-query-and-report)  | Email reputation & malicious sender reporting            | `none`   | Yes   | Unknown | Free            |
| [GreyNoise](https://github.com/GreyNoise-Intelligence/api.greynoise.io) | Analyzes internet-wide scanners                          | `apiKey` | Yes   | Unknown | Free/Commercial |
| [Hybrid Analysis](https://www.hybrid-analysis.com/docs/api/v2)          | Online sandbox                                           | `none`   | Yes   | Unknown | Free            |
| [IPinfo](https://ipinfo.io)                                             | IP location, ASN, VPN detection                          | `none`   | Yes   | Unknown | Free            |
| [MalwareBazaar](https://bazaar.abuse.ch/api/)                           | Malware sharing service                                  | `apiKey` | Yes   | Unknown | Free            |
| [Onyphe](https://www.onyphe.io/)                                        | Search engine for connected devices                      | `apiKey` | Yes   | Unknown | Free/Commercial |
| [Pulsedive](https://pulsedive.com/api/)                                 | Threat intel from 50+ OSINT feeds                        | `apiKey` | Yes   | Unknown | Free            |
| [Shodan.io](https://developer.shodan.io/)                               | Search engine for connected devices                      | `apiKey` | Yes   | Unknown | Free/Commercial |
| [URLhaus](https://urlhaus-api.abuse.ch/)                                | Abuse.ch API for malicious URLs                          | `apiKey` | Yes   | Unknown | Free            |
| [urlscan.io](https://urlscan.io/about-api/)                             | URL scanning tool                                        | `apiKey` | Yes   | Unknown | Free            |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/)   | File/URL analysis                                        | `apiKey` | Yes   | Unknown | Free            |

### Tools & Platforms

| API                                                                                        | Description                         | Auth     | HTTPS | CORS    | Free Tier         |
| ------------------------------------------------------------------------------------------ | ----------------------------------- | -------- | ----- | ------- | ----------------- |
| [MISP](https://www.circl.lu/doc/misp/automation/)                                          | Open source threat intel platform   | `apiKey` | Yes   | Unknown | Free (OpenSource) |
| [TheHive](https://blog.thehive-project.org/tag/api/)                                       | Security incident response platform | `apiKey` | Yes   | Unknown | Free              |
| [Viper.li](https://github.com/viper-framework/viper/blob/master/docs/source/usage/web.rst) | Malware repository                  | `apiKey` | Yes   | Unknown | Free (OpenSource) |

### SIEM & Monitoring

| API                                                                                    | Description                      | Auth   | HTTPS | CORS    | Free Tier         |
| -------------------------------------------------------------------------------------- | -------------------------------- | ------ | ----- | ------- | ----------------- |
| [ELK Stack](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs.html) | ELK Stack API for logging/search | `none` | No    | Unknown | Free (OpenSource) |
| [Splunk](http://dev.splunk.com/restapi)                                                | Splunk API for SIEM              | `none` | No    | Unknown | Freemium          |

### Various Security

| API                                                                  | Description              | Auth     | HTTPS | CORS    | Free Tier |
| -------------------------------------------------------------------- | ------------------------ | -------- | ----- | ------- | --------- |
| [AlienVault OTX](https://otx.alienvault.com/api/)                    | IP/domain/URL reputation | `apiKey` | Yes   | Unknown | Free      |
| [Google Safe Browsing](https://developers.google.com/safe-browsing/) | Link/domain flagging     | `apiKey` | Yes   | Unknown | Free      |
| [Have I Been Pwned](https://haveibeenpwned.com/API/v3)               | Data breach checks       | `apiKey` | Yes   | Unknown | Free      |

**[⬆ Back to Index](#index)**

## Animals

| API                                                        | Description                               | Auth    | HTTPS | CORS    |
| ---------------------------------------------------------- | ----------------------------------------- | ------- | ----- | ------- |
| [Cat Facts](https://alexwohlbruck.github.io/cat-facts/)    | Daily cat facts                           | No      | Yes   | No      |
| [Dogs](https://dog.ceo/dog-api/)                           | Random dog images (Stanford Dogs Dataset) | No      | Yes   | Yes     |
| [HTTPCat](https://http.cat/)                               | Cat image for every HTTP status           | No      | Yes   | Unknown |
| [Petfinder](https://www.petfinder.com/developers/v2/docs/) | Pet adoption data                         | `OAuth` | Yes   | Yes     |
| [RandomDog](https://random.dog/woof.json)                  | Random dog pictures                       | No      | Yes   | Yes     |
| [RandomFox](https://randomfox.ca/floof/)                   | Random fox pictures                       | No      | Yes   | No      |
| [Shibe.Online](http://shibe.online/)                       | Random Shiba Inu, cats, or birds          | No      | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Anime

| API                                                                       | Description                        | Auth    | HTTPS | CORS    |
| ------------------------------------------------------------------------- | ---------------------------------- | ------- | ----- | ------- |
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs)                  | Anime discovery & tracking         | `OAuth` | Yes   | Unknown |
| [AnimeNewsNetwork](https://www.animenewsnetwork.com/encyclopedia/api.php) | Anime industry news                | No      | Yes   | Yes     |
| [Jikan](https://jikan.moe)                                                | Unofficial MyAnimeList API         | No      | Yes   | Yes     |
| [Kitsu](http://docs.kitsu.apiary.io/)                                     | Anime discovery platform           | `OAuth` | Yes   | Unknown |
| [Studio Ghibli](https://ghibliapi.herokuapp.com)                          | Resources from Studio Ghibli films | No      | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Anti-Malware

| API                                                                   | Description              | Auth     | HTTPS | CORS    |
| --------------------------------------------------------------------- | ------------------------ | -------- | ----- | ------- |
| [AbuseIPDB](https://docs.abuseipdb.com/)                              | IP/domain/URL reputation | `apiKey` | Yes   | Unknown |
| [Google Safe Browsing](https://developers.google.com/safe-browsing/)  | Link/domain flagging     | `apiKey` | Yes   | Unknown |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/) | File/URL analysis        | `apiKey` | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Art & Design

| API                                                                  | Description          | Auth     | HTTPS | CORS    |
| -------------------------------------------------------------------- | -------------------- | -------- | ----- | ------- |
| [Behance](https://www.behance.net/dev)                               | Design projects      | `apiKey` | Yes   | Unknown |
| [Dribbble](http://developer.dribbble.com/v2/)                        | Design inspiration   | `OAuth`  | No    | Unknown |
| [Harvard Art Museums](https://github.com/harvardartmuseums/api-docs) | Art collection       | `apiKey` | No    | Unknown |
| [Iconfinder](https://developer.iconfinder.com)                       | Icons search         | `apiKey` | Yes   | Unknown |
| [Rijksmuseum](https://www.rijksmuseum.nl/en/api)                     | Dutch art collection | `apiKey` | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Books

| API                                                    | Description           | Auth    | HTTPS | CORS    |
| ------------------------------------------------------ | --------------------- | ------- | ----- | ------- |
| [Google Books](https://developers.google.com/books/)   | Book search & details | `OAuth` | Yes   | Unknown |
| [Open Library](https://openlibrary.org/developers/api) | Books & covers        | No      | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Business

| API                                                          | Description        | Auth     | HTTPS | CORS    |
| ------------------------------------------------------------ | ------------------ | -------- | ----- | ------- |
| [Clearbit Logo](https://clearbit.com/docs#logo-api)          | Company logos      | `apiKey` | Yes   | Unknown |
| [Domainsdb.info](https://domainsdb.info/)                    | Domain name search | No       | Yes   | Unknown |
| [Gmail](https://developers.google.com/gmail/api/)            | Email access       | `OAuth`  | Yes   | Unknown |
| [Google Analytics](https://developers.google.com/analytics/) | Analytics data     | `OAuth`  | Yes   | Unknown |
| [Trello](https://developers.trello.com/)                     | Project boards     | `OAuth`  | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Calendar

| API                                                                    | Description                     | Auth     | HTTPS | CORS    |
| ---------------------------------------------------------------------- | ------------------------------- | -------- | ----- | ------- |
| [Calendar Index](https://www.calendarindex.com/)                       | Holidays & working days         | `apiKey` | Yes   | Yes     |
| [Google Calendar](https://developers.google.com/google-apps/calendar/) | Events management               | `OAuth`  | Yes   | Unknown |
| [Holidays](https://holidayapi.com/)                                    | Historical holidays             | `apiKey` | Yes   | Unknown |
| [Nager.Date](https://date.nager.at)                                    | Public holidays (90+ countries) | No       | Yes   | No      |
| [Namedays Calendar](https://api.abalin.net/)                           | Namedays for multiple countries | No       | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Cloud Storage & File Sharing

| API                                                  | Description     | Auth     | HTTPS | CORS    |
| ---------------------------------------------------- | --------------- | -------- | ----- | ------- |
| [Box](https://developer.box.com/)                    | File sharing    | `OAuth`  | Yes   | Unknown |
| [Dropbox](https://www.dropbox.com/developers)        | File storage    | `OAuth`  | Yes   | Unknown |
| [Google Drive](https://developers.google.com/drive/) | File management | `OAuth`  | Yes   | Unknown |
| [Pastebin](https://pastebin.com/api/)                | Text storage    | `apiKey` | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Continuous Integration

| API                                                     | Description            | Auth     | HTTPS | CORS    |
| ------------------------------------------------------- | ---------------------- | -------- | ----- | ------- |
| [CircleCI](https://circleci.com/docs/api/v1-reference/) | CI/CD automation       | `apiKey` | Yes   | Unknown |
| [Travis CI](https://docs.travis-ci.com/api/)            | GitHub project testing | `apiKey` | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Cryptocurrency

| API                                                 | Description           | Auth     | HTTPS | CORS    |
| --------------------------------------------------- | --------------------- | -------- | ----- | ------- |
| [CoinGecko](http://www.coingecko.com/api)           | Prices, market data   | No       | Yes   | Yes     |
| [CoinMarketCap](https://coinmarketcap.com/api/)     | Cryptocurrency prices | `apiKey` | Yes   | Unknown |
| [Coinpaprika](https://api.coinpaprika.com)          | Prices, volume        | No       | Yes   | Yes     |
| [CryptoCompare](https://www.cryptocompare.com/api#) | Comparisons           | No       | Yes   | Unknown |
| [Gemini](https://docs.gemini.com/rest-api/)         | Exchange data         | No       | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Currency Exchange

| API                                                  | Description         | Auth     | HTTPS | CORS    |
| ---------------------------------------------------- | ------------------- | -------- | ----- | ------- |
| [ExchangeRate-API](https://www.exchangerate-api.com) | Currency conversion | No       | Yes   | Yes     |
| [Exchangeratesapi.io](https://exchangeratesapi.io)   | Rates & conversion  | No       | Yes   | Yes     |
| [Fixer.io](http://fixer.io)                          | Exchange rates      | `apiKey` | Yes   | Unknown |
| [Frankfurter](https://www.frankfurter.app/docs)      | Rates & time series | No       | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Data Validation

| API                                                            | Description                  | Auth     | HTTPS | CORS    |
| -------------------------------------------------------------- | ---------------------------- | -------- | ----- | ------- |
| [Cloudmersive Validate](https://cloudmersive.com/validate-api) | Email, phone, VAT validation | `apiKey` | Yes   | Yes     |
| [Lob.com](https://lob.com/)                                    | US address verification      | `apiKey` | Yes   | Unknown |
| [NumValidate](https://numvalidate.com)                         | Phone validation             | No       | Yes   | Unknown |
| [vatlayer](https://vatlayer.com)                               | VAT number validation        | No       | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Development

| API                                        | Description              | Auth     | HTTPS | CORS    |
| ------------------------------------------ | ------------------------ | -------- | ----- | ------- |
| [Agify.io](https://agify.io)               | Age estimation from name | No       | Yes   | Yes     |
| [APIs.guru](https://apis.guru/api-doc/)    | OpenAPI specs directory  | No       | Yes   | Unknown |
| [GitHub](https://developer.github.com/v3/) | Repos & user data        | `OAuth`  | Yes   | Yes     |
| [IPify](https://www.ipify.org/)            | Simple IP lookup         | No       | Yes   | Unknown |
| [JSONbin.io](https://jsonbin.io)           | JSON storage             | `apiKey` | Yes   | Yes     |
| [Nationalize.io](https://nationalize.io)   | Nationality from name    | No       | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Shopping

| API                                                                              | Description                           | Auth     | HTTPS | CORS    |
| -------------------------------------------------------------------------------- | ------------------------------------- | -------- | ----- | ------- |
| [Best Buy](https://bestbuyapis.github.io/api-documentation/#overview)            | Products, categories, recommendations | `apiKey` | Yes   | Unknown |
| [eBay](https://developer.ebay.com/)                                              | Buy/sell on eBay                      | `OAuth`  | Yes   | Unknown |
| [Etsy](https://www.etsy.com/developers/documentation/getting_started/api_basics) | Shop & listing management             | `OAuth`  | Yes   | Unknown |
| [Octopart](https://octopart.com/api/v4/reference)                                | Electronics parts data                | `apiKey` | Yes   | Unknown |
| [WooCommerce](https://woocommerce.github.io/woocommerce-rest-api-docs/)          | WordPress e-commerce                  | `apiKey` | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Social

| API                                                                             | Description             | Auth    | HTTPS | CORS    |
| ------------------------------------------------------------------------------- | ----------------------- | ------- | ----- | ------- |
| [Discord](https://discord.com/developers/docs/intro)                            | Bot integration         | `OAuth` | Yes   | Unknown |
| [Facebook](https://developers.facebook.com/)                                    | Login, sharing, plugins | `OAuth` | Yes   | Unknown |
| [HackerNews](https://github.com/HackerNews/API)                                 | Social news             | No      | Yes   | Unknown |
| [Instagram](https://www.instagram.com/developer/)                               | Login & sharing         | `OAuth` | Yes   | Unknown |
| [LinkedIn](https://docs.microsoft.com/en-us/linkedin/?context=linkedin/context) | Professional networking | `OAuth` | Yes   | Unknown |
| [Reddit](https://www.reddit.com/dev/api)                                        | Community posts         | `OAuth` | Yes   | Unknown |
| [Slack](https://api.slack.com/)                                                 | Team messaging          | `OAuth` | Yes   | Unknown |
| [Twitter](https://developer.twitter.com/en/docs)                                | Tweets & data           | `OAuth` | Yes   | No      |

**[⬆ Back to Index](#index)**

## Sports & Fitness

| API                                                           | Description                 | Auth     | HTTPS | CORS    |
| ------------------------------------------------------------- | --------------------------- | -------- | ----- | ------- |
| [API-FOOTBALL](https://www.api-football.com/documentation-v3) | Leagues, cups, fixtures     | `apiKey` | Yes   | Yes     |
| [balldontlie](https://www.balldontlie.io)                     | NBA stats                   | No       | Yes   | Yes     |
| [Ergast F1](http://ergast.com/mrd/)                           | F1 data since 1950          | No       | Yes   | Unknown |
| [OpenLigaDB](https://www.openligadb.de)                       | Crowdsourced league results | No       | Yes   | Yes     |
| [Sportmonks Football](https://docs.sportmonks.com/football/)  | Scores, stats, fixtures     | `apiKey` | Yes   | Unknown |
| [Strava](https://strava.github.io/api/)                       | Athlete activities          | `OAuth`  | Yes   | Unknown |
| [TheSportsDB](https://www.thesportsdb.com/api.php)            | Crowdsourced sports data    | `apiKey` | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Test Data

| API                                                     | Description           | Auth     | HTTPS | CORS    |
| ------------------------------------------------------- | --------------------- | -------- | ----- | ------- |
| [Bacon Ipsum](https://baconipsum.com/json-api/)         | Lorem ipsum generator | No       | Yes   | Unknown |
| [FakeJSON](https://fakejson.com)                        | Fake data generation  | `apiKey` | Yes   | Yes     |
| [JSONPlaceholder](http://jsonplaceholder.typicode.com/) | Mock REST API         | No       | No    | Unknown |
| [RandomUser](https://randomuser.me)                     | Random user data      | No       | Yes   | Unknown |
| [RoboHash](https://robohash.org/)                       | Robot avatars         | No       | Yes   | Unknown |

**[⬆ Back to Index](#index)**

## Text Analysis

| API                                                                             | Description                | Auth     | HTTPS | CORS    |
| ------------------------------------------------------------------------------- | -------------------------- | -------- | ----- | ------- |
| [Detect Language](https://detectlanguage.com/)                                  | Language detection         | `apiKey` | Yes   | Unknown |
| [LanguageTool](https://languagetool.org/http-api/)                              | Grammar & style checker    | No       | Yes   | Unknown |
| [LibreTranslate](https://libretranslate.com/docs)                               | Translation (17 languages) | No       | Yes   | Unknown |
| [Sentiment Analysis](https://www.meaningcloud.com/developer/sentiment-analysis) | Multilingual sentiment     | `apiKey` | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Transportation

| API                                                              | Description               | Auth     | HTTPS | CORS    |
| ---------------------------------------------------------------- | ------------------------- | -------- | ----- | ------- |
| [Amadeus](https://developers.amadeus.com/self-service)           | Flight search             | `OAuth`  | Yes   | Unknown |
| [GraphHopper](https://docs.graphhopper.com/)                     | Routing directions        | `apiKey` | Yes   | Unknown |
| [Open Charge Map](https://openchargemap.org/site/develop/api)    | EV charging stations      | `apiKey` | Yes   | Yes     |
| [OpenSky Network](https://opensky-network.org/apidoc/index.html) | Real-time flight data     | No       | Yes   | Unknown |
| [Transport for London](https://api.tfl.gov.uk)                   | TfL transit data          | `apiKey` | Yes   | Unknown |
| [Uber](https://developer.uber.com/products)                      | Ride requests & estimates | `OAuth`  | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## URL Shorteners

| API                                                   | Description                | Auth     | HTTPS | CORS    |
| ----------------------------------------------------- | -------------------------- | -------- | ----- | ------- |
| [Bitly](http://dev.bitly.com/get_started.html)        | URL shortening & analytics | `OAuth`  | Yes   | Unknown |
| [CleanURI](https://cleanuri.com/docs)                 | Simple URL shortener       | No       | Yes   | Yes     |
| [Kutt](https://docs.kutt.it/)                         | Modern URL shortener       | `apiKey` | Yes   | Yes     |
| [Rebrandly](https://developers.rebrandly.com/v1/docs) | Branded link shortening    | `apiKey` | Yes   | Unknown |
| [TinyURL](https://tinyurl.com/app/dev)                | Basic shortening           | `apiKey` | Yes   | No      |

**[⬆ Back to Index](#index)**

## Vehicle

| API                                      | Description                             | Auth    | HTTPS | CORS    |
| ---------------------------------------- | --------------------------------------- | ------- | ----- | ------- |
| [NHTSA](https://vpic.nhtsa.dot.gov/api/) | Vehicle product info                    | No      | Yes   | Unknown |
| [Smartcar](https://smartcar.com/docs/)   | Vehicle control (lock/unlock, odometer) | `OAuth` | Yes   | Yes     |

**[⬆ Back to Index](#index)**

## Video

| API                                                      | Description                    | Auth     | HTTPS | CORS    |
| -------------------------------------------------------- | ------------------------------ | -------- | ----- | ------- |
| [Breaking Bad](https://breakingbadapi.com/documentation) | Breaking Bad data              | No       | Yes   | Unknown |
| [IMDb-API](https://imdb-api.com/)                        | Movies, TV, actors             | `apiKey` | Yes   | Unknown |
| [Open Movie Database](http://www.omdbapi.com/)           | Movie info                     | `apiKey` | Yes   | Unknown |
| [SWAPI](https://swapi.dev/)                              | Star Wars data                 | No       | Yes   | Yes     |
| [TMDb](https://www.themoviedb.org/documentation/api)     | Movies & TV (community-driven) | `apiKey` | Yes   | Unknown |
| [Trakt](https://trakt.docs.apiary.io/)                   | Movies & TV tracking           | `apiKey` | Yes   | Yes     |
| [YouTube](https://developers.google.com/youtube/)        | Video embedding & data         | `OAuth`  | Yes   | Unknown |

**[⬆ Back to Index](#index)**

This collection is continuously updatable—suggest additions via feedback! For more, check sources like [public-apis](https://github.com/public-apis/public-apis) or [awesome-security-apis](https://github.com/deralexxx/security-apis).
