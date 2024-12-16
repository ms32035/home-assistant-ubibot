"""Ubibot component."""

import logging

import voluptuous as vol

from homeassistant.const import CONF_API_KEY, CONF_SCAN_INTERVAL
from homeassistant.helpers import config_validation as cv

from .sensor import UbibotSensor, UbibotData
from .const import SENSOR_TYPES, CONF_CHANNEL, DOMAIN

_LOGGER = logging.getLogger(__name__)


# DOMAIN = "ubibot"

CONFIG_OPTIONS = vol.Schema(
    {
        vol.Required(CONF_API_KEY): str,
        vol.Required(CONF_CHANNEL): str,
        vol.Required(CONF_SCAN_INTERVAL, default=900): cv.positive_int,
    },
)


async def async_setup_entry(hass, config_entry):
    return True


# async def async_setup_platform(
#         hass,
#         config ,
#         async_add_entities ,
#         discovery_info = None,
# ):
#     config_data = hass.data[DOMAIN]
#     api_key = config_data[CONF_API_KEY]
#     channel = config_data[CONF_CHANNEL]
#     scan_interval = config_data[CONF_SCAN_INTERVAL]
#
#     ubibot_data = UbibotData(api_key, channel, scan_interval)
#
#     for t in SENSOR_TYPES.keys():
#         async_add_entities([UbibotSensor(t, channel, ubibot_data)])
