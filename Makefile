run:
	docker rm -f homeassistant || true
	docker run -d --name homeassistant -e TZ=Pacific/Auckland -v $(shell realpath config):/config -v $(shell realpath electric_kiwi):/config/custom_components/electric_kiwi --network=host ghcr.io/home-assistant/home-assistant:stable

shell:
	docker exec -it homeassistant /bin/bash