# LumenLive — راهنمای کامل پروژه برای Claude Code
**آخرین بروزرسانی**: ۲۲ ژوئن ۲۰۲۶

---

## اطلاعات کلیدی

| چیز | مقدار |
|-----|-------|
| نوع پروژه | Telegram Mini App |
| مسیر | `Desktop/LumenLive/` |
| بات | `@LumenLive_bot` (توکن در `.env`) |
| زبان بات | Python |
| زبان Mini App | HTML/CSS/JS |
| هاست فعلی | localhost (Live Server) |
| هاست نهایی | GitHub + Vercel (انجام نشده) |
| دیتابیس | Supabase (وصل شده) |

### Supabase
- URL: `https://tiifrhxyosmkfizpfcuz.supabase.co`
- جدول: `user_coins` (id, created_at, telegram_user_id int8, coin_symbol text, is_active bool default true)
- Policy: `allow_all_operations` (ALL, public, using: true)
- Unique Constraint: روی (telegram_user_id, coin_symbol)
- Keys: در `.env` — SUPABASE_URL + SUPABASE_PUBLISHABLE_KEY

### API
- CoinGecko Demo: رایگان، 100 call/دقیقه — برای قیمت کریپتو
- TELEGRAM_USER_ID موقت برای تست: `123456789` (بعداً از Telegram.WebApp.initDataUnsafe.user.id)

---

## ساختار فایل‌ها

```
LumenLive/
├── bot/
│   ├── main.py              ✅ کار می‌کنه
│   └── services/
│       └── price_service.py ✅ 30 کوین
├── miniapp/
│   ├── index.html           ✅ Home Screen
│   ├── crypto.html          ✅ لیست کوین‌ها (Supabase + CoinGecko)
│   ├── manage-crypto.html   ✅ مدیریت 30 کوین
│   ├── coin-detail.html     ⚠️ ناقص
│   ├── metals.html          ❌ نساخته
│   ├── stocks.html          ❌ نساخته
│   ├── more.html            ❌ خالی
│   └── js/
│       └── supabase.js      ✅ کار می‌کنه (PATCH-based)
└── .env                     ✅
```

---

## وضعیت هر صفحه

---

### 1. index.html (Home Screen) ✅ کامل

**چی هست:**
- هدر "My Portfolio" با $0.00 و دکمه "Add wallet address"
- 4 کارت اصلی: Crypto، Metals، Stocks & Oil، More
- هر کارت آیکون AI-generated PNG داره (تو assets/icons/)
- Bottom Nav: Home, Watchlist, Alerts, Settings
- استایل: گلس‌مورفیسم تیره (#0A0C10)

**قرار چیکار کنیم:**
- وقتی پورتفولیو واقعی وصل شد، $0.00 رو با موجودی واقعی عوض کنیم
- Bottom Nav رو به صفحات مربوطه وصل کنیم

---

### 2. crypto.html ✅ تقریباً کامل

**چی هست:**
- کوین‌های انتخابی کاربر از Supabase خونده می‌شه
- قیمت‌های واقعی از CoinGecko API (هر 60 ثانیه آپدیت)
- آیکون همه کوین‌ها از jsdelivr CDN
- دکمه Manage crypto → manage-crypto.html
- دکمه Reset → برمی‌گرده به 5 کوین پیش‌فرض
- بدون رفرش آپدیت می‌شه (visibilitychange)

**قرار چیکار کنیم:**
- هیچی، فعلاً کامله ✅

---

### 3. manage-crypto.html ✅ کامل

**چی هست:**
- لیست 30 کوین با toggle switch گلس‌مورفیسم
- آیکون همه کوین‌ها از CDN
- وضعیت toggle از Supabase خونده می‌شه
- هر تغییر بلافاصله در Supabase ذخیره می‌شه
- badge بالا تعداد کوین‌های انتخابی رو نشون می‌ده

**قرار چیکار کنیم:**
- هیچی، فعلاً کامله ✅

---

### 4. coin-detail.html ⚠️ ناقص — اولویت بالا

**چی هست:**
- هدر با قیمت + درصد تغییر
- نمودار خطی زیبا با انیمیشن + tooltip لمسی
- تب‌های زمانی: LIVE, 1H, 1D, 1W, 1M, 1Y
- بخش Stats: Market Cap, 24h Volume, Circulating Supply, All-Time High
- بخش About: دکمه‌های Contract address و Website

**مشکل فعلی:**
- همیشه BTC نشون می‌ده! باید از URL param بخونه (`?coin=ETH`)
- داده‌های نمودار hardcoded هستن — باید از CoinGecko market_chart بیاد
- Stats داده‌های واقعی نداره

**قرار چیکار کنیم:**
1. از URL param کوین رو بخونه: `const coin = new URLSearchParams(location.search).get('coin') || 'BTC'`
2. CoinGecko ID رو پیدا کنه و قیمت + تغییر رو بگیره
3. نمودار رو از `market_chart` API بکشه (endpoint: `/coins/{id}/market_chart?vs_currency=usd&days=1`)
4. Stats واقعی از `/coins/{id}` API بگیره (market_cap, volume, supply, ath)

---

### 5. metals.html ❌ نساخته — اولویت متوسط

**قرار چیکار کنیم:**
- مشابه crypto.html ولی برای فلزات
- کوین‌ها: طلا (XAU)، نقره (XAG)، مس، پلاتین
- API پیشنهادی: metals.live یا همون CoinGecko (PAXG برای طلا)
- آیکون‌ها: عکس‌های AI-generated (مثل شمش‌هایی که داریم)

---

### 6. stocks.html ❌ نساخته — اولویت متوسط

**قرار چیکار کنیم:**
- نمایش سهام (AAPL, TSLA, NVDA و...) + نفت (WTI, Brent)
- API پیشنهادی: Yahoo Finance (غیررسمی، رایگان) یا Alpha Vantage (رایگان با محدودیت)
- سطر اول: شاخص‌های کلی (S&P 500, NASDAQ, DOW)
- سطر دوم: سهام‌های محبوب

---

### 7. more.html ❌ خالی — اولویت پایین‌تر

**قرار چیکار کنیم (6 کارت):**

| کارت | توضیح | پیچیدگی |
|------|-------|---------|
| Alerts & Tracking | هشدار قیمتی (مثلاً BTC زیر 60k) | متوسط |
| Personalize | تغییر تم، ترتیب کارت‌ها | آسان |
| Asset Analysis | Fear & Greed Index، Heatmap | متوسط |
| Social | اشتراک‌گذاری قیمت به صورت کارت زیبا | آسان |
| Local Market | **نقطه تمایز اصلی** — دلار آزاد، سکه، بورس تهران | سخت (API ایرانی) |
| Quick Tools | ماشین حساب P&L، تبدیل واحد | آسان |

---

## لیست 30 کوین

```
BTC, ETH, USDT, XRP, SOL, USDC, TRX, HYPE, ADA, DOGE,
AVAX, SUI, LINK, DOT, LTC, POL, SHIB, BCH, TON, UNI,
ICP, NEAR, APT, XLM, ATOM, FIL, ARB, OP, XMR, PEPE
```

**5 پیش‌فرض**: BTC, ETH, USDT, XRP, SOL

**آیکون CDN**: `https://cdn.jsdelivr.net/gh/spothq/cryptocurrency-icons@master/128/color/{name}.png`
- POL → `matic.png`
- بقیه با اسم خودشون (btc, eth, usdt, ...)

**CoinGecko IDs**:
```javascript
BTC:'bitcoin', ETH:'ethereum', USDT:'tether', XRP:'ripple', SOL:'solana',
USDC:'usd-coin', TRX:'tron', ADA:'cardano', DOGE:'dogecoin', AVAX:'avalanche-2',
SUI:'sui', LINK:'chainlink', DOT:'polkadot', LTC:'litecoin', POL:'matic-network',
SHIB:'shiba-inu', BCH:'bitcoin-cash', TON:'the-open-network', UNI:'uniswap',
ICP:'internet-computer', NEAR:'near', APT:'aptos', XLM:'stellar', ATOM:'cosmos',
FIL:'filecoin', ARB:'arbitrum', OP:'optimism', XMR:'monero', PEPE:'pepe', HYPE:'hyperliquid'
```

---

## قدم‌های بعدی (اولویت‌بندی)

### 🔴 فوری
1. **coin-detail.html** — وصل به کوین خاص + قیمت واقعی + نمودار واقعی

### 🟡 بعدی
2. **GitHub + Vercel** — هاست HTTPS واقعی (لازمه برای تلگرام)
3. **اتصال به بات تلگرام** — تنظیم Menu Button
4. **جایگزین TELEGRAM_USER_ID** با ID واقعی از Telegram SDK

### 🟢 بعداً
5. metals.html
6. stocks.html
7. more.html (Local Market = اولویت بالای این بخش)
8. پورتفولیو (اتصال کیف‌پول با آدرس عمومی)
9. سیستم اشتراک ماهانه

---

## نکات فنی مهم برای Claude Code

- **supabase.js**: از PATCH استفاده می‌کنه (نه POST) — نباید تغییر کنه
- **Unique Constraint**: روی (telegram_user_id, coin_symbol) در Supabase فعاله
- **استایل**: گلس‌مورفیسم تیره — همه صفحات باید یکدست باشن
- **فونت**: Manrope (متن) + JetBrains Mono (قیمت‌ها)
- **پس‌زمینه**: #0A0C10 با radial-gradient بنفش/آبی
- **CoinGecko**: رایگان، نیاز به API key نداره، محدودیت 100 call/دقیقه
