# Ubibot integration for Home Assistant

**:warning: Deprecation notice :warning:**

After 6 years of running my Ubibot WS1 I've come to a conclusion that the standards are now 
Matter and Thread. This integration is no longer maintained, but should a new maintainer come,
I'm happy to transfer support them to them. Otherwise, it will stop working soon, when 
Home Assistant drops support for YAML based configurations.

Some attempt to upgrade the integration can be found in the `feature/reafactor` branch.

This repo provides a plugin to work with Ubibot thermometers as sensors

## Installation

Install using HACS

## Configuration

Configure as a sensor in HA YAML configuration.yaml

```
sensor:
  platform: ubibot
  api_key: !secret ubibot_apikey
  channel: !secret ubibot_channel_number
  scan_interval: 900
```

Store secrets in secrets.yaml

```
ubibot_apikey: "YOUR_API_KEY" 
ubibot_channel_number: "YOUR_CHANNEL_NUMBER"
```
