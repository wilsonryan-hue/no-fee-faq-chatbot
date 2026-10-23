// Run: node test/test.js  — checks differently worded questions hit the right answer, and off-topic ones get "I don't know".
global.window = {}; global.document = { readyState: "complete", currentScript: null, querySelector: () => null };
require("../faq-bot.js");
const cfg = require("../example/faq.json");
const bot = new window.TCHFaqBot.Bot(cfg);
const cases = [
  ["when are you open", 0], ["what time do you close on saturday", 0], ["opening times?", 0],
  ["can i order a birthday cake", 1], ["custom cake orders", 1],
  ["anything gluten free", 2], ["is it safe for coeliacs", 2],
  ["do you deliver", 3], ["can you deliver a cake", 3],
  ["where do i park", 4], ["is there parking nearby", 4],
  ["do you take contactless", 5], ["can i pay with cash", 5],
  ["vegan options?", 6], ["anything without dairy", 6],
  ["can you hold a loaf for me", 7], ["reserve bread for tomorow", 7],
  ["wholesale for my cafe", 8], ["trade prices for a business", 8],
  ["i want my money back", 9], ["refund please", 9],
];
const misses = ["what is the capital of france", "tell me a joke about cats", "who won the football"];
let fail = 0;
for (const [q, want] of cases) {
  const r = bot.ask(q);
  const got = r && !r.miss ? cfg.faqs.indexOf(r.f) : -1;
  if (got !== want) { fail++; console.log("FAIL", JSON.stringify(q), "got", got, "want", want); }
}
for (const q of misses) {
  const r = bot.ask(q);
  if (!r || !r.miss) { fail++; console.log("FAIL should not answer", JSON.stringify(q), r && r.f && r.f.q); }
}
console.log(`${cases.length + misses.length - fail}/${cases.length + misses.length} passed`);
process.exit(fail ? 1 : 0);
