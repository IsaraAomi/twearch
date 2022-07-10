# twearch
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
  ```
- Run python script:
  ```
  $ cd src
  $ python main.py
  ```
- The results are output in `data` directory.
  - Recommend install the following extensions when viewing csv files on VSCode.
    - [Edit csv](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)
    - [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
