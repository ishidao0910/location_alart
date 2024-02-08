# How you test LINE MessageAPI

```
curl -i -X POST https://api.line.me/v2/bot/message/push \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer LINE_CHANNEL_ACCESS_TOKEN' \
    -d '{ "to": "MY_LINE_USER_ID", "messages": [{ "type": "text", "text": "hello world" }] }'
```

