.PHONY: all fetch analyze clean

all: analyze

fetch:
	@echo "--- Fetching data ---"
	bash ./fetch_metars.sh
	@echo "--- Data output into raw_metars directory ---"
	@echo "--- Fetching complete ---"

analyze: fetch
	@echo "--- Analyzing data ---"
	bash ./analyze_data.sh
	@echo "--- Appending data into weather_report.csv ---"
	@echo "--- Pipeline complete ---"

clean:
	@echo "--- Cleaning up ---"
	rm -rf weather_report.csv
	rm -rf raw_metars/
