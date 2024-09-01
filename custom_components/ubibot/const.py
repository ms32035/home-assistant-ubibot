"""Constants for Ubibot module."""
from homeassistant.const import (
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_ILLUMINANCE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    TEMP_CELSIUS,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
)

SENSOR_TYPES = {
    "temperature": {
        "class": DEVICE_CLASS_TEMPERATURE,
        "unit": TEMP_CELSIUS,
        "icon": "mdi:thermometer",
        "field": "field1",
    },
    "humidity": {
        "class": DEVICE_CLASS_HUMIDITY,
        "unit": "%",
        "icon": "mdi:water-percent",
        "field": "field2",
    },
    "lux": {
        "class": DEVICE_CLASS_ILLUMINANCE,
        "unit": "lux",
        "icon": "mdi:lightbulb-on-outline",
        "field": "field3",
    },
    "wifi_rssi": {
        "class": DEVICE_CLASS_SIGNAL_STRENGTH,
        "unit": SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        "icon": "mdi:wifi",
        "field": "field5",
    },
}

MODELS = {"ubibot-ws1": "WS1"}