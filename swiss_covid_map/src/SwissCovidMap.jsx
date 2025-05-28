import React, { useState, useEffect } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { csv } from "d3-fetch";

const CSV_PATH = "/data/COVID19Cases_geoRegion_w.csv";

export default function SwissCovidMap() {
  const [selectedWeekIndex, setSelectedWeekIndex] = useState(0);
  const [weeklyData, setWeeklyData] = useState({});
  const [weeks, setWeeks] = useState([]);

  useEffect(() => {
    csv(CSV_PATH).then((rawData) => {
      const structured = {};
      rawData.forEach((row) => {
        const week = row.datum;
        const canton = row.geoRegion;
        const entries = parseInt(row.entries);

        if (!structured[week]) structured[week] = {};
        structured[week][canton] = entries;
      });
      const sortedWeeks = Object.keys(structured).sort();
      setWeeklyData(structured);
      setWeeks(sortedWeeks);
    });
  }, []);

  if (weeks.length === 0) return <div>Loading data...</div>;

  const selectedWeek = weeks[selectedWeekIndex];
  const dataForWeek = weeklyData[selectedWeek];
  const maxCases = Math.max(
    ...Object.values(weeklyData).flatMap(weekData => Object.values(weekData))
  );

  function getColor(value, maxValue) {
    const intensity = value / maxValue;
    const red = 255;
    const greenBlue = 255 - Math.floor(intensity * 255);
    return `rgb(${red}, ${greenBlue}, ${greenBlue})`;
  }

  return (
    <div className="p-4 space-y-4">
      <h1 className="text-xl font-bold">COVID-19 in Switzerland (Week {selectedWeek})</h1>

      <div className="w-full overflow-auto">
        <ComposableMap
          projection="geoMercator"
          width={1200}
          height={1000}
          projectionConfig={{ scale: 13000, center: [8.3, 46.8] }}
        >
          <Geographies geography="/data/swiss-maps.json">
            {({ geographies }) =>
              geographies.map((geo) => {
                const cantonCode = geo.properties.name; // Should be 2-letter codes like "ZH", "BE"
                const value = dataForWeek[cantonCode] || 0;
                const fill = getColor(value, maxCases);

                return (
                  <Geography
                    key={geo.rsmKey}
                    geography={geo}
                    fill={fill}
                    stroke="#333"
                    style={{
                      default: { outline: "none" },
                      hover: { outline: "none" },
                      pressed: { outline: "none" },
                    }}
                  />
                );
              })
            }
          </Geographies>
        </ComposableMap>
      </div>

      <div className="flex flex-col items-start">
        <label>Week</label>
        <input
          type="range"
          min={0}
          max={weeks.length - 1}
          value={selectedWeekIndex}
          onChange={(e) => setSelectedWeekIndex(parseInt(e.target.value))}
        />
        <span>{selectedWeek}</span>
      </div>
    </div>
  );
}
