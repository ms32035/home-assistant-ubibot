"""Ubibot sensor."""

from datetime import datetime
import json
import logging
import threading
import typing

import requests

from homeassistant.const import CONF_API_KEY, CONF_SCAN_INTERVAL
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.typing import DiscoveryInfoType
from homeassistant.helpers.device_registry import DeviceInfo

if typing.TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from homeassistant.config_entries import ConfigEntry
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import SENSOR_TYPES, MODELS, DOMAIN, CONF_CHANNEL

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
        hass: "HomeAssistant",
        config_entry: "ConfigEntry",
        async_add_entities: "AddEntitiesCallback",
):
    """Ubibot sensor setup."""

    config_data = hass.data[DOMAIN]
    api_key = config_data[CONF_API_KEY]
    channel = config_data[CONF_CHANNEL]
    scan_interval = config_data[CONF_SCAN_INTERVAL]

    ubibot_data = UbibotData(api_key, channel, scan_interval)

    for t in SENSOR_TYPES.keys():
        async_add_entities([UbibotSensor(t, channel, ubibot_data)])


class UbibotSensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, sensor_type, channel, ubibot_data):
        """Initialize the sensor."""
        self._type = sensor_type
        self._channel = channel
        self._ubibot_data = ubibot_data
        self._state = self._ubibot_data.data["channel"]["last_values"][
            SENSOR_TYPES[self._type]["field"]
        ]["value"]

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"Ubibot - {self._channel} - {self._type}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self._state

    @property
    def device_class(self) -> str:
        """Return the device class of the sensor."""
        return SENSOR_TYPES[self._type]["class"]

    @property
    def native_unit_of_measurement(self) -> str:
        """Return the native unit of measurement."""
        return SENSOR_TYPES[self._type]["unit"]

    @property
    def icon(self) -> str:
        """Return the icon."""
        return SENSOR_TYPES[self._type]["icon"]

    @property
    def unique_id(self) -> [str]:
        """Return the unique_id."""
        return f"{self._channel}_{self._type}"

    async def async_update(self):
        """Fetch new state data for the sensor."""
        self._ubibot_data.update()
        self._state = self._ubibot_data.data["channel"]["last_values"][
            SENSOR_TYPES[self._type]["field"]
        ]["value"]

    @property
    def state_class(self) -> SensorStateClass:
        """Return sensor state class"""
        return SensorStateClass.MEASUREMENT

    @property
    def device_info(self) -> DeviceInfo:
        """Return device"""

        return DeviceInfo(
            identifiers={(DOMAIN, self._ubibot_data.data["channel"]["full_serial"])},
            name=self._ubibot_data.data["channel"]["full_serial"],
            serial_number=self._ubibot_data.data["channel"]["full_serial"],
            sw_version=self._ubibot_data.data["channel"]["firmware"],
            manufacturer="Ubibot",
            model=MODELS.get(
                self._ubibot_data.data["channel"]["product_id"],
                self._ubibot_data.data["channel"]["product_id"],
            ),
            model_id=self._ubibot_data.data["channel"]["product_id"],
        )


class UbibotData:
    """Ubibot data object."""

    URL = "https://api.ubibot.io/channels/{0}?account_key={1}"

    def __init__(self, account_key, channel, scan_interval):
        """
        Initialize the UniFi Ubibot data object.

        :param account_key: Ubibot Account Key
        :param channel: Channel ID
        :param scan_interval: refresh interval in seconds
        """
        self.account_key = account_key
        self.channel = channel
        self.scan_interval = scan_interval
        self.last_refresh = datetime(2000, 1, 1)
        self.data = None
        self._update_in_progress = threading.Lock()
        self.update()

    def update(self):
        """Get data from Ubibot API."""
        if (
            datetime.now() < self.last_refresh + self.scan_interval
            or not self._update_in_progress.acquire(False)
        ):
            return
        try:
            url = UbibotData.URL.format(self.channel, self.account_key)
            r = requests.get(url)
            if r.status_code == 200:
                self.data = json.loads(r.text)
                self.data["channel"]["last_values"] = json.loads(
                    self.data["channel"]["last_values"]
                )
            else:
                _LOGGER.error(r.status_code)
            self.last_refresh = datetime.now()
        finally:
            self._update_in_progress.release()
