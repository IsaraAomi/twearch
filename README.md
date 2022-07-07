# twearch
## Requirements
- Install `tweepy`:
  ```
  $ pip install tweepy
  ```

## Usage
- Create `src/private_info.py` as preparation:
  ```python
  class TwitterApiInfo:
      bearer_token        = "YOUR_BEARER_TOKEN"
      consumer_key        = "YOUR_API_KEY"
      consumer_secret     = "YOUR_API_SECRET"
      access_token        = "YOUR_ACCESS_TOKEN"
      access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
  class TwitterMyAccountInfo:
      user_id  = 1234567890
      username = "YOUR_USER_NAME"
      name     = "YOUR_NAME"
  ```
