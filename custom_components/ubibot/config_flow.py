from homeassistant import config_entries
from . import DOMAIN, CONFIG_SCHEMA


class UbibotConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Ubibot config flow."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Ubibot", data=user_input)

        return self.async_show_form(step_id="user", data_schema=CONFIG_SCHEMA)
