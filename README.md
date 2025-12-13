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

| [Anime News Network](https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=4658) | Anime/manga encyclopedia | No | Yes | Unknown | [Docs](https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=4658) | Unlimited |
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

| [Art Institute of Chicago](https://api.artic.edu/api/v1/artworks/search?q=cats) | Artwork from the museum | No | Yes | Unknown | [Docs](https://api.artic.edu/api/v1/artworks/search?q=cats) | Unlimited |
| [COLOURlovers](https://www.colourlovers.com/api/colors/new?format=json) | Color trends | No | Yes | Unknown | [Docs](https://www.colourlovers.com/api/colors/new?format=json) | Unlimited |
| [DiceBear](https://api.dicebear.com/6.x/pixel-art/svg) | Generate random SVG avatars | No | Yes | Unknown | [Docs](https://api.dicebear.com/6.x/pixel-art/svg) | Unlimited |
| [Dogs](https://dog.ceo/api/breeds/image/random) | Random dog images | No | Yes | Unknown | [Docs](https://dog.ceo/api/breeds/image/random) | Unlimited |
| [HTTP Cats](https://http.cat/401) | Cat images for HTTP status codes | No | Yes | Unknown | [Docs](https://http.cat/401) | Unlimited |
| [Lorem Picsum](https://picsum.photos/200/300) | Placeholder images | No | Yes | Unknown | [Docs](https://picsum.photos/200/300) | Unlimited |
| [Metropolitan Museum of Art](https://collectionapi.metmuseum.org/public/collection/v1/objects/100) | Artwork from the museum | No | Yes | Unknown | [Docs](https://collectionapi.metmuseum.org/public/collection/v1/objects/100) | Unlimited |
| [PHP-Noise](https://php-noise.com/noise.php?hex=FFFFFF&json) | Noise background image generator | No | Yes | Unknown | [Docs](https://php-noise.com/noise.php?hex=FFFFFF&json) | Unlimited |
| [Placebear](https://placebear.com/200/300) | Pictures of bears for use as placeholders | No | Yes | Unknown | [Docs](https://placebear.com/200/300) | Unlimited |
| [Random Dog](https://random.dog/woof.json) | Random dog images | No | Yes | Unknown | [Docs](https://random.dog/woof.json) | Unlimited |
| [RandomFox](https://randomfox.ca/floof/) | Random pictures of foxes | No | Yes | Unknown | [Docs](https://randomfox.ca/floof/) | Unlimited |
| [ReSmush](http://api.resmush.it/ws.php?img=http://www.resmush.it/assets/images/jpg_example_original.jpg&qlty=95) | Image compression and optimization | No | No | Unknown | [Docs](http://api.resmush.it/ws.php?img=http://www.resmush.it/assets/images/jpg_example_original.jpg&qlty=95) | Unlimited |
| [RoboHash](https://robohash.org/onerobot.png) | Generate unique images from text | No | Yes | Unknown | [Docs](https://robohash.org/onerobot.png) | Unlimited |
| [Vadivelu Status Codes](https://vadivelu.anoram.com/gif/200) | HTTP Codes with images | No | Yes | Unknown | [Docs](https://vadivelu.anoram.com/gif/200) | Unlimited |
**[⬆ Back to Index](#index)**

## Books

Search and metadata.

| API                                                    | Description            | Auth    | HTTPS | CORS    | Link                                           | Free Tier  |
| ------------------------------------------------------ | ---------------------- | ------- | ----- | ------- | ---------------------------------------------- | ---------- |
| [Google Books](https://developers.google.com/books/)   | Book search/details    | `OAuth` | Yes   | Unknown | [Docs](https://developers.google.com/books/)   | 1K req/day |
| [Open Library](https://openlibrary.org/developers/api) | Books & covers         | No      | Yes   | Unknown | [Docs](https://openlibrary.org/developers/api) | Unlimited  |
| [Bhagavad Gita](https://bhagavadgita.io/api)           | Gita text in languages | `OAuth` | Yes   | Yes     | [Docs](https://bhagavadgita.io/api)            | Unlimited  |

| [4chan](https://a.4cdn.org/boards.json) | 4chan's read-only API | No | Yes | Unknown | [Docs](https://a.4cdn.org/boards.json) | Unlimited |
| [Ceska Televize](https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=30.01.2024&channel=ct24) | Czech television program data | No | Yes | Unknown | [Docs](https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=30.01.2024&channel=ct24) | Unlimited |
| [Chronicling America](https://chroniclingamerica.loc.gov/newspapers.json) | Historic US newspapers | No | Yes | Unknown | [Docs](https://chroniclingamerica.loc.gov/newspapers.json) | Unlimited |
| [Crossref](https://api.crossref.org/journals?query=pharmacy+health) | Scholarly metadata | No | Yes | Unknown | [Docs](https://api.crossref.org/journals?query=pharmacy+health) | Unlimited |
| [HackerNews](https://hacker-news.firebaseio.com/v0/item/8863.json) | Hacker News API | No | Yes | Unknown | [Docs](https://hacker-news.firebaseio.com/v0/item/8863.json) | Unlimited |
| [Ice and Fire](https://anapioficeandfire.com/api/characters/581) | Quantified and structured data from the universe of Ice and Fire | No | Yes | Unknown | [Docs](https://anapioficeandfire.com/api/characters/581) | Unlimited |
| [Listly](https://list.ly/api/v4/meta?url=http://google.com) | Top 10 lists | No | Yes | Unknown | [Docs](https://list.ly/api/v4/meta?url=http://google.com) | Unlimited |
| [MCU-Countdown](https://www.whenisthenextmcufilm.com/api) | When is the next MCU film? | No | Yes | Unknown | [Docs](https://www.whenisthenextmcufilm.com/api) | Unlimited |
| [Mediawiki](https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvprop=content&format=json) | Wikipedia page content and revisions | No | Yes | Unknown | [Docs](https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvprop=content&format=json) | Unlimited |
| [Reddit](https://www.reddit.com/r/Wallstreetbets/top.json?limit=10&t=year) | Public content from Reddit | No | Yes | Unknown | [Docs](https://www.reddit.com/r/Wallstreetbets/top.json?limit=10&t=year) | Unlimited |
| [Reddit Stocks](https://tradestie.com/api/v1/apps/reddit) | Top stocks from Wallstreetbets | No | Yes | Unknown | [Docs](https://tradestie.com/api/v1/apps/reddit) | Unlimited |
| [Wolne Lektury](https://wolnelektury.pl/api/authors/edgar-allan-poe/) | Search ebooks from wolnelektury.pl | No | Yes | Unknown | [Docs](https://wolnelektury.pl/api/authors/edgar-allan-poe/) | Unlimited |
| [WordPress](https://techcrunch.com/wp-json/wp/v2/posts?per_page=100&context=embed) | Posts from any public WordPress site | No | Yes | Unknown | [Docs](https://techcrunch.com/wp-json/wp/v2/posts?per_page=100&context=embed) | Unlimited |
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

| [UK Bank Holidays](https://www.gov.uk/bank-holidays.json) | UK bank holidays | No | Yes | Unknown | [Docs](https://www.gov.uk/bank-holidays.json) | Unlimited |
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

| [Binance](https://api4.binance.com/api/v3/ticker/24hr) | 24 hr crypto data | No | Yes | Unknown | [Docs](https://api4.binance.com/api/v3/ticker/24hr) | Unlimited |
| [CoinBase](https://api.coinbase.com/v2/currencies) | Currency codes and names | No | Yes | Unknown | [Docs](https://api.coinbase.com/v2/currencies) | Unlimited |
| [CoinCap](https://api.coincap.io/v2/assets) | Real time cryptocurrency prices | No | Yes | Unknown | [Docs](https://api.coincap.io/v2/assets) | Unlimited |
| [CoinDesk](https://api.coindesk.com/v1/bpi/currentprice.json) | Bitcoin price index | No | Yes | Unknown | [Docs](https://api.coindesk.com/v1/bpi/currentprice.json) | Unlimited |
| [CoinLore](https://api.coinlore.net/api/tickers/) | Cryptocurrency market data | No | Yes | Unknown | [Docs](https://api.coinlore.net/api/tickers/) | Unlimited |
| [CoinMap](https://coinmap.org/api/v1/venues/) | Crypto ATMs | No | Yes | Unknown | [Docs](https://coinmap.org/api/v1/venues/) | Unlimited |
| [Coinpaprika](https://api.coinpaprika.com/v1/coins/btc-bitcoin) | Cryptocurrency data | No | Yes | Unknown | [Docs](https://api.coinpaprika.com/v1/coins/btc-bitcoin) | Unlimited |
| [DEX Screener](https://api.dexscreener.com/latest/dex/search?q=WBNB%20USDC) | Blockchain screener | No | Yes | Unknown | [Docs](https://api.dexscreener.com/latest/dex/search?q=WBNB%20USDC) | Unlimited |
| [GeckoTerminal](https://api.geckoterminal.com/api/v2/networks) | Crypto data | No | Yes | Unknown | [Docs](https://api.geckoterminal.com/api/v2/networks) | Unlimited |
| [Gemini](https://api.gemini.com/v2/ticker/btcusd) | Cryptocurrency market data | No | Yes | Unknown | [Docs](https://api.gemini.com/v2/ticker/btcusd) | Unlimited |
| [Kraken](https://api.kraken.com/0/public/Trades?pair=ltcusd) | Crypto data | No | Yes | Unknown | [Docs](https://api.kraken.com/0/public/Trades?pair=ltcusd) | Unlimited |
| [KuCoin](https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT) | Crypto data | No | Yes | Unknown | [Docs](https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT) | Unlimited |
| [Nexchange](https://api.n.exchange/en/api/v1/pair/) | Cryptocurrency market data | No | Yes | Unknown | [Docs](https://api.n.exchange/en/api/v1/pair/) | Unlimited |
| [OKX](https://www.okx.com/api/v5/market/tickers?instType=SPOT) | Cryptocurrency market data | No | Yes | Unknown | [Docs](https://www.okx.com/api/v5/market/tickers?instType=SPOT) | Unlimited |
| [Razorpay IFSC](https://ifsc.razorpay.com/YESB0DNB002) | Indian Financial Systems Codes | No | Yes | Unknown | [Docs](https://ifsc.razorpay.com/YESB0DNB002) | Unlimited |
| [WazirX](https://api.wazirx.com/sapi/v1/tickers/24hr) | Crypto data | No | Yes | Unknown | [Docs](https://api.wazirx.com/sapi/v1/tickers/24hr) | Unlimited |
**[⬆ Back to Index](#index)**

## Currency Exchange

Rates and conversions.

| API                                                  | Description           | Auth     | HTTPS | CORS    | Link                                     | Free Tier      |
| ---------------------------------------------------- | --------------------- | -------- | ----- | ------- | ---------------------------------------- | -------------- |
| [ExchangeRate-API](https://www.exchangerate-api.com) | Live/historical rates | No       | Yes   | Yes     | [Docs](https://www.exchangerate-api.com) | 1.5K req/month |
| [Fixer.io](https://fixer.io)                         | Forex rates           | `apiKey` | Yes   | Unknown | [Docs](https://fixer.io)                 | 100 req/month  |
| [Frankfurter](https://www.frankfurter.app/docs)      | ECB rates & series    | No       | Yes   | Yes     | [Docs](https://www.frankfurter.app/docs) | Unlimited      |

| [Currency Rates](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json) | Currency exchange rates | No | Yes | Unknown | [Docs](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json) | Unlimited |
| [NBP Web](http://api.nbp.pl/api/cenyzlota/last/30/?format=json) | Currency exchange rates and gold prices | No | No | Unknown | [Docs](http://api.nbp.pl/api/cenyzlota/last/30/?format=json) | Unlimited |
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

| [Agify](https://api.agify.io?name=bella) | Predict age based on a name | No | Yes | Unknown | [Docs](https://api.agify.io?name=bella) | Unlimited |
| [APIC Agent](https://api.apicagent.com/?ua=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_5)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/89.0.4389.114%20Safari/537.36) | Detect browser, OS, and device from user agent | No | Yes | Unknown | [Docs](https://api.apicagent.com/?ua=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_5)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/89.0.4389.114%20Safari/537.36) | Unlimited |
| [Arul's Public APIs](https://api.aruljohn.com/ip/json) | Get IP address | No | Yes | Unknown | [Docs](https://api.aruljohn.com/ip/json) | Unlimited |
| [Cloudflare Trace](https://1.1.1.1/cdn-cgi/trace) | Get IP address, user agent, etc | No | Yes | Unknown | [Docs](https://1.1.1.1/cdn-cgi/trace) | Unlimited |
| [Digital Ocean Status](https://status.digitalocean.com/api/v2/summary.json) | DigitalOcean status | No | Yes | Unknown | [Docs](https://status.digitalocean.com/api/v2/summary.json) | Unlimited |
| [FilterLists](http://filterlists.com/api/directory/lists) | Lists of filters used by ad blockers | No | No | Unknown | [Docs](http://filterlists.com/api/directory/lists) | Unlimited |
| [Genderize.io](https://api.genderize.io?name=scott) | Predict gender based on a name | No | Yes | Unknown | [Docs](https://api.genderize.io?name=scott) | Unlimited |
| [Google Favicons](https://www.google.com/s2/favicons?domain=quora.com&sz=32) | Google's unofficial favicon fetcher | No | Yes | Unknown | [Docs](https://www.google.com/s2/favicons?domain=quora.com&sz=32) | Unlimited |
| [goQR](http://api.qrserver.com/v1/create-qr-code/?data=https://mixedanalytics.com&size=100x100) | Create and read QR codes | No | No | Unknown | [Docs](http://api.qrserver.com/v1/create-qr-code/?data=https://mixedanalytics.com&size=100x100) | Unlimited |
| [HTTPBin](http://httpbin.org/get) | Inspect user agent and headers | No | No | Unknown | [Docs](http://httpbin.org/get) | Unlimited |
| [Image-Charts](https://image-charts.com/chart?cht=p3&chs=700x100&chd=t:60,40&chl=Hello|World&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1) | Chart images | No | Yes | Unknown | [Docs](https://image-charts.com/chart?cht=p3&chs=700x100&chd=t:60,40&chl=Hello|World&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1) | Unlimited |
| [IP2Location](https://api.ip2location.io/) | Get public IP address | No | Yes | Unknown | [Docs](https://api.ip2location.io/) | Unlimited |
| [IPify](https://api.ipify.org?format=json) | Get public IP address | No | Yes | Unknown | [Docs](https://api.ipify.org?format=json) | Unlimited |
| [is.gd](https://is.gd/create.php?format=simple&url=www.example.com) | URL shortener | No | Yes | Unknown | [Docs](https://is.gd/create.php?format=simple&url=www.example.com) | Unlimited |
| [Microlink](https://api.microlink.io/?url=https://github.com/microlinkhq) | Retrieve metadata and screenshots from any URL | No | Yes | Unknown | [Docs](https://api.microlink.io/?url=https://github.com/microlinkhq) | Unlimited |
| [Nationalize.io](https://api.nationalize.io?name=michael) | Predict nationality based on a name | No | Yes | Unknown | [Docs](https://api.nationalize.io?name=michael) | Unlimited |
| [QuickChart](https://quickchart.io/chart?c={type:'bar',data:{labels:[2019,2020,2021,2022, 2023],datasets:[{label:'Users',data:[120,60,50,180,120]}]}}) | Generate charts on-the-fly | No | Yes | Unknown | [Docs](https://quickchart.io/chart?c={type:'bar',data:{labels:[2019,2020,2021,2022, 2023],datasets:[{label:'Users',data:[120,60,50,180,120]}]}}) | Unlimited |
| [Serialif Color](https://color.serialif.com/aquamarine) | Get colors in different formats | No | Yes | Unknown | [Docs](https://color.serialif.com/aquamarine) | Unlimited |
| [Sixdots](https://storeapi.six-dots.app/last_updated_100) | Google playstore analysis | No | Yes | Unknown | [Docs](https://storeapi.six-dots.app/last_updated_100) | Unlimited |
| [Un-Shorten](https://unshorten.me/json/goo.gl/IGL1lE) | Unshorten shortened URLs | No | Yes | Unknown | [Docs](https://unshorten.me/json/goo.gl/IGL1lE) | Unlimited |
| [URLhaus](https://urlhaus-api.abuse.ch/v1/urls/recent/limit/3/) | Receive and submit malware URLs | No | Yes | Unknown | [Docs](https://urlhaus-api.abuse.ch/v1/urls/recent/limit/3/) | Unlimited |
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

| [7Timer!](http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json) | Weather forecasts for astronomy | No | No | Unknown | [Docs](http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json) | Unlimited |
| [Aviation Weather Center](https://aviationweather.gov/api/data/airport?ids=KMCI) | Aviation Digital Data Service (ADDS) data | No | Yes | Unknown | [Docs](https://aviationweather.gov/api/data/airport?ids=KMCI) | Unlimited |
| [openSenseMap](https://api.opensensemap.org/boxes/57000b8745fd40c8196ad04c?format=json) | Personal senseBox (weather station) data | No | Yes | Unknown | [Docs](https://api.opensensemap.org/boxes/57000b8745fd40c8196ad04c?format=json) | Unlimited |
| [SG Weather](https://api.data.gov.sg/v1/environment/air-temperature) | Realtime weather readings for Singapore | No | Yes | Unknown | [Docs](https://api.data.gov.sg/v1/environment/air-temperature) | Unlimited |
| [wttr](wttr.in/London?format=3) | Console-oriented weather forecast service | No | No | Unknown | [Docs](wttr.in/London?format=3) | Unlimited |
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

| [Cocktail Database](https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita) | Cocktail recipes | No | Yes | Unknown | [Docs](https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita) | Unlimited |
| [Open Brewery DB](https://api.openbrewerydb.org/breweries) | Breweries | No | Yes | Unknown | [Docs](https://api.openbrewerydb.org/breweries) | Unlimited |
| [Spoonacular](https://api.spoonacular.com/recipes/complexSearch) | Comprehensive food API | No | Yes | Unknown | [Docs](https://api.spoonacular.com/recipes/complexSearch) | Unlimited |
| [Whisky Hunter](https://whiskyhunter.net/api/auctions_data/?format=json) | Whisky auctions | No | Yes | Unknown | [Docs](https://whiskyhunter.net/api/auctions_data/?format=json) | Unlimited |
**[⬆ Back to Index](#index)**

## Games & Comics

Scores, lore, assets.

| API                                                | Description       | Auth     | HTTPS | CORS    | Link                                        | Free Tier    |
| -------------------------------------------------- | ----------------- | -------- | ----- | ------- | ------------------------------------------- | ------------ |
| [IGDB](https://www.igdb.com/api)                   | Game database     | `apiKey` | Yes   | Unknown | [Docs](https://www.igdb.com/api)            | 1K calls/day |
| [TheSportsDB](https://www.thesportsdb.com/api.php) | Sports events/art | `apiKey` | Yes   | Yes     | [Docs](https://www.thesportsdb.com/api.php) | Unlimited    |
| [Animal Crossing](http://acnhapi.com/)             | Item/critter data | No       | Yes   | Unknown | [Docs](http://acnhapi.com/)                 | Unlimited    |

| [AmiiboAPI](https://www.amiiboapi.com/api/amiibo/?name=mario) | Nintendo Amiibo database | No | Yes | Unknown | [Docs](https://www.amiiboapi.com/api/amiibo/?name=mario) | Unlimited |
| [Barter](https://barter.vg/browse/cards/json) | Digital game libraries, wishlists and tradables | No | Yes | Unknown | [Docs](https://barter.vg/browse/cards/json) | Unlimited |
| [Board Game Geek](https://boardgamegeek.com/xmlapi/search?search=frika) | Board games | No | Yes | Unknown | [Docs](https://boardgamegeek.com/xmlapi/search?search=frika) | Unlimited |
| [CheapShark](https://www.cheapshark.com/api/1.0/deals?upperPrice=15) | Price comparison for digital games | No | Yes | Unknown | [Docs](https://www.cheapshark.com/api/1.0/deals?upperPrice=15) | Unlimited |
| [Chuck Norris Jokes](https://api.chucknorris.io/jokes/random) | Chuck Norris facts | No | Yes | Unknown | [Docs](https://api.chucknorris.io/jokes/random) | Unlimited |
| [D&D 5th Edition](https://www.dnd5eapi.co/api/features) | Official 5th Edition of Dungeons & Dragons | No | Yes | Unknown | [Docs](https://www.dnd5eapi.co/api/features) | Unlimited |
| [Data Dragon](https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json) | League of Legends champions API | No | Yes | Unknown | [Docs](https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json) | Unlimited |
| [Deck of Cards](https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1) | Simulate a deck of cards | No | Yes | Unknown | [Docs](https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1) | Unlimited |
| [Evil Insult Generator](https://evilinsult.com/generate_insult.php?lang=en&type=json) | Generate insults | No | Yes | Unknown | [Docs](https://evilinsult.com/generate_insult.php?lang=en&type=json) | Unlimited |
| [FreeToGame](https://www.freetogame.com/api/games?platform=pc) | Free-to-play games | No | Yes | Unknown | [Docs](https://www.freetogame.com/api/games?platform=pc) | Unlimited |
| [Gamerpower](https://www.gamerpower.com/api/giveaways?platform=steam&type=loot&sort-by=popularity) | Free games and giveaways | No | Yes | Unknown | [Docs](https://www.gamerpower.com/api/giveaways?platform=steam&type=loot&sort-by=popularity) | Unlimited |
| [Hyrule Compendium](https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel) | The Legend of Zelda: BOTW | No | Yes | Unknown | [Docs](https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel) | Unlimited |
| [icanhazdadjoke](https://icanhazdadjoke.com/) | Dad jokes | No | Yes | Unknown | [Docs](https://icanhazdadjoke.com/) | Unlimited |
| [Imgflip](https://api.imgflip.com/get_memes) | Popular memes | No | Yes | Unknown | [Docs](https://api.imgflip.com/get_memes) | Unlimited |
| [isEven](https://api.isevenapi.xyz/api/iseven/12/) | Check if a number is even | No | Yes | Unknown | [Docs](https://api.isevenapi.xyz/api/iseven/12/) | Unlimited |
| [JokeAPI](https://v2.jokeapi.dev/joke/Any?safe-mode) | Jokes | No | Yes | Unknown | [Docs](https://v2.jokeapi.dev/joke/Any?safe-mode) | Unlimited |
| [Magic: The Gathering](https://api.magicthegathering.io/v1/sets) | Cards and sets from MTG | No | Yes | Unknown | [Docs](https://api.magicthegathering.io/v1/sets) | Unlimited |
| [Official Joke](https://official-joke-api.appspot.com/random_joke) | Jokes | No | Yes | Unknown | [Docs](https://official-joke-api.appspot.com/random_joke) | Unlimited |
| [Open Trivia DB](https://opentdb.com/api.php?amount=10&category=17&difficulty=easy) | Trivia questions | No | Yes | Unknown | [Docs](https://opentdb.com/api.php?amount=10&category=17&difficulty=easy) | Unlimited |
| [PokéAPI](https://pokeapi.co/api/v2/pokemon/ditto) | Pokémon data | No | Yes | Unknown | [Docs](https://pokeapi.co/api/v2/pokemon/ditto) | Unlimited |
| [Pokémon TCG](https://api.pokemontcg.io/v2/cards/xy1-1) | Pokémon card data | No | Yes | Unknown | [Docs](https://api.pokemontcg.io/v2/cards/xy1-1) | Unlimited |
| [RuneScape](https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1) | Runescape data | No | Yes | Unknown | [Docs](https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1) | Unlimited |
| [Scryfall](https://api.scryfall.com/cards/search?order=cmc&q=c:red%20pow=3) | Magic: The Gathering card data | No | Yes | Unknown | [Docs](https://api.scryfall.com/cards/search?order=cmc&q=c:red%20pow=3) | Unlimited |
| [TCGdex](https://api.tcgdex.net/v2/en/sets) | Pokémon card data | No | Yes | Unknown | [Docs](https://api.tcgdex.net/v2/en/sets) | Unlimited |
| [XIVAPI](https://xivapi.com/Action/127) | Final Fantasy XIV | No | Yes | Unknown | [Docs](https://xivapi.com/Action/127) | Unlimited |
| [xkcd](http://xkcd.com/info.0.json) | xkcd comics | No | No | Unknown | [Docs](http://xkcd.com/info.0.json) | Unlimited |
| [Yes or No?](https://yesno.wtf/api) | Randomly generate a yes or no image | No | Yes | Unknown | [Docs](https://yesno.wtf/api) | Unlimited |
**[⬆ Back to Index](#index)**

## Geocoding & Maps

Locations, routing.

| API                                                                                       | Description               | Auth     | HTTPS | CORS    | Link                                                            | Free Tier       |
| ----------------------------------------------------------------------------------------- | ------------------------- | -------- | ----- | ------- | --------------------------------------------------------------- | --------------- |
| [BigDataCloud Reverse Geocoding](https://www.bigdatacloud.com/packages/reverse-geocoding) | Address from coords       | `apiKey` | Yes   | Yes     | [Docs](https://www.bigdatacloud.com/packages/reverse-geocoding) | 10K calls/month |
| [OpenStreetMap Nominatim](https://nominatim.org/release-docs/develop/api/Search/)         | Search/ geocode           | No       | Yes   | Unknown | [Docs](https://nominatim.org/release-docs/develop/api/Search/)  | Rate limited    |
| [Positionstack](https://positionstack.com/)                                               | Forward/reverse geocoding | `apiKey` | Yes   | Unknown | [Docs](https://positionstack.com/)                              | 25K calls/month |

| [Adresse](https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port) | French addresses and geocoding | No | Yes | Unknown | [Docs](https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port) | Unlimited |
| [Country.is](https://api.country.is/9.9.9.9) | Lookup country by IP address | No | Yes | Unknown | [Docs](https://api.country.is/9.9.9.9) | Unlimited |
| [Geocode](https://geocode.xyz/51.50354,-0.12768?geoit=json) | Forward/reverse geocoding | No | Yes | Unknown | [Docs](https://geocode.xyz/51.50354,-0.12768?geoit=json) | Unlimited |
| [GeoJS](https://get.geojs.io/v1/ip/geo.json) | Geolocation by IP address | No | Yes | Unknown | [Docs](https://get.geojs.io/v1/ip/geo.json) | Unlimited |
| [geoPlugin](http://www.geoplugin.net/php.gp) | Currency conversion and geolocation data | No | No | Unknown | [Docs](http://www.geoplugin.net/php.gp) | Unlimited |
| [GetTheData](https://api.getthedata.com/bng2latlong/529090/179645) | UK geo coordinates conversion | No | Yes | Unknown | [Docs](https://api.getthedata.com/bng2latlong/529090/179645) | Unlimited |
| [HelloSalut](http://stefanbohacek.com/hellosalut/?mode=auto) | Translate "hello" by IP address | No | No | Unknown | [Docs](http://stefanbohacek.com/hellosalut/?mode=auto) | Unlimited |
| [Hong Kong GeoData Store](https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=museums) | Hong Kong geo data | No | Yes | Unknown | [Docs](https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=museums) | Unlimited |
| [ipapi](https://ipapi.co/json/) | Geolocation by IP address | No | Yes | Unknown | [Docs](https://ipapi.co/json/) | Unlimited |
| [IPGeo](https://api.techniknews.net/ipgeo/) | Geolocation by IP address | No | Yes | Unknown | [Docs](https://api.techniknews.net/ipgeo/) | Unlimited |
| [Nominatum](https://nominatim.openstreetmap.org/search.php?city=taipei&format=jsonv2) | Locations and addresses | No | Yes | Unknown | [Docs](https://nominatim.openstreetmap.org/search.php?city=taipei&format=jsonv2) | Unlimited |
| [Open Topo Data](https://api.opentopodata.org/v1/srtm90m?locations=-43.5,172.5|27.6,1.98&interpolation=cubic) | Determine elevation for lat/long | No | Yes | Unknown | [Docs](https://api.opentopodata.org/v1/srtm90m?locations=-43.5,172.5|27.6,1.98&interpolation=cubic) | Unlimited |
| [Postcodes](https://api.postcodes.io/postcodes/OX49%205NU) | UK geo data by postcode | No | Yes | Unknown | [Docs](https://api.postcodes.io/postcodes/OX49%205NU) | Unlimited |
| [ViaCEP](https://viacep.com.br/ws/01001000/json/) | Brazil's postal address codes (CEPs) | No | Yes | Unknown | [Docs](https://viacep.com.br/ws/01001000/json/) | Unlimited |
| [Zippopotamus](https://api.zippopotam.us/us/90210) | Zip code information for 60 countries | No | Yes | Unknown | [Docs](https://api.zippopotam.us/us/90210) | Unlimited |
| [Ziptastic](https://ziptasticapi.com/90210) | US geo data by zipcode | No | Yes | Unknown | [Docs](https://ziptasticapi.com/90210) | Unlimited |
**[⬆ Back to Index](#index)**

## Government & Open Data

Public records, stats.

| API                                      | Description        | Auth     | HTTPS | CORS    | Link                                  | Free Tier |
| ---------------------------------------- | ------------------ | -------- | ----- | ------- | ------------------------------------- | --------- |
| [USA.gov](https://www.usa.gov/developer) | US gov data        | `apiKey` | Yes   | Unknown | [Docs](https://www.usa.gov/developer) | Unlimited |
| [Congress.gov](https://api.congress.gov) | US legislation     | No       | Yes   | Unknown | [Docs](https://api.congress.gov)      | Unlimited |
| [API Setu](https://www.apisetu.gov.in/)  | India gov services | No       | Yes   | Yes     | [Docs](https://www.apisetu.gov.in/)   | Unlimited |

| [Banco Central Do Brasil](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados/ultimos/10?formato=json) | Brazil Central Bank data | No | Yes | Unknown | [Docs](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados/ultimos/10?formato=json) | Unlimited |
| [Belgian Open Data Initiative](https://social.brussels/rest/sector/5/organisations) | Belgian government open data | No | Yes | Unknown | [Docs](https://social.brussels/rest/sector/5/organisations) | Unlimited |
| [Brasil](https://brasilapi.com.br/api/feriados/v1/2024) | Brazil public data | No | Yes | Unknown | [Docs](https://brasilapi.com.br/api/feriados/v1/2024) | Unlimited |
| [CiviX](https://www.bclaws.gov.bc.ca/civix/search/complete/fullsearch?q=water&s=0&e=20&nFrag=5&lFrag=100) | Law and bylaw content of British Columbia | No | Yes | Unknown | [Docs](https://www.bclaws.gov.bc.ca/civix/search/complete/fullsearch?q=water&s=0&e=20&nFrag=5&lFrag=100) | Unlimited |
| [Colorado Information Marketplace](https://data.colorado.gov/resource/4ykn-tg5h.json) | Colorado state open data | No | Yes | Unknown | [Docs](https://data.colorado.gov/resource/4ykn-tg5h.json) | Unlimited |
| [Data USA](https://datausa.io/api/data?drilldowns=Nation&measures=Population) | US public data | No | Yes | Unknown | [Docs](https://datausa.io/api/data?drilldowns=Nation&measures=Population) | Unlimited |
| [Data.gov](https://data.ny.gov/api/views/d6yy-54nr/rows.xml?accessType=DOWNLOAD) | U.S. government open data | No | Yes | Unknown | [Docs](https://data.ny.gov/api/views/d6yy-54nr/rows.xml?accessType=DOWNLOAD) | Unlimited |
| [Data.gov.au](https://www.data.act.gov.au/api/views/s4g9-ndv2/rows.json?accessType=DOWNLOAD) | Australian government open data | No | Yes | Unknown | [Docs](https://www.data.act.gov.au/api/views/s4g9-ndv2/rows.json?accessType=DOWNLOAD) | Unlimited |
| [Dawum](https://api.dawum.de/) | German election polls | No | Yes | Unknown | [Docs](https://api.dawum.de/) | Unlimited |
| [European Commission Taxation and Customs](https://ec.europa.eu/taxation_customs/vies/rest-api/ms/DE/vat/122268496) | Europan Comission taxes | No | Yes | Unknown | [Docs](https://ec.europa.eu/taxation_customs/vies/rest-api/ms/DE/vat/122268496) | Unlimited |
| [FBI Wanted](https://api.fbi.gov/wanted/v1/list) | FBI Wanted data | No | Yes | Unknown | [Docs](https://api.fbi.gov/wanted/v1/list) | Unlimited |
| [Federal Register](https://www.federalregister.gov/api/v1/documents/2023-05167?publication_date=2023-03-14) | Daily journal of the US government | No | Yes | Unknown | [Docs](https://www.federalregister.gov/api/v1/documents/2023-05167?publication_date=2023-03-14) | Unlimited |
| [Food Standards Agency](https://ratings.food.gov.uk/OpenDataFiles/FHRS529en-GB.json) | UK restaurant hygiene ratings | No | Yes | Unknown | [Docs](https://ratings.food.gov.uk/OpenDataFiles/FHRS529en-GB.json) | Unlimited |
| [NYC Open Data](https://data.cityofnewyork.us/resource/erm2-nwe9.json?unique_key=57056073) | New York City open data | No | Yes | Unknown | [Docs](https://data.cityofnewyork.us/resource/erm2-nwe9.json?unique_key=57056073) | Unlimited |
| [Open Data DC](https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_TrafficVolume_WebMercator/MapServer/171/query?where=1%3D1&outFields=ROUTEID,FROMMEASURE,TOMEASURE,FROMDATE,TODATE&outSR=4326&f=json) | Washington DC open data | No | Yes | Unknown | [Docs](https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_TrafficVolume_WebMercator/MapServer/171/query?where=1%3D1&outFields=ROUTEID,FROMMEASURE,TOMEASURE,FROMDATE,TODATE&outSR=4326&f=json) | Unlimited |
| [Open Government, Canada](https://open.canada.ca/data/api/action/package_show?id=5953da6b-d81b-4a2c-8b27-145892827fb0) | Canadian government open data | No | Yes | Unknown | [Docs](https://open.canada.ca/data/api/action/package_show?id=5953da6b-d81b-4a2c-8b27-145892827fb0) | Unlimited |
| [Represent Civic Information](https://represent.opennorth.ca/representatives/?first_name=Jack) | Canada's elected officials and electoral districts | No | Yes | Unknown | [Docs](https://represent.opennorth.ca/representatives/?first_name=Jack) | Unlimited |
| [USAspending](https://api.usaspending.gov/api/v2/references/toptier_agencies/) | U.S. federal government spending data | No | Yes | Unknown | [Docs](https://api.usaspending.gov/api/v2/references/toptier_agencies/) | Unlimited |
| [USPTO](https://developer.uspto.gov/ipmarketplace-api/search/query?searchText=vehicles) | US Patent and Trademark Office | No | Yes | Unknown | [Docs](https://developer.uspto.gov/ipmarketplace-api/search/query?searchText=vehicles) | Unlimited |
| [World Bank](http://api.worldbank.org/v2/region?format=json) | World Bank open data | No | No | Unknown | [Docs](http://api.worldbank.org/v2/region?format=json) | Unlimited |
| [Archive.org](https://archive.org/metadata/TheAdventuresOfTomSawyer_201303) | Large public digital archive | No | Yes | Unknown | [Docs](https://archive.org/metadata/TheAdventuresOfTomSawyer_201303) | Unlimited |
| [Carbon Intensity](https://api.carbonintensity.org.uk/intensity/date) | Carbon intensity of the electricity system in Great Britain | No | Yes | Unknown | [Docs](https://api.carbonintensity.org.uk/intensity/date) | Unlimited |
| [Data.Police.UK](https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2023-01) | UK crime & police data | No | Yes | Unknown | [Docs](https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2023-01) | Unlimited |
| [Fipe](https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos) | Brazilian vehicles and prices | No | Yes | Unknown | [Docs](https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos) | Unlimited |
| [House Stock Watcher](https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml) | US Congress members' stock transactions | No | Yes | Unknown | [Docs](https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml) | Unlimited |
| [Leadsbox](https://leadsbox.biz/?query=lawyers+in+germany) | 71 Million business records in 202 countries | No | Yes | Unknown | [Docs](https://leadsbox.biz/?query=lawyers+in+germany) | Unlimited |
| [Open Library](http://openlibrary.org/api/volumes/brief/isbn/9780525440987.json) | Information about books | No | No | Unknown | [Docs](http://openlibrary.org/api/volumes/brief/isbn/9780525440987.json) | Unlimited |
| [PM2.5](https://pm25.lass-net.org/API-1.0.0/project/airbox/latest/) | PM2.5 environmental data monitoring | No | Yes | Unknown | [Docs](https://pm25.lass-net.org/API-1.0.0/project/airbox/latest/) | Unlimited |
| [Universities List](http://universities.hipolabs.com/search?country=United+Kingdom) | Universities | No | No | Unknown | [Docs](http://universities.hipolabs.com/search?country=United+Kingdom) | Unlimited |
| [Vehicles](https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMake/merc?format=json) | National Highway Traffic Safety Administration's catalog of vehicles specs | No | Yes | Unknown | [Docs](https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMake/merc?format=json) | Unlimited |
| [Wayback Machine](https://archive.org/wayback/available?url=google.com) | Internet archive availability | No | Yes | Unknown | [Docs](https://archive.org/wayback/available?url=google.com) | Unlimited |
| [Wikipedia](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Tiger_King/daily/20210901/20210930) | Pageview stats | No | Yes | Unknown | [Docs](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Tiger_King/daily/20210901/20210930) | Unlimited |
**[⬆ Back to Index](#index)**

## Health

Symptoms, trackers (use ethically).

| API                                                                | Description      | Auth     | HTTPS | CORS    | Link                                                        | Free Tier       |
| ------------------------------------------------------------------ | ---------------- | -------- | ----- | ------- | ----------------------------------------------------------- | --------------- |
| [ApiMedic](https://apimedic.com/)                                  | Symptom checker  | `apiKey` | Yes   | Unknown | [Docs](https://apimedic.com/)                               | 100 calls/day   |
| [Infermedica](https://developer.infermedica.com/docs/introduction) | Triage/diagnosis | `apiKey` | Yes   | Unknown | [Docs](https://developer.infermedica.com/docs/introduction) | 1K checks/month |

| [HealthCare.gov](https://www.healthcare.gov/api/index.json) | US health insurance data | No | Yes | Unknown | [Docs](https://www.healthcare.gov/api/index.json) | Unlimited |
| [Makeup](http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline) | Makeup brands and product info | No | No | Unknown | [Docs](http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline) | Unlimited |
| [NPPES](https://npiregistry.cms.hhs.gov/api/?version=2.1&city=baltimore) | US health care providers | No | Yes | Unknown | [Docs](https://npiregistry.cms.hhs.gov/api/?version=2.1&city=baltimore) | Unlimited |
| [openFDA](https://api.fda.gov/food/enforcement.json?limit=10) | Food & Drug Administration data (US) | No | Yes | Unknown | [Docs](https://api.fda.gov/food/enforcement.json?limit=10) | Unlimited |
**[⬆ Back to Index](#index)**

## Jobs

Listings and career data.

| API                                            | Description      | Auth | HTTPS | CORS | Link                                   | Free Tier |
| ---------------------------------------------- | ---------------- | ---- | ----- | ---- | -------------------------------------- | --------- |
| [GraphQL Jobs](https://graphql.jobs/docs/api/) | Job board search | No   | Yes   | Yes  | [Docs](https://graphql.jobs/docs/api/) | Unlimited |

| [Jobicy](https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo) | List of remote jobs | No | Yes | Unknown | [Docs](https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo) | Unlimited |
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

| [Final Space](https://finalspaceapi.com/api/v0/episode/) | Television show Final Space | No | Yes | Unknown | [Docs](https://finalspaceapi.com/api/v0/episode/) | Unlimited |
| [Rick and Morty](https://rickandmortyapi.com/api/character/108) | Rick and Morty characters | No | Yes | Unknown | [Docs](https://rickandmortyapi.com/api/character/108) | Unlimited |
| [STAPI](https://stapi.co/api/v2/rest/spacecraft/search) | Star Trek information | No | Yes | Unknown | [Docs](https://stapi.co/api/v2/rest/spacecraft/search) | Unlimited |
| [SWAPI](https://swapi.dev/api/planets/3/?format=json) | Star Wars information | No | Yes | Unknown | [Docs](https://swapi.dev/api/planets/3/?format=json) | Unlimited |
| [TVMaze](http://api.tvmaze.com/search/shows?q=golden girls) | TV show information | No | No | Unknown | [Docs](http://api.tvmaze.com/search/shows?q=golden girls) | Unlimited |
**[⬆ Back to Index](#index)**

## Music

Tracks, lyrics, metadata.

| API                                                                | Description       | Auth     | HTTPS | CORS    | Link                                                        | Free Tier |
| ------------------------------------------------------------------ | ----------------- | -------- | ----- | ------- | ----------------------------------------------------------- | --------- |
| [Spotify Web](https://developer.spotify.com/documentation/web-api) | Playlists, search | `OAuth`  | Yes   | Unknown | [Docs](https://developer.spotify.com/documentation/web-api) | Unlimited |
| [Lyrics.ovh](https://lyricsovh.docs.apiary.io)                     | Song lyrics       | No       | Yes   | Unknown | [Docs](https://lyricsovh.docs.apiary.io)                    | Unlimited |
| [TheAudioDB](http://www.theaudiodb.com)                            | Artist/album art  | `apiKey` | Yes   | Unknown | [Docs](http://www.theaudiodb.com)                           | Unlimited |

| [Binary Jazz](https://binaryjazz.us/wp-json/genrenator/v1/genre/5) | Fetch a random genre | No | Yes | Unknown | [Docs](https://binaryjazz.us/wp-json/genrenator/v1/genre/5) | Unlimited |
| [iTunes Search](https://itunes.apple.com/search?term=radiohead) | iTunes content | No | Yes | Unknown | [Docs](https://itunes.apple.com/search?term=radiohead) | Unlimited |
| [MusicBrainz](http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json) | Music data | No | No | Unknown | [Docs](http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json) | Unlimited |
| [Openwhyd](https://openwhyd.org/hot/electro?format=json) | Playlists from various streaming platforms | No | Yes | Unknown | [Docs](https://openwhyd.org/hot/electro?format=json) | Unlimited |
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

| [Advice Slip](https://api.adviceslip.com/advice/search/love) | Generate random advice | No | Yes | Unknown | [Docs](https://api.adviceslip.com/advice/search/love) | Unlimited |
| [Affirmations](https://www.affirmations.dev/) | Generate affirmations | No | Yes | Unknown | [Docs](https://www.affirmations.dev/) | Unlimited |
| [Breaking Bad Quotes](https://api.breakingbadquotes.xyz/v1/quotes) | Retrieve some quotes of Breaking Bad | No | Yes | Unknown | [Docs](https://api.breakingbadquotes.xyz/v1/quotes) | Unlimited |
| [Dictum](https://api.fisenko.net/v1/quotes/en?query=string&offset=0&limit=0) | Inspiring expressions | No | Yes | Unknown | [Docs](https://api.fisenko.net/v1/quotes/en?query=string&offset=0&limit=0) | Unlimited |
| [Game of Thrones Quotes](https://api.gameofthronesquotes.xyz/v1/random) | Retrieve some quotes of Game of Thrones | No | Yes | Unknown | [Docs](https://api.gameofthronesquotes.xyz/v1/random) | Unlimited |
| [Kanye](https://api.kanye.rest/) | Kanye quotes | No | Yes | Unknown | [Docs](https://api.kanye.rest/) | Unlimited |
| [Quotable](https://api.quotable.io/quotes/random) | Random quotes | No | Yes | Unknown | [Docs](https://api.quotable.io/quotes/random) | Unlimited |
| [Quote Garden](https://quote-garden.onrender.com/api/v3/quotes) | Database of 75000 quotes | No | Yes | Unknown | [Docs](https://quote-garden.onrender.com/api/v3/quotes) | Unlimited |
| [Quotes on Design](https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand) | Quotes about design | No | Yes | Unknown | [Docs](https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand) | Unlimited |
| [Ron Swanson Quotes](https://ron-swanson-quotes.herokuapp.com/v2/quotes) | Ron Swanson quotes API | No | Yes | Unknown | [Docs](https://ron-swanson-quotes.herokuapp.com/v2/quotes) | Unlimited |
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

| [Arcsecond](https://api.arcsecond.io/activities/) | Worldwide astronomy data | No | Yes | Unknown | [Docs](https://api.arcsecond.io/activities/) | Unlimited |
| [Asterank](http://www.asterank.com/api/skymorph/search?target=J99TS7A) | Asteroids, minor planets, and other objects | No | No | Unknown | [Docs](http://www.asterank.com/api/skymorph/search?target=J99TS7A) | Unlimited |
| [Cat-Facts](https://cat-fact.herokuapp.com/facts/random) | Daily cat facts | No | Yes | Unknown | [Docs](https://cat-fact.herokuapp.com/facts/random) | Unlimited |
| [CelesTrak](https://celestrak.org/NORAD/elements/gp.php?INTDES=2023-015&FORMAT=JSON-PRETTY) | General perturbations orbital data | No | Yes | Unknown | [Docs](https://celestrak.org/NORAD/elements/gp.php?INTDES=2023-015&FORMAT=JSON-PRETTY) | Unlimited |
| [GBIF](https://api.gbif.org/v1/occurrence/search?year=1800,1899) | Global Biodiversity Information Facility | No | Yes | Unknown | [Docs](https://api.gbif.org/v1/occurrence/search?year=1800,1899) | Unlimited |
| [iDigBio](https://search.idigbio.org/v2/search/records/?rq={"data.dwc:dynamicProperties":"nsf_tcn"}&limit=1) | Digitized data for millions of biological specimens | No | Yes | Unknown | [Docs](https://search.idigbio.org/v2/search/records/?rq={"data.dwc:dynamicProperties":"nsf_tcn"}&limit=1) | Unlimited |
| [ITIS](https://www.itis.gov/ITISWebService/services/ITISService/searchByCommonName?srchKey=ferret-badger) | Integrated Taxonomic Information System | No | Yes | Unknown | [Docs](https://www.itis.gov/ITISWebService/services/ITISService/searchByCommonName?srchKey=ferret-badger) | Unlimited |
| [Newton](https://newton.now.sh/api/v2/factor/x^2-1) | Advanced math | No | Yes | Unknown | [Docs](https://newton.now.sh/api/v2/factor/x^2-1) | Unlimited |
| [Numbers](http://numbersapi.com/random/math) | Facts about numbers | No | No | Unknown | [Docs](http://numbersapi.com/random/math) | Unlimited |
| [Open Notify](http://api.open-notify.org/astros.json) | ISS location and people in space | No | No | Unknown | [Docs](http://api.open-notify.org/astros.json) | Unlimited |
| [Spaceflight News](https://api.spaceflightnewsapi.net/v3/articles) | Spaceflight related news | No | Yes | Unknown | [Docs](https://api.spaceflightnewsapi.net/v3/articles) | Unlimited |
| [SpaceX](https://api.spacexdata.com/v5/launches/latest) | Launch and rocket data | No | Yes | Unknown | [Docs](https://api.spacexdata.com/v5/launches/latest) | Unlimited |
| [SunriseSunset](https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873&timezone=UTC&date=today) | Sunrise and sunset times | No | Yes | Unknown | [Docs](https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873&timezone=UTC&date=today) | Unlimited |
| [TheSpaceDevs](https://ll.thespacedevs.com/2.2.0/agencies/?limit=10) | Rocket launches, space events and crewed spaceflight | No | Yes | Unknown | [Docs](https://ll.thespacedevs.com/2.2.0/agencies/?limit=10) | Unlimited |
| [USGS Earthquake Catalog](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-03-01&endtime=2023-03-02&minmagnitude=5) | Latest earthquakes | No | Yes | Unknown | [Docs](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-03-01&endtime=2023-03-02&minmagnitude=5) | Unlimited |
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

| [CityBikes](http://api.citybik.es/v2/networks) | Bike sharing networks | No | No | Unknown | [Docs](http://api.citybik.es/v2/networks) | Unlimited |
| [Ergast F1](http://ergast.com/api/f1/drivers.json) | Motor racing data | No | No | Unknown | [Docs](http://ergast.com/api/f1/drivers.json) | Unlimited |
| [Football-Data](http://api.football-data.org/v4/competitions/) | Football (soccer) competitions and data | No | No | Unknown | [Docs](http://api.football-data.org/v4/competitions/) | Unlimited |
| [nhlapi](https://api-web.nhle.com/v1/standings-season) | NHL data | No | Yes | Unknown | [Docs](https://api-web.nhle.com/v1/standings-season) | Unlimited |
**[⬆ Back to Index](#index)**

## Test Data & Mocking

Fakes for prototyping.

| API                                                              | Description         | Auth | HTTPS | CORS    | Link                                             | Free Tier |
| ---------------------------------------------------------------- | ------------------- | ---- | ----- | ------- | ------------------------------------------------ | --------- |
| [RandomUser](https://randomuser.me)                              | Fake users/profiles | No   | Yes   | Unknown | [Docs](https://randomuser.me)                    | Unlimited |
| [Mockyard](https://mockyard.in/)                                 | Realistic mocks     | No   | Yes   | Yes     | [Docs](https://mockyard.in/)                     | Unlimited |
| [English Random Words](https://random-words-api.vercel.app/word) | Word generation     | No   | Yes   | No      | [Docs](https://random-words-api.vercel.app/word) | Unlimited |

| [Bacon Ipsum](https://baconipsum.com/api/?type=meat-and-filler) | Generate fake data for testing | No | Yes | Unknown | [Docs](https://baconipsum.com/api/?type=meat-and-filler) | Unlimited |
| [Faker](https://fakerapi.it/api/v1/credit_cards?_quantity=2) | Generate fake data | No | Yes | Unknown | [Docs](https://fakerapi.it/api/v1/credit_cards?_quantity=2) | Unlimited |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts/1) | Fake REST API for testing | No | Yes | Unknown | [Docs](https://jsonplaceholder.typicode.com/posts/1) | Unlimited |
| [Loripsum](https://loripsum.net/api/10/short/headers) | Generate fake placeholder text | No | Yes | Unknown | [Docs](https://loripsum.net/api/10/short/headers) | Unlimited |
| [Reqres](https://reqres.in/api/users?page=1) | Test against a real API | No | Yes | Unknown | [Docs](https://reqres.in/api/users?page=1) | Unlimited |
| [REST](https://api.restful-api.dev/objects) | Rest API for testing | No | Yes | Unknown | [Docs](https://api.restful-api.dev/objects) | Unlimited |
| [Softwium](https://softwium.com/api/books) | Dummy JSON data for a variety of categories | No | Yes | Unknown | [Docs](https://softwium.com/api/books) | Unlimited |
| [UUID Generator](https://www.uuidtools.com/api/generate/v1/count/3) | Generate UUIDs and GUIDs | No | Yes | Unknown | [Docs](https://www.uuidtools.com/api/generate/v1/count/3) | Unlimited |
**[⬆ Back to Index](#index)**

## Text Analysis & NLP

Sentiment, translation.

| API                                                                             | Description            | Auth     | HTTPS | CORS    | Link                                                              | Free Tier       |
| ------------------------------------------------------------------------------- | ---------------------- | -------- | ----- | ------- | ----------------------------------------------------------------- | --------------- |
| [Detect Language](https://detectlanguage.com/)                                  | Lang ID                | `apiKey` | Yes   | Unknown | [Docs](https://detectlanguage.com/)                               | 100 calls/month |
| [LibreTranslate](https://libretranslate.com/docs)                               | Translation (17 langs) | No       | Yes   | Unknown | [Docs](https://libretranslate.com/docs)                           | Self-host free  |
| [Sentiment Analysis](https://www.meaningcloud.com/developer/sentiment-analysis) | Multilingual sentiment | `apiKey` | Yes   | Yes     | [Docs](https://www.meaningcloud.com/developer/sentiment-analysis) | 20K words/month |

| [Chinese Character Web](http://ccdb.hemiola.com/characters/radicals/85?count) | Information about Chinese characters | No | No | Unknown | [Docs](http://ccdb.hemiola.com/characters/radicals/85?count) | Unlimited |
| [Chinese Text Project](https://api.ctext.org/getdictionaryheadwords) | Digital library for pre-modern Chinese texts | No | Yes | Unknown | [Docs](https://api.ctext.org/getdictionaryheadwords) | Unlimited |
| [Datamuse](https://api.datamuse.com/words?ml=ringing+in+the+ears) | Query words matching conditions | No | Yes | Unknown | [Docs](https://api.datamuse.com/words?ml=ringing+in+the+ears) | Unlimited |
| [Free Dictionary](https://api.dictionaryapi.dev/api/v2/entries/en/digital) | Word definitions and phonetics | No | Yes | Unknown | [Docs](https://api.dictionaryapi.dev/api/v2/entries/en/digital) | Unlimited |
| [PurgoMalum](https://www.purgomalum.com/service/json?text=this%20is%20some%20test%20input) | Check content for profanity | No | Yes | Unknown | [Docs](https://www.purgomalum.com/service/json?text=this%20is%20some%20test%20input) | Unlimited |
**[⬆ Back to Index](#index)**

## Transportation

Flights, routes.

| API                                                              | Description         | Auth     | HTTPS | CORS    | Link                                                  | Free Tier     |
| ---------------------------------------------------------------- | ------------------- | -------- | ----- | ------- | ----------------------------------------------------- | ------------- |
| [OpenSky Network](https://opensky-network.org/apidoc/index.html) | Flight tracking     | No       | Yes   | Unknown | [Docs](https://opensky-network.org/apidoc/index.html) | Unlimited     |
| [AviationStack](https://aviationstack.com/)                      | Airport/flight data | `apiKey` | Yes   | Unknown | [Docs](https://aviationstack.com/)                    | 100 req/month |
| [GraphHopper](https://docs.graphhopper.com/)                     | Routing/directions  | `apiKey` | Yes   | Unknown | [Docs](https://docs.graphhopper.com/)                 | 2.5K req/day  |

| [Derhuerst](https://v6.vbb.transport.rest/locations?query=berlin) | Public transport for Berlin & Brandenburg | No | Yes | Unknown | [Docs](https://v6.vbb.transport.rest/locations?query=berlin) | Unlimited |
| [iRail](https://api.irail.be/vehicle/?id=BE.NMBS.IC1832&format=json&lang=en&alerts=false) | Belgian railways | No | Yes | Unknown | [Docs](https://api.irail.be/vehicle/?id=BE.NMBS.IC1832&format=json&lang=en&alerts=false) | Unlimited |
| [MBTA](https://api-v3.mbta.com/route_patterns?filter[route]=CR-Providence&include=representative_trip&fields[trip]=headsign) | Public transport for Boston | No | Yes | Unknown | [Docs](https://api-v3.mbta.com/route_patterns?filter[route]=CR-Providence&include=representative_trip&fields[trip]=headsign) | Unlimited |
| [Metro Lisboa](https://app.metrolisboa.pt/status/getLinhas.php) | Subway line status | No | Yes | Unknown | [Docs](https://app.metrolisboa.pt/status/getLinhas.php) | Unlimited |
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
