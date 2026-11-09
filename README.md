<div align="center">

# 📈 AI Stock Analysis System

[![GitHub stars](https://img.shields.io/github/stars/ZhuLinsen/daily_stock_analysis?style=social)](https://github.com/ZhuLinsen/daily_stock_analysis/stargazers)
[![arXiv](https://img.shields.io/badge/arXiv-2608.26990-b31b1b.svg)](https://arxiv.org/abs/2608.26990)
[![CI](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/r/zhulinsen/daily_stock_analysis)

<p align="center">
  <img src="https://trendshift.io/api/badge/trendshift/repositories/18527/daily?language=Python" alt="#1 Python Repository Of The Day | Trendshift" width="250" height="55"/>&nbsp;<a href="https://hellogithub.com/repository/ZhuLinsen/daily_stock_analysis" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=6daa16e405ce46ed97b4a57706aeb29f&claim_uid=pfiJMqhR9uvDGlT&theme=neutral" alt="Featured｜HelloGitHub" width="230" /></a>
</p>

> 🤖 AI-powered stock analysis system for A-shares / Hong Kong / US / Japanese / Korean / Taiwan watchlists. It runs daily and pushes a decision dashboard to WeChat Work, Feishu, Telegram, Discord, Slack, or email.

[**Product Preview**](#-product-preview) · [**Key Features**](#-key-features) · [**Quick Start**](#-quick-start) · [**Sample Output**](#-sample-output) · [**Documentation Index**](docs/INDEX_EN.md) · [**Full Guide**](docs/full-guide_EN.md)

English | [Chinese](README.md) | [Traditional Chinese](docs/README_CHT.md)

</div>

<details open>
<summary><strong>💖 Sponsors</strong></summary>
<hr>
<div align="center">
  <p><a href="https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis"><img src="./docs/assets/modelflare_banner_en.png" alt="Modelflare" width="720"></a><br>Thanks to <strong>Modelflare</strong> for sponsoring this project. From the United States and operated by Havenbyte LLC, it provides full-strength and stable access to GPT, Claude, Gemini, Grok, and 40+ image/video models at a low cost. Selected OpenAI groups offer <strong>65% / 75% / 85% daily cache-hit guarantees</strong>; a single <strong>US$20 top-up unlocks GPT at 0.015x</strong>, and <strong>US$50 unlocks Claude at 0.03x</strong>. <a href="https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis">Register via this exclusive link</a></p>
  <hr>
  <p>
    <a href="https://serpapi.com/github-daily-stock-analysis" target="_blank"><img src="./docs/assets/serpapi_banner_en.png" alt="Easily scrape real-time financial news data from search engines - SerpApi" width="300" height="141" style="width: 300px; height: 141px; object-fit: contain;"></a>
  </p>
</div>
</details>

## 🖥️ Product Preview

<p align="center">
  <img src="docs/assets/readme_workspace_tour_20260510.gif" alt="DSA Web workspace demo" width="720">
</p>

## ✨ Key Features

| Capability | Coverage |
|------------|----------|
| AI decision reports | Core conclusion, score, trend, entry/exit levels, risk alerts, catalysts, and action checklist |
| Multi-market data | Covers A-shares, Hong Kong, US, Japanese, Korean, Taiwan stocks, ETFs, quotes, K-lines, technical indicators, news, announcements, fundamentals, and report support data. See [market coverage](docs/market-support.md) |
| Web / desktop workspace | Manual analysis, task progress, history, full Markdown reports, backtests, portfolio, settings, and light/dark themes |
| Agent strategy chat | Multi-turn Q&A with 15 built-in strategies across Web / Bot / API |
| Smart import & autocomplete | Image, CSV/Excel, and clipboard import; code/name/pinyin/alias autocomplete |
| Automation & notifications | GitHub Actions, Docker, local scheduler, FastAPI service, and WeChat Work / Feishu / Telegram / Discord / Slack / email delivery |

> For detailed field contracts, fundamental P0 timeout semantics, trading rules, data-source priority, and Web/API behaviors, please read the [Full Guide](docs/full-guide_EN.md).

### Tech Stack & Data Sources

| Type | Supported |
|------|-----------|
| AI Models | [Modelflare](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis), [AIHubMix](https://inferera.com/?aff=CfMq), Gemini, OpenAI-compatible providers, DeepSeek, Qwen, Claude, Ollama |
| Market Data | AkShare, Tushare, Pytdx, Baostock, YFinance, Longbridge |
| News Search | [Anspire](https://open.anspire.cn/dsa?share_code=QFBC0FYC), [SerpAPI](https://serpapi.com/github-daily-stock-analysis), [Tavily](https://tavily.com/), [Bocha](https://open.bocha.cn/), [Brave](https://brave.com/search/api/), [MiniMax](https://platform.minimaxi.com/), SearXNG |
| Social Sentiment | [Stock Sentiment API](https://api.adanos.org/docs) for Reddit / X / Polymarket, US stocks only |

> The project includes free market-data sources such as AkShare, Baostock, and YFinance and can run without extra credentials. These free sources can be rate-limited, change upstream contracts, or be affected by network conditions, so stability is not guaranteed. For batch or scheduled analysis, or for steadier quotes, configure token-based sources such as Tushare or Longbridge. See [Data Source Configuration](docs/full-guide_EN.md#data-source-configuration).

## 🚀 Quick Start

### Option 1: GitHub Actions (Recommended)

> Deploy in about 5 minutes and require no server or infrastructure setup.

#### 1. Fork this repository

Click `Fork` in the upper-right corner. A star is always appreciated.

#### 2. Configure Secrets

Open your forked repository and go to `Settings` → `Secrets and variables` → `Actions` → `New repository secret`.

**AI model configuration (configure at least one)**

Start with one provider and one API key. For multi-model routing, image recognition, local models, or advanced routing, refer to the [LLM configuration guide](docs/LLM_CONFIG_GUIDE_EN.md).

| Secret Name | Description | Required |
|-------------|-------------|:--------:|
| `MODELFLARE_KEY` | [Modelflare](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis) API key for leading global models at a lower cost | Recommended |
| `AIHUBMIX_KEY` | [AIHubMix](https://inferera.com/?aff=CfMq) API key; one key can switch across model families and includes a 10% discount for this project | Recommended |
| `GEMINI_API_KEY` | Google Gemini API key | Optional |
| `ANTHROPIC_API_KEY` | Anthropic Claude API key | Optional |
| `OPENAI_API_KEY` | OpenAI-compatible API key, including DeepSeek and Qwen-compatible services | Optional |
| `OPENAI_BASE_URL` / `OPENAI_MODEL` | Fill these when using an OpenAI-compatible provider | Optional |

> Ollama is better suited for local and Docker deployment. GitHub Actions is usually smoother with a cloud API.

**Notification channels (configure at least one)**

| Secret Name | Description |
|-------------|-------------|
| `WECHAT_WEBHOOK_URL` | WeChat Work bot |
| `FEISHU_WEBHOOK_URL` | Feishu bot |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Telegram |
| `DISCORD_WEBHOOK_URL` | Discord webhook |
| `SLACK_BOT_TOKEN` + `SLACK_CHANNEL_ID` | Slack bot |
| `EMAIL_SENDER` + `EMAIL_PASSWORD` | Email push |

See [Notification Configuration](docs/full-guide_EN.md#notification-channel-configuration) for more channels, signature checks, grouped email, and Markdown-to-image settings.

**Watchlist (required)**

| Secret Name | Description | Required |
|-------------|-------------|:--------:|
| `STOCK_LIST` | Watchlist codes such as `600519,hk00700,AAPL,7203.T,005930.KS,2330.TW`; explicitly registered indices like `sh000016` and `930606.CSI` are also supported through the `--stocks` entry or GitHub Actions flow. See [index watchlist setup](docs/full-guide_EN.md#index-watchlist-configuration). | ✅ |

**News source configuration (recommended)**

News sources significantly affect sentiment, announcements, event analysis, and market trend detection. For details, see [Full Guide](docs/full-guide_EN.md).

#### 3. Run the workflow

```bash
python main.py
python main.py --debug
python main.py --schedule
python main.py --serve
python main.py --serve-only
```

> For Docker, scheduled tasks, cloud-hosted access, and desktop packaging, refer to the [Full Guide](docs/full-guide_EN.md) and [Desktop Packaging Guide](docs/desktop-package.md).

## 📱 Sample Output

### Decision Dashboard

```text
🎯 2026-02-08 Decision Dashboard
3 stocks analyzed | 🟢 Buy: 0 🟡 Watch: 2 🔴 Sell: 1

📊 Summary
⚪ Zhongtu High-Tech (000657): Watch | Score 65 | Bullish
⚪ Yungding Shares (600105): Watch | Score 48 | Range-bound
🟡 Xinlai Yichuang (300260): Sell | Score 35 | Bearish
```

### Market Review

```text
🎯 2026-01-10 Market Review

📊 Major indexes
- Shanghai Composite: 3250.12 (🟢+0.85%)
- Shenzhen Component: 10521.36 (🟢+1.02%)
- ChiNext: 2156.78 (🟢+1.35%)
```

## ⚙️ Configuration

Complete environment variables, model providers, notification channels, data-source priorities, trading discipline, fundamental P0 timeout semantics, and deployment details are documented in the [Full Guide](docs/full-guide_EN.md).

## 🖥️ Web Interface

The Web workspace provides config management, task monitoring, manual analysis, history, full Markdown reports, agent Q&A, backtests, holdings, smart import, and light/dark themes.

```bash
python main.py --webui
python main.py --webui-only
```

Open `http://127.0.0.1:8000` in a browser. For authentication, smart import, search autocomplete, history-copy, and cloud access details, see the [local WebUI guide](docs/full-guide_EN.md#local-webui-management-interface).

## 🤖 Agent Strategy Q&A

Once a usable AI API key is configured, the Web `/chat` page supports strategy Q&A. You can disable it explicitly via `AGENT_MODE=false`.

- Built-in strategies include moving-average crossovers, wave theory, trend-following, hot themes, event-driven analysis, growth quality, and expectation re-rating.
- Supports live quotes, K-line data, technical indicators, news, and risk analysis.
- Supports multi-turn conversation, exporting sessions, sending results to notifications, and background execution.
- Supports custom strategy files and multi-agent orchestration (experimental).

> For agent parameters, `skill` compatibility, multi-agent mode, and budget guardrails, see [Full Guide](docs/full-guide_EN.md#local-webui-management-interface) and [LLM Configuration Guide](docs/LLM_CONFIG_GUIDE_EN.md).

## 🧩 Related Projects

> DSA focuses on daily analysis reports; AlphaSift provides reference logic for stock screening, while AlphaEvo is used for strategy validation and evolution.

| Project | Focus |
|---------|-------|
| [AlphaSift](https://github.com/ZhuLinsen/alphasift) | Reference implementation for the DSA stock-selection pipeline |
| [AlphaEvo](https://github.com/ZhuLinsen/alphaevo) | Strategy backtesting and self-evolution for validating rule sets and parameter combinations |

## 📬 Contact & Collaborations

| Channel | Detail |
|---------|--------|
| Email | [zhuls345@gmail.com](mailto:zhuls345@gmail.com) |
| Xiaohongshu | [Follow us](http://xhslink.com/m/tU520DWCKT) |
| Issues | [Submit an issue](https://github.com/ZhuLinsen/daily_stock_analysis/issues) |

## 📄 License

[MIT License](LICENSE) © 2026 ZhuLinsen

Please note the source of this repository in any downstream use or derivative work. Thank you for supporting continued maintenance.

## ⚠️ Disclaimer

This project is intended for learning and research only and does not constitute investment advice. The stock market is risky; invest carefully. The author is not responsible for any losses arising from use of this project.

---
