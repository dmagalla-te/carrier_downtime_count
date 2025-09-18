# carrier_downtime_count
P&amp;G requested this script in order to calculate the downtime per service provider


pyinstaller --onefile --noconsole --name "carrier_downtime_count" --distpath "./dist" --workpath "./build" --specpath "." --add-data "config;config" --hidden-import=httpx --hidden-import=pydantic --hidden-import=asyncio --hidden-import=csv --hidden-import=re --hidden-import=datetime --hidden-import=time --clean main_endpoint.py

para mac

pyinstaller --onefile --noconsole --name "carrier_downtime_count" --distpath "./dist" --workpath "./build" --specpath "." --add-data "config:config" --hidden-import=httpx --hidden-import=pydantic --hidden-import=asyncio --hidden-import=csv --hidden-import=re --hidden-import=datetime --hidden-import=time --clean main_endpoint.py