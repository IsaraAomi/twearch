# twearch
## Description
- This program allows you to search for any string of tweets from users you follow, specifying a date interval.
- The results can be retrieved as a list in the form of a csv file.

## Requirements
- Python version: `3.8.12`
- Install `tweepy`:
  ```
  $ pip install tweepy
  ```

## Usage
- Copy `src/private_info_dummy.py` to `src/private_info.py`.
  ```
  $ cd src
  $ cp private_info_dummy.py private_info.py
  ```
- Edit `src/private_info.py` according to your API and token information.
  - How to get your API and token information:
    - [【Twitter】APIキー利用申請から発行までの手順解説｜ツイッター運用自動化アプリ作成に向けた環境構築](https://di-acc2.com/system/rpa/9688/)
- Edit the setting section in `src/main.py`:
  ```python
  SEARCH_END_TIME   = "2022-06-15T00:00:00Z"  # UTC
  SEARCH_START_TIME = "2022-06-10T00:00:00Z"  # UTC
  SEARCH_WORD       = "あなたのサークル"
  SEARCH_WORD_SAT   = "土曜日"
  SEARCH_WORD_SUN   = "日曜日"
  ```
- Run python script:
  ```
  $ cd src
  $ python main.py
  ```
- The results are output in `data` directory.
  - Recommend to install the following extensions when viewing csv files on VSCode.
    - [Edit csv](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)
    - [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
