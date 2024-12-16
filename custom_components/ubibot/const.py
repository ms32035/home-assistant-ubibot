"""Constants for Ubibot module."""

from homeassistant.components.sensor.const import SensorDeviceClass
from homeassistant.const import (
    LIGHT_LUX,
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    UnitOfTemperature,
)

SENSOR_TYPES = {
    "temperature": {
        "class": SensorDeviceClass.TEMPERATURE,
        "unit": UnitOfTemperature.CELSIUS,
        "icon": "mdi:thermometer",
        "field": "field1",
    },
    "humidity": {
        "class": SensorDeviceClass.HUMIDITY,
        "unit": PERCENTAGE,
        "icon": "mdi:water-percent",
        "field": "field2",
    },
    "lux": {
        "class": SensorDeviceClass.ILLUMINANCE,
        "unit": LIGHT_LUX,
        "icon": "mdi:lightbulb-on-outline",
        "field": "field3",
    },
    "wifi_rssi": {
        "class": SensorDeviceClass.SIGNAL_STRENGTH,
        "unit": SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        "icon": "mdi:wifi",
        "field": "field5",
    },
}

MODELS = {"ubibot-ws1": "WS1"}

CONF_CHANNEL = "channel"

DOMAIN = "ubibot"
