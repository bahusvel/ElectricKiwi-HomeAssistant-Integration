from __future__ import annotations
from .const import DOMAIN

PLATFORMS: list[str] = ["binary_sensor"]

async def async_setup(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.states.async_set(DOMAIN+".world", "Paulus")
    hass.async_add_job(hass.config_entries.async_forward_entry_setup(entry, 'binary_sensor'))

    # Return boolean to indicate that initialization was successful.
    return True