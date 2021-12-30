"""Ubibot component."""

import logging

import voluptuous as vol

from homeassistant.const import CONF_API_KEY, CONF_USERNAME
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)


CONF_CHANNEL = "channel"
CONF_INTERVAL = "scan_interval"

DOMAIN = "ubibot"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_API_KEY): cv.string,
                vol.Required(CONF_CHANNEL): cv.string,
                vol.Required(CONF_USERNAME): cv.string,
                vol.Optional(CONF_INTERVAL): cv.positive_int,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
