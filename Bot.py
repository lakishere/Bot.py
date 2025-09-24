name: Run Telegram Bot

on:
  schedule:
    - cron: '*/15 * * * *' # كل 15 دقيقة
  workflow_dispatch:

jobs:
  bot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run bot
        run: python bot.py
        env:
          TOKEN: ${{ secrets.BOT_TOKEN }}
