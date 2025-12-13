# Ultimate Free APIs Collection (2025 Edition)

[![Awesome](https://awesome.re)](https://github.com/sindresorhus/awesome) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-brightgreen.svg)](https://creativecommons.org/publicdomain/zero/1.0/) [![Stars](https://img.shields.io/github/stars/BRAIMcodes/awesome-free-apis)](https://github.com/BRAIMcodes/awesome-free-apis)

A **curated, deduplicated, and community-driven** collection of **free public APIs** for developers, security professionals, and hobbyists (beginners to pros). Aggregated and refined from 10+ sources like [public-apis](https://github.com/public-apis/public-apis), [mixed-analytics](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/), and your repo—now fully English, streamlined for easy navigation, and verified for 2025 relevance.

**Why this list?**

- **Free-first**: Only APIs with generous free tiers (no-auth preferred for beginners).
- **Pro tips**: Rate limits noted; security APIs prioritized for threat intel.
- **Navigation**: Use Ctrl+F (or Cmd+F) for quick search. Tables are mobile-friendly.
- **Contribute**: Fork, add PRs for new APIs (include Auth/HTTPS/CORS). See [CONTRIBUTING.md](CONTRIBUTING.md).

> **Beginner Hack**: Start with "No Auth" APIs—plug into Postman or curl instantly. **Pro Tip**: Check CORS for web apps; use proxies like CORS Anywhere for testing.

## Index

- [AI & Machine Learning](#ai--machine-learning)
- [Animals](#animals)
- [Anime](#anime)
- [Anti-Malware & Security](#anti-malware--security)
- [Art & Design](#art--design)
- [Books](#books)
- [Business & Productivity](#business--productivity)
- [Calendar & Holidays](#calendar--holidays)
- [Cloud Storage & File Sharing](#cloud-storage--file-sharing)
- [Cryptocurrency](#cryptocurrency)
- [Currency Exchange](#currency-exchange)
- [Data Validation](#data-validation)
- [Development & Testing](#development--testing)
- [Email & Messaging](#email--messaging)
- [Environment & Weather](#environment--weather)
- [Finance](#finance)
- [Food & Recipes](#food--recipes)
- [Games & Comics](#games--comics)
- [Geocoding & Maps](#geocoding--maps)
- [Government & Open Data](#government--open-data)
- [Health](#health)
- [Jobs](#jobs)
- [Logistics & Shipping](#logistics--shipping)
- [Movies & TV](#movies--tv)
- [Music](#music)
- [News](#news)
- [Personality & Quotes](#personality--quotes)
- [Photography](#photography)
- [Programming & Code](#programming--code)
- [Science & Math](#science--math)
- [Shopping](#shopping)
- [Social Media](#social-media)
- [Sports & Fitness](#sports--fitness)
- [Test Data & Mocking](#test-data--mocking)
- [Text Analysis & NLP](#text-analysis--nlp)
- [Transportation](#transportation)
- [URL Shorteners](#url-shorteners)
- [Vehicle](#vehicle)
- [Video](#video)

---

## AI & Machine Learning

Free tiers for NLP, generation, and more. Great for hobbyist chatbots or pro ML prototypes.

| API                                                            | Description                                          | Auth     | HTTPS | CORS    | Link                                              | Free Tier                     |
| -------------------------------------------------------------- | ---------------------------------------------------- | -------- | ----- | ------- | ------------------------------------------------- | ----------------------------- |
| [OpenAI](https://platform.openai.com/docs/api-reference)       | GPT models for text generation, chat, and embeddings | `apiKey` | Yes   | Unknown | [Docs](https://platform.openai.com/docs)          | Limited credits (~$5-18 free) |
| [Groq](https://console.groq.com/docs/overview)                 | Fast inference for Llama/Mistral models              | `apiKey` | Yes   | Yes     | [Docs](https://console.groq.com/docs)             | 1M tokens/day                 |
| [Hugging Face Inference](https://huggingface.co/inference-api) | Host/run ML models (e.g., sentiment, translation)    | `apiKey` | Yes   | Yes     | [Docs](https://huggingface.co/docs/api-inference) | 1K reqs/day                   |
| [Cohere](https://docs.cohere.com/reference/generate)           | Text generation, summarization, embeddings           | `apiKey` | Yes   | Unknown | [Docs](https://docs.cohere.com)                   | 1K calls/month                |
| [Replicate](https://replicate.com/docs)                        | Run open-source models (e.g., Stable Diffusion)      | `apiKey` | Yes   | Yes     | [Docs](https://replicate.com/docs)                | $10 credit                    |

**[⬆ Back to Index](#index)**

## Animals

Fun, no-auth APIs for pet projects or memes.

| API                                                        | Description              | Auth    | HTTPS | CORS | Link                                                  | Free Tier      |
| ---------------------------------------------------------- | ------------------------ | ------- | ----- | ---- | ----------------------------------------------------- | -------------- |
| [Cat Facts](https://alexwohlbruck.github.io/cat-facts/)    | Daily random cat facts   | No      | Yes   | No   | [Docs](https://alexwohlbruck.github.io/cat-facts/)    | Unlimited      |
| [Dogs](https://dog.ceo/dog-api/)                           | Random dog breeds/images | No      | Yes   | Yes  | [Docs](https://dog.ceo/dog-api/)                      | Unlimited      |
| [RandomFox](https://randomfox.ca/floof/)                   | Random fox images        | No      | Yes   | No   | [Docs](https://randomfox.ca/floof/)                   | Unlimited      |
| [Petfinder](https://www.petfinder.com/developers/v2/docs/) | Pet adoption listings    | `OAuth` | Yes   | Yes  | [Docs](https://www.petfinder.com/developers/v2/docs/) | 100 calls/hour |

**[⬆ Back to Index](#index)**

## Anime

Track and discover anime/manga.

| API                                                      | Description                | Auth    | HTTPS | CORS    | Link                                                  | Free Tier                 |
| -------------------------------------------------------- | -------------------------- | ------- | ----- | ------- | ----------------------------------------------------- | ------------------------- |
| [AniList](https://github.com/AniList/ApiV2-GraphQL-Docs) | Anime discovery & tracking | `OAuth` | Yes   | Unknown | [Docs](https://github.com/AniList/ApiV2-GraphQL-Docs) | Unlimited                 |
| [Jikan](https://jikan.moe)                               | Unofficial MyAnimeList API | No      | Yes   | Yes     | [Docs](https://jikan.moe)                             | Rate limited (60 req/min) |
| [Kitsu](http://docs.kitsu.apiary.io/)                    | Anime/manga database       | `OAuth` | Yes   | Unknown | [Docs](http://docs.kitsu.apiary.io/)                  | Unlimited                 |

**[⬆ Back to Index](#index)**

## Anti-Malware & Security

Threat intel, scans, and validation. Essential for pros; beginners: Start with VirusTotal.

| API                                                                   | Description            | Auth     | HTTPS | CORS    | Link                                                            | Free Tier        |
| --------------------------------------------------------------------- | ---------------------- | -------- | ----- | ------- | --------------------------------------------------------------- | ---------------- |
| [VirusTotal](https://www.virustotal.com/en/documentation/public-api/) | File/URL malware scans | `apiKey` | Yes   | Unknown | [Docs](https://www.virustotal.com/en/documentation/public-api/) | 500 req/day      |
| [AbuseIPDB](https://docs.abuseipdb.com/)                              | IP reputation checks   | `apiKey` | Yes   | Unknown | [Docs](https://docs.abuseipdb.com/)                             | 1K lookups/day   |
| [Have I Been Pwned](https://haveibeenpwned.com/API/v3)                | Breach checks          | `apiKey` | Yes   | Unknown | [Docs](https://haveibeenpwned.com/API/v3)                       | Rate limited     |
| [GreyNoise](https://docs.greynoise.io/reference/get_v3-community-ip)  | Scanner IP intel       | `apiKey` | Yes   | Unknown | [Docs](https://docs.greynoise.io)                               | Community free   |
| [URLScan](https://urlscan.io/about-api/)                              | URL scanning           | `apiKey` | Yes   | Unknown | [Docs](https://urlscan.io/about-api/)                           | Unlimited public |

**[⬆ Back to Index](#index)**

## Art & Design

Icons, images, and inspiration.

| API                                              | Description     | Auth     | HTTPS | CORS    | Link                                       | Free Tier   |
| ------------------------------------------------ | --------------- | -------- | ----- | ------- | ------------------------------------------ | ----------- |
| [Unsplash](https://unsplash.com/documentation)   | High-res photos | `apiKey` | Yes   | Yes     | [Docs](https://unsplash.com/documentation) | 50 req/hour |
| [Iconfinder](https://developer.iconfinder.com)   | Icon search     | `apiKey` | Yes   | Unknown | [Docs](https://developer.iconfinder.com)   | 100 req/day |
| [Rijksmuseum](https://www.rijksmuseum.nl/en/api) | Art collection  | `apiKey` | Yes   | Unknown | [Docs](https://www.rijksmuseum.nl/en/api)  | Unlimited   |

**[⬆ Back to Index](#index)**

## Books

Search and metadata.

| API                                                    | Description            | Auth    | HTTPS | CORS    | Link                                           | Free Tier  |
| ------------------------------------------------------ | ---------------------- | ------- | ----- | ------- | ---------------------------------------------- | ---------- |
| [Google Books](https://developers.google.com/books/)   | Book search/details    | `OAuth` | Yes   | Unknown | [Docs](https://developers.google.com/books/)   | 1K req/day |
| [Open Library](https://openlibrary.org/developers/api) | Books & covers         | No      | Yes   | Unknown | [Docs](https://openlibrary.org/developers/api) | Unlimited  |
| [Bhagavad Gita](https://bhagavadgita.io/api)           | Gita text in languages | `OAuth` | Yes   | Yes     | [Docs](https://bhagavadgita.io/api)            | Unlimited  |

**[⬆ Back to Index](#index)**

## Business & Productivity

Analytics, tasks, and tools.

| API                                                          | Description        | Auth     | HTTPS | CORS    | Link                                             | Free Tier     |
| ------------------------------------------------------------ | ------------------ | -------- | ----- | ------- | ------------------------------------------------ | ------------- |
| [Trello](https://developers.trello.com/)                     | Boards & tasks     | `OAuth`  | Yes   | Unknown | [Docs](https://developers.trello.com/)           | Unlimited     |
| [Google Analytics](https://developers.google.com/analytics/) | Usage data         | `OAuth`  | Yes   | Unknown | [Docs](https://developers.google.com/analytics/) | Unlimited     |
| [Monday.com](https://api.developer.monday.com/docs)          | Project management | `apiKey` | Yes   | Unknown | [Docs](https://api.developer.monday.com/docs)    | 2K items free |

**[⬆ Back to Index](#index)**

## Calendar & Holidays

Events and dates.

| API                                                                    | Description                     | Auth     | HTTPS | CORS    | Link                                                        | Free Tier      |
| ---------------------------------------------------------------------- | ------------------------------- | -------- | ----- | ------- | ----------------------------------------------------------- | -------------- |
| [Nager.Date](https://date.nager.at)                                    | Public holidays (90+ countries) | No       | Yes   | No      | [Docs](https://date.nager.at)                               | Unlimited      |
| [Google Calendar](https://developers.google.com/google-apps/calendar/) | Events CRUD                     | `OAuth`  | Yes   | Unknown | [Docs](https://developers.google.com/google-apps/calendar/) | Unlimited      |
| [Holidays](https://holidayapi.com/)                                    | Historical/global holidays      | `apiKey` | Yes   | Unknown | [Docs](https://holidayapi.com/)                             | 1K calls/month |

**[⬆ Back to Index](#index)**

## Cloud Storage & File Sharing

Upload/retrieve files.

| API                                                  | Description         | Auth    | HTTPS | CORS    | Link                                         | Free Tier          |
| ---------------------------------------------------- | ------------------- | ------- | ----- | ------- | -------------------------------------------- | ------------------ |
| [Pantry](https://getpantry.cloud/)                   | Simple JSON storage | No      | Yes   | Yes     | [Docs](https://getpantry.cloud/)             | Unlimited (public) |
| [BayFiles](https://bayfiles.com/docs/api)            | File upload/sharing | No      | Yes   | Unknown | [Docs](https://bayfiles.com/docs/api)        | 1GB free           |
| [Google Drive](https://developers.google.com/drive/) | File management     | `OAuth` | Yes   | Unknown | [Docs](https://developers.google.com/drive/) | 15GB free          |

**[⬆ Back to Index](#index)**

## Cryptocurrency

Prices, markets, and exchanges.

| API                                                 | Description                         | Auth     | HTTPS | CORS    | Link                                       | Free Tier         |
| --------------------------------------------------- | ----------------------------------- | -------- | ----- | ------- | ------------------------------------------ | ----------------- |
| [CoinGecko](https://www.coingecko.com/en/api)       | Prices, market data (no key needed) | No       | Yes   | Yes     | [Docs](https://www.coingecko.com/en/api)   | Unlimited         |
| [CoinMarketCap](https://coinmarketcap.com/api/)     | Crypto rankings/prices              | `apiKey` | Yes   | Unknown | [Docs](https://coinmarketcap.com/api/)     | 10K credits/month |
| [Nomics](https://nomics.com/docs/)                  | Real-time/historical data           | `apiKey` | Yes   | Yes     | [Docs](https://nomics.com/docs/)           | 1K calls/day      |
| [CryptoCompare](https://www.cryptocompare.com/api#) | Comparisons & news                  | No       | Yes   | Unknown | [Docs](https://www.cryptocompare.com/api#) | Unlimited         |

**[⬆ Back to Index](#index)**

## Currency Exchange

Rates and conversions.

| API                                                  | Description           | Auth     | HTTPS | CORS    | Link                                     | Free Tier      |
| ---------------------------------------------------- | --------------------- | -------- | ----- | ------- | ---------------------------------------- | -------------- |
| [ExchangeRate-API](https://www.exchangerate-api.com) | Live/historical rates | No       | Yes   | Yes     | [Docs](https://www.exchangerate-api.com) | 1.5K req/month |
| [Fixer.io](https://fixer.io)                         | Forex rates           | `apiKey` | Yes   | Unknown | [Docs](https://fixer.io)                 | 100 req/month  |
| [Frankfurter](https://www.frankfurter.app/docs)      | ECB rates & series    | No       | Yes   | Yes     | [Docs](https://www.frankfurter.app/docs) | Unlimited      |

**[⬆ Back to Index](#index)**

## Data Validation

Emails, phones, addresses.

| API                                    | Description             | Auth     | HTTPS | CORS    | Link                            | Free Tier        |
| -------------------------------------- | ----------------------- | -------- | ----- | ------- | ------------------------------- | ---------------- |
| [NumValidate](https://numvalidate.com) | Phone validation        | No       | Yes   | Unknown | [Docs](https://numvalidate.com) | Unlimited        |
| [vatlayer](https://vatlayer.com)       | VAT number checks       | No       | Yes   | Unknown | [Docs](https://vatlayer.com)    | 100 calls/month  |
| [Lob.com](https://lob.com/)            | US address verification | `apiKey` | Yes   | Unknown | [Docs](https://lob.com/)        | 250 verifs/month |

**[⬆ Back to Index](#index)**

## Development & Testing

Tools, mocks, and utils.

| API                                                     | Description             | Auth             | HTTPS | CORS         | Link                                         | Free Tier   |
| ------------------------------------------------------- | ----------------------- | ---------------- | ----- | ------------ | -------------------------------------------- | ----------- |
| [JSONPlaceholder](http://jsonplaceholder.typicode.com/) | Fake REST data          | No               | No    | Unknown      | [Docs](http://jsonplaceholder.typicode.com/) | Unlimited   |
| [GitHub REST](https://docs.github.com/en/rest)          | Repos, users, workflows | `OAuth`/`apiKey` | Yes   | Yes (public) | [Docs](https://docs.github.com/en/rest)      | 5K req/hour |
| [ReqRes](https://reqres.in/)                            | Mock users/delays       | No               | Yes   | Yes          | [Docs](https://reqres.in/)                   | Unlimited   |
| [Mocky](https://designer.mocky.io/)                     | Custom mock responses   | No               | Yes   | Yes          | [Docs](https://designer.mocky.io/)           | Unlimited   |

**[⬆ Back to Index](#index)**

## Email & Messaging

Send/receive, validation.

| API                                               | Description         | Auth     | HTTPS | CORS    | Link                                        | Free Tier       |
| ------------------------------------------------- | ------------------- | -------- | ----- | ------- | ------------------------------------------- | --------------- |
| [Mailgun](https://www.mailgun.com/)               | Transactional email | `apiKey` | Yes   | Unknown | [Docs](https://www.mailgun.com/)            | 5K emails/month |
| [EVA](https://eva.pingutil.com/)                  | Email validation    | No       | Yes   | Yes     | [Docs](https://eva.pingutil.com/)           | Unlimited       |
| [Twilio SMS](https://www.twilio.com/docs/sms/api) | Global SMS          | `apiKey` | Yes   | Unknown | [Docs](https://www.twilio.com/docs/sms/api) | $15 credit      |

**[⬆ Back to Index](#index)**

## Environment & Weather

Climate, forecasts.

| API                                          | Description          | Auth     | HTTPS | CORS    | Link                                   | Free Tier       |
| -------------------------------------------- | -------------------- | -------- | ----- | ------- | -------------------------------------- | --------------- |
| [Open-Meteo](https://open-meteo.com/en/docs) | Global forecasts     | No       | Yes   | Yes     | [Docs](https://open-meteo.com/en/docs) | Unlimited       |
| [Weatherstack](https://weatherstack.com/)    | Real-time/historical | `apiKey` | Yes   | Unknown | [Docs](https://weatherstack.com/)      | 250 calls/month |
| [CO2 Offset](https://co2offset.io/api.html)  | Carbon calculations  | No       | Yes   | Unknown | [Docs](https://co2offset.io/api.html)  | Unlimited       |

**[⬆ Back to Index](#index)**

## Finance

Stocks, banking, crypto.

| API                                                                                            | Description        | Auth     | HTTPS | CORS    | Link                                                    | Free Tier          |
| ---------------------------------------------------------------------------------------------- | ------------------ | -------- | ----- | ------- | ------------------------------------------------------- | ------------------ |
| [Alpaca](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/) | Stock trading data | `apiKey` | Yes   | Yes     | [Docs](https://alpaca.markets/docs)                     | Paper trading free |
| [Marketstack](https://marketstack.com/)                                                        | End-of-day prices  | `apiKey` | Yes   | Unknown | [Docs](https://marketstack.com/)                        | 100 req/month      |
| [SEC EDGAR](https://www.sec.gov/edgar/sec-api-documentation)                                   | US filings         | No       | Yes   | Yes     | [Docs](https://www.sec.gov/edgar/sec-api-documentation) | Unlimited          |

**[⬆ Back to Index](#index)**

## Food & Recipes

Ingredients, nutrition.

| API                                                      | Description             | Auth     | HTTPS | CORS    | Link                                                   | Free Tier       |
| -------------------------------------------------------- | ----------------------- | -------- | ----- | ------- | ------------------------------------------------------ | --------------- |
| [Fruityvice](https://www.fruityvice.com)                 | Fruit nutrition data    | No       | Yes   | Unknown | [Docs](https://www.fruityvice.com)                     | Unlimited       |
| [Edamam](https://developer.edamam.com/edamam-recipe-api) | Recipe search/nutrition | `apiKey` | Yes   | Unknown | [Docs](https://developer.edamam.com/edamam-recipe-api) | 10K calls/month |
| [Open Food Facts](https://en.wiki.openfoodfacts.org/API) | Product database        | No       | Yes   | Unknown | [Docs](https://en.wiki.openfoodfacts.org/API)          | Unlimited       |

**[⬆ Back to Index](#index)**

## Games & Comics

Scores, lore, assets.

| API                                                | Description       | Auth     | HTTPS | CORS    | Link                                        | Free Tier    |
| -------------------------------------------------- | ----------------- | -------- | ----- | ------- | ------------------------------------------- | ------------ |
| [IGDB](https://www.igdb.com/api)                   | Game database     | `apiKey` | Yes   | Unknown | [Docs](https://www.igdb.com/api)            | 1K calls/day |
| [TheSportsDB](https://www.thesportsdb.com/api.php) | Sports events/art | `apiKey` | Yes   | Yes     | [Docs](https://www.thesportsdb.com/api.php) | Unlimited    |
| [Animal Crossing](http://acnhapi.com/)             | Item/critter data | No       | Yes   | Unknown | [Docs](http://acnhapi.com/)                 | Unlimited    |

**[⬆ Back to Index](#index)**

## Geocoding & Maps

Locations, routing.

| API                                                                                       | Description               | Auth     | HTTPS | CORS    | Link                                                            | Free Tier       |
| ----------------------------------------------------------------------------------------- | ------------------------- | -------- | ----- | ------- | --------------------------------------------------------------- | --------------- |
| [BigDataCloud Reverse Geocoding](https://www.bigdatacloud.com/packages/reverse-geocoding) | Address from coords       | `apiKey` | Yes   | Yes     | [Docs](https://www.bigdatacloud.com/packages/reverse-geocoding) | 10K calls/month |
| [OpenStreetMap Nominatim](https://nominatim.org/release-docs/develop/api/Search/)         | Search/ geocode           | No       | Yes   | Unknown | [Docs](https://nominatim.org/release-docs/develop/api/Search/)  | Rate limited    |
| [Positionstack](https://positionstack.com/)                                               | Forward/reverse geocoding | `apiKey` | Yes   | Unknown | [Docs](https://positionstack.com/)                              | 25K calls/month |

**[⬆ Back to Index](#index)**

## Government & Open Data

Public records, stats.

| API                                      | Description        | Auth     | HTTPS | CORS    | Link                                  | Free Tier |
| ---------------------------------------- | ------------------ | -------- | ----- | ------- | ------------------------------------- | --------- |
| [USA.gov](https://www.usa.gov/developer) | US gov data        | `apiKey` | Yes   | Unknown | [Docs](https://www.usa.gov/developer) | Unlimited |
| [Congress.gov](https://api.congress.gov) | US legislation     | No       | Yes   | Unknown | [Docs](https://api.congress.gov)      | Unlimited |
| [API Setu](https://www.apisetu.gov.in/)  | India gov services | No       | Yes   | Yes     | [Docs](https://www.apisetu.gov.in/)   | Unlimited |

**[⬆ Back to Index](#index)**

## Health

Symptoms, trackers (use ethically).

| API                                                                | Description      | Auth     | HTTPS | CORS    | Link                                                        | Free Tier       |
| ------------------------------------------------------------------ | ---------------- | -------- | ----- | ------- | ----------------------------------------------------------- | --------------- |
| [ApiMedic](https://apimedic.com/)                                  | Symptom checker  | `apiKey` | Yes   | Unknown | [Docs](https://apimedic.com/)                               | 100 calls/day   |
| [Infermedica](https://developer.infermedica.com/docs/introduction) | Triage/diagnosis | `apiKey` | Yes   | Unknown | [Docs](https://developer.infermedica.com/docs/introduction) | 1K checks/month |

**[⬆ Back to Index](#index)**

## Jobs

Listings and career data.

| API                                            | Description      | Auth | HTTPS | CORS | Link                                   | Free Tier |
| ---------------------------------------------- | ---------------- | ---- | ----- | ---- | -------------------------------------- | --------- |
| [GraphQL Jobs](https://graphql.jobs/docs/api/) | Job board search | No   | Yes   | Yes  | [Docs](https://graphql.jobs/docs/api/) | Unlimited |

**[⬆ Back to Index](#index)**

## Logistics & Shipping

Tracking, rates (global focus; China-specific noted).

| API                                                | Description            | Auth     | HTTPS | CORS    | Link                                       | Free Tier          |
| -------------------------------------------------- | ---------------------- | -------- | ----- | ------- | ------------------------------------------ | ------------------ |
| [AfterShip](https://www.aftership.com/docs)        | Multi-carrier tracking | `apiKey` | Yes   | Unknown | [Docs](https://www.aftership.com/docs)     | 50 shipments/month |
| [Ship24](https://www.ship24.com/zh/couriers)       | Global parcel tracking | No       | Yes   | Unknown | [Docs](https://www.ship24.com/zh/couriers) | Unlimited public   |
| [快递 100 (China)](https://api.kuaidi100.com/home) | China express tracking | `apiKey` | Yes   | Unknown | [Docs](https://api.kuaidi100.com/home)     | 1K queries/day     |

**[⬆ Back to Index](#index)**

## Movies & TV

Metadata, quotes.

| API                                                  | Description      | Auth     | HTTPS | CORS    | Link                                                 | Free Tier  |
| ---------------------------------------------------- | ---------------- | -------- | ----- | ------- | ---------------------------------------------------- | ---------- |
| [TMDb](https://www.themoviedb.org/documentation/api) | Movies/TV search | `apiKey` | Yes   | Unknown | [Docs](https://www.themoviedb.org/documentation/api) | Unlimited  |
| [OMDb](https://www.omdbapi.com/)                     | Movie details    | `apiKey` | Yes   | Unknown | [Docs](https://www.omdbapi.com/)                     | 1K req/day |
| [IMDb-API](https://imdb-api.com/)                    | Titles, ratings  | `apiKey` | Yes   | Unknown | [Docs](https://imdb-api.com/)                        | 1K req/day |

**[⬆ Back to Index](#index)**

## Music

Tracks, lyrics, metadata.

| API                                                                | Description       | Auth     | HTTPS | CORS    | Link                                                        | Free Tier |
| ------------------------------------------------------------------ | ----------------- | -------- | ----- | ------- | ----------------------------------------------------------- | --------- |
| [Spotify Web](https://developer.spotify.com/documentation/web-api) | Playlists, search | `OAuth`  | Yes   | Unknown | [Docs](https://developer.spotify.com/documentation/web-api) | Unlimited |
| [Lyrics.ovh](https://lyricsovh.docs.apiary.io)                     | Song lyrics       | No       | Yes   | Unknown | [Docs](https://lyricsovh.docs.apiary.io)                    | Unlimited |
| [TheAudioDB](http://www.theaudiodb.com)                            | Artist/album art  | `apiKey` | Yes   | Unknown | [Docs](http://www.theaudiodb.com)                           | Unlimited |

**[⬆ Back to Index](#index)**

## News

Headlines, articles.

| API                                                | Description        | Auth     | HTTPS | CORS    | Link                                         | Free Tier       |
| -------------------------------------------------- | ------------------ | -------- | ----- | ------- | -------------------------------------------- | --------------- |
| [Mediastack](https://mediastack.com/documentation) | Global news        | `apiKey` | Yes   | Unknown | [Docs](https://mediastack.com/documentation) | 500 calls/month |
| [NewsCatcher](https://newscatcherapi.com/news-api) | Search/filter news | `apiKey` | Yes   | Unknown | [Docs](https://newscatcherapi.com/news-api)  | 50 articles/day |

**[⬆ Back to Index](#index)**

## Personality & Quotes

Fun, motivational.

| API                                                          | Description       | Auth | HTTPS | CORS    | Link                                                 | Free Tier |
| ------------------------------------------------------------ | ----------------- | ---- | ----- | ------- | ---------------------------------------------------- | --------- |
| [Bored](https://www.boredapi.com/)                           | Random activities | No   | Yes   | Unknown | [Docs](https://www.boredapi.com/)                    | Unlimited |
| [They Said So](http://quotes.rest/qod.json?category=inspire) | Daily quotes      | No   | Yes   | Unknown | [Docs](http://quotes.rest/qod.json?category=inspire) | Unlimited |
| [Forismatic](http://api.forismatic.com/api/1.0/)             | Random quotes     | No   | Yes   | Unknown | [Docs](http://api.forismatic.com/api/1.0/)           | Unlimited |

**[⬆ Back to Index](#index)**

## Photography

Images, edits.

| API                                                | Description              | Auth     | HTTPS | CORS    | Link                                              | Free Tier        |
| -------------------------------------------------- | ------------------------ | -------- | ----- | ------- | ------------------------------------------------- | ---------------- |
| [Duply](https://duply.co/docs#getting-started-api) | Photo duplication check  | `apiKey` | Yes   | Yes     | [Docs](https://duply.co/docs#getting-started-api) | 100 checks/month |
| [Pixabay](https://pixabay.com/api/docs/)           | Free stock photos/videos | `apiKey` | Yes   | Unknown | [Docs](https://pixabay.com/api/docs/)             | 5K req/day       |

**[⬆ Back to Index](#index)**

## Programming & Code

Challenges, langs.

| API                                                | Description                 | Auth     | HTTPS | CORS    | Link                                           | Free Tier |
| -------------------------------------------------- | --------------------------- | -------- | ----- | ------- | ---------------------------------------------- | --------- |
| [KONTESTS](https://kontests.net/api)               | Coding contest schedules    | No       | Yes   | Unknown | [Docs](https://kontests.net/api)               | Unlimited |
| [Codewars](https://dev.codewars.com/#introduction) | Kata solutions/leaderboards | `apiKey` | Yes   | Unknown | [Docs](https://dev.codewars.com/#introduction) | Unlimited |

**[⬆ Back to Index](#index)**

## Science & Math

Data, calculations.

| API                                                   | Description        | Auth     | HTTPS | CORS    | Link                                           | Free Tier      |
| ----------------------------------------------------- | ------------------ | -------- | ----- | ------- | ---------------------------------------------- | -------------- |
| [arXiv](https://arxiv.org/help/api/user-manual)       | Research papers    | No       | Yes   | Unknown | [Docs](https://arxiv.org/help/api/user-manual) | Unlimited      |
| [NASA](https://api.nasa.gov/index.html)               | Space imagery/data | `apiKey` | Yes   | Unknown | [Docs](https://api.nasa.gov/index.html)        | 1K req/hour    |
| [WolframAlpha](http://products.wolframalpha.com/api/) | Computations       | `apiKey` | Yes   | Unknown | [Docs](http://products.wolframalpha.com/api/)  | 2K calls/month |

**[⬆ Back to Index](#index)**

## Shopping

Products, e-commerce.

| API                                                                   | Description       | Auth     | HTTPS | CORS    | Link                                                              | Free Tier      |
| --------------------------------------------------------------------- | ----------------- | -------- | ----- | ------- | ----------------------------------------------------------------- | -------------- |
| [Octopart](https://octopart.com/api/v4/reference)                     | Electronics parts | `apiKey` | Yes   | Unknown | [Docs](https://octopart.com/api/v4/reference)                     | 1K calls/month |
| [Best Buy](https://bestbuyapis.github.io/api-documentation/#overview) | Products/reviews  | `apiKey` | Yes   | Unknown | [Docs](https://bestbuyapis.github.io/api-documentation/#overview) | Unlimited      |

**[⬆ Back to Index](#index)**

## Social Media

Posts, profiles.

| API                                                | Description      | Auth    | HTTPS | CORS    | Link                                          | Free Tier        |
| -------------------------------------------------- | ---------------- | ------- | ----- | ------- | --------------------------------------------- | ---------------- |
| [Twitter/X](https://developer.twitter.com/en/docs) | Tweets, trends   | `OAuth` | Yes   | No      | [Docs](https://developer.twitter.com/en/docs) | 1.5K posts/month |
| [Reddit](https://www.reddit.com/dev/api)           | Subreddits/posts | `OAuth` | Yes   | Unknown | [Docs](https://www.reddit.com/dev/api)        | Rate limited     |
| [aztro](https://aztro.sameerkumar.website/)        | Daily horoscopes | No      | Yes   | Unknown | [Docs](https://aztro.sameerkumar.website/)    | Unlimited        |

**[⬆ Back to Index](#index)**

## Sports & Fitness

Scores, stats.

| API                                                          | Description      | Auth     | HTTPS | CORS    | Link                                          | Free Tier       |
| ------------------------------------------------------------ | ---------------- | -------- | ----- | ------- | --------------------------------------------- | --------------- |
| [balldontlie](https://www.balldontlie.io)                    | NBA stats        | No       | Yes   | Yes     | [Docs](https://www.balldontlie.io)            | Unlimited       |
| [Sportmonks Football](https://docs.sportmonks.com/football/) | Soccer fixtures  | `apiKey` | Yes   | Unknown | [Docs](https://docs.sportmonks.com/football/) | 180 calls/month |
| [ApiMedic](https://apimedic.com/)                            | Fitness symptoms | `apiKey` | Yes   | Unknown | [Docs](https://apimedic.com/)                 | 100 calls/day   |

**[⬆ Back to Index](#index)**

## Test Data & Mocking

Fakes for prototyping.

| API                                                              | Description         | Auth | HTTPS | CORS    | Link                                             | Free Tier |
| ---------------------------------------------------------------- | ------------------- | ---- | ----- | ------- | ------------------------------------------------ | --------- |
| [RandomUser](https://randomuser.me)                              | Fake users/profiles | No   | Yes   | Unknown | [Docs](https://randomuser.me)                    | Unlimited |
| [Mockyard](https://mockyard.in/)                                 | Realistic mocks     | No   | Yes   | Yes     | [Docs](https://mockyard.in/)                     | Unlimited |
| [English Random Words](https://random-words-api.vercel.app/word) | Word generation     | No   | Yes   | No      | [Docs](https://random-words-api.vercel.app/word) | Unlimited |

**[⬆ Back to Index](#index)**

## Text Analysis & NLP

Sentiment, translation.

| API                                                                             | Description            | Auth     | HTTPS | CORS    | Link                                                              | Free Tier       |
| ------------------------------------------------------------------------------- | ---------------------- | -------- | ----- | ------- | ----------------------------------------------------------------- | --------------- |
| [Detect Language](https://detectlanguage.com/)                                  | Lang ID                | `apiKey` | Yes   | Unknown | [Docs](https://detectlanguage.com/)                               | 100 calls/month |
| [LibreTranslate](https://libretranslate.com/docs)                               | Translation (17 langs) | No       | Yes   | Unknown | [Docs](https://libretranslate.com/docs)                           | Self-host free  |
| [Sentiment Analysis](https://www.meaningcloud.com/developer/sentiment-analysis) | Multilingual sentiment | `apiKey` | Yes   | Yes     | [Docs](https://www.meaningcloud.com/developer/sentiment-analysis) | 20K words/month |

**[⬆ Back to Index](#index)**

## Transportation

Flights, routes.

| API                                                              | Description         | Auth     | HTTPS | CORS    | Link                                                  | Free Tier     |
| ---------------------------------------------------------------- | ------------------- | -------- | ----- | ------- | ----------------------------------------------------- | ------------- |
| [OpenSky Network](https://opensky-network.org/apidoc/index.html) | Flight tracking     | No       | Yes   | Unknown | [Docs](https://opensky-network.org/apidoc/index.html) | Unlimited     |
| [AviationStack](https://aviationstack.com/)                      | Airport/flight data | `apiKey` | Yes   | Unknown | [Docs](https://aviationstack.com/)                    | 100 req/month |
| [GraphHopper](https://docs.graphhopper.com/)                     | Routing/directions  | `apiKey` | Yes   | Unknown | [Docs](https://docs.graphhopper.com/)                 | 2.5K req/day  |

**[⬆ Back to Index](#index)**

## URL Shorteners

Link management.

| API                                     | Description        | Auth     | HTTPS | CORS | Link                                  | Free Tier      |
| --------------------------------------- | ------------------ | -------- | ----- | ---- | ------------------------------------- | -------------- |
| [Shrtcode](https://shrtco.de/docs)      | Custom short links | No       | Yes   | Yes  | [Docs](https://shrtco.de/docs)        | Unlimited      |
| [TinyURL](https://tinyurl.com/app/dev)  | Basic shortening   | `apiKey` | Yes   | No   | [Docs](https://tinyurl.com/app/dev)   | Unlimited      |
| [UrlBae](https://urlbae.com/developers) | Analytics included | `apiKey` | Yes   | Yes  | [Docs](https://urlbae.com/developers) | 1K links/month |

**[⬆ Back to Index](#index)**

## Vehicle

Cars, EVs.

| API                                                           | Description           | Auth     | HTTPS | CORS    | Link                                               | Free Tier |
| ------------------------------------------------------------- | --------------------- | -------- | ----- | ------- | -------------------------------------------------- | --------- |
| [NHTSA](https://vpic.nhtsa.dot.gov/api/)                      | Vehicle specs/recalls | No       | Yes   | Unknown | [Docs](https://vpic.nhtsa.dot.gov/api/)            | Unlimited |
| [Open Charge Map](https://openchargemap.org/site/develop/api) | EV stations           | `apiKey` | Yes   | Yes     | [Docs](https://openchargemap.org/site/develop/api) | Unlimited |

**[⬆ Back to Index](#index)**

## Video

Streaming, edits.

| API                                                        | Description             | Auth     | HTTPS | CORS    | Link                                              | Free Tier     |
| ---------------------------------------------------------- | ----------------------- | -------- | ----- | ------- | ------------------------------------------------- | ------------- |
| [YouTube Data](https://developers.google.com/youtube/)     | Videos, playlists       | `OAuth`  | Yes   | Unknown | [Docs](https://developers.google.com/youtube/)    | 10K units/day |
| [Mux](https://www.mux.com/)                                | Video encoding/playback | `apiKey` | Yes   | Unknown | [Docs](https://www.mux.com/)                      | 3K min/month  |
| [Bob's Burgers](https://bobs-burgers-api-ui.herokuapp.com) | Episode/quote data      | No       | Yes   | Yes     | [Docs](https://bobs-burgers-api-ui.herokuapp.com) | Unlimited     |

**[⬆ Back to Index](#index)**

---

**Sources**: Inspired by [public-apis](https://github.com/public-apis/public-apis), [mixed-analytics](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/), and community feedback (2025 updates). Star/fork to support! 🚀
