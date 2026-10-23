# No-fee FAQ chatbot

A free, open-source FAQ chatbot for small business websites. It answers your customers' common questions from a list **you** approve, so it never makes up prices, opening times or promises.

- **One file.** `faq-bot.js` is about 7 KB with no dependencies.
- **No monthly fee.** No AI service, no API key, no server. It runs in the visitor's browser.
- **Honest.** If a question isn't on your list, it says it doesn't know and points to your email instead of guessing.
- **Forgiving.** Handles different wording, plurals and small typos ("tomorow"), and you can add your own synonyms.
- **Private.** No cookies, no tracking, nothing sent anywhere.

**[Live demo](https://www.tchworks.co.uk/no-fee-faq-chatbot/)** (set up for a pretend bakery).

## Quick start

1. Put your questions in a spreadsheet with three columns, `question`, `answer`, `keywords` (keywords separated by `;`), and save it as CSV. See [`example/faqs.csv`](example/faqs.csv).
2. Turn it into the config file (Python 3, standard library only):
   ```
   python3 tools/csv_to_faq.py faqs.csv faq.json --name "Your Business" --colour "#1f3fbf" --email hello@your-site.co.uk
   ```
3. Upload `faq-bot.js` and `faq.json` to your site and add this just before `</body>`:
   ```html
   <script src="/faq-bot.js" data-config="/faq.json" defer></script>
   ```

A round "Questions? Ask us" button appears bottom right. Answers can include links written as `[text](https://...)`.

## Platforms

- **Any HTML site / GitHub Pages / Netlify:** upload both files and paste the script tag.
- **WordPress:** upload both files to Media (or your theme folder), then add the script tag with a header/footer code plugin, using the full file URLs.
- **Squarespace:** use the Code Injection footer box. Host the two files somewhere public (e.g. a free GitHub Pages repo) and use their full URLs, or paste the config inline (see below).
- **Wix:** add it as Custom Code placed at the end of the body, with full URLs as above.
- **Shopify:** upload both files to your store's Files area, then add the script tag to `theme.liquid` just before `</body>`.

Some builders only allow custom code on paid plans; check yours first.

### Inline config (no second file)

```html
<script>window.TCH_FAQ = { "name": "Your Business", "faqs": [ {"q": "What are your opening hours?", "keywords": ["open","hours"], "a": "Tue–Sat, 8am–4pm."} ] };</script>
<script src="https://your-site/faq-bot.js" defer></script>
```

### Embed in the page instead of a floating button

```js
fetch("/faq.json").then(r => r.json()).then(c => { c.inline = "#faq-box"; TCHFaqBot.mount(c); });
```

## Config options

| Key | What it does |
|---|---|
| `faqs` | List of `{ "q": question, "a": answer, "keywords": [...] }` |
| `name`, `colour`, `button` | Header title, brand colour, button text |
| `greeting`, `fallback` | First message, and the reply when it doesn't know |
| `suggest` | Indexes of questions to show as tap-to-ask chips |
| `synonyms` | `{ "price": ["cost","fee"] }` so different words match |
| `threshold` | How sure it must be before answering (default `0.34`; raise it to guess less) |

## Test it

```
node test/test.js
```

Runs 24 differently worded questions against the example, including off-topic ones it must refuse. Write your own cases the same way before going live.

## Want it set up for you?

[TCH Works](https://www.tchworks.co.uk/services/faq-chatbot/?src=github) will write the questions from your own website, get every answer approved by you, match your brand colour, test 30+ ways of asking, and send install steps for your platform. **From £60, one-off, no monthly fee.** Email tchworks.shop@agentmail.to.

## Licence

MIT. Use it on as many sites as you like, including client sites.
