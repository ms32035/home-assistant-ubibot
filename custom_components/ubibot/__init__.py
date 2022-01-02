"""Ubibot component."""

import logging

import voluptuous as vol

from homeassistant.const import CONF_API_KEY, CONF_USERNAME, CONF_SCAN_INTERVAL
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)


CONF_CHANNEL = "channel"

DOMAIN = "ubibot"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_API_KEY): cv.string,
                vol.Required(CONF_CHANNEL): cv.string,
                vol.Required(CONF_USERNAME): cv.string,
                vol.Optional(CONF_SCAN_INTERVAL): cv.positive_int,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
