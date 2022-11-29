"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


async def async_setup(hass, config_entry, async_add_entities):
    """Add sensors for passed config_entry in HA."""
    #hub = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([HourOfPower()])


class HourOfPower(BinarySensorEntity):
    """Representation of a Sensor."""2

    _attr_name = "Hour of Power"

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_is_on = False