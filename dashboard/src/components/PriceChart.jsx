// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   Tooltip,
//   CartesianGrid,
//   ResponsiveContainer,
//   ReferenceLine,
// } from "recharts";

// export default function PriceChart({ prices, changePoint, selectedEvent }) {
//   return (
//     <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg mt-8">
//       <div className="mb-6">
//         <h2 className="text-2xl font-semibold text-white">
//           Brent Oil Price History
//         </h2>

//         <p className="text-slate-400 mt-1">
//           Historical Brent crude oil prices with the detected Bayesian change point.
//         </p>
//       </div>

//       <div style={{ width: "100%", height: 500 }}>
//         <ResponsiveContainer>
//           <LineChart data={prices}>
//             <CartesianGrid
//               stroke="#334155"
//               strokeDasharray="4 4"
//             />

//             <XAxis
//               dataKey="Date"
//               stroke="#CBD5E1"
//               tick={{ fontSize: 12 }}
//               minTickGap={50}
//             />

//             <YAxis
//               stroke="#CBD5E1"
//               tick={{ fontSize: 12 }}
//             />

//             <Tooltip
//               contentStyle={{
//                 backgroundColor: "#1E293B",
//                 border: "1px solid #334155",
//                 color: "#fff",
//               }}
//             />

//             <ReferenceLine
//               x={changePoint.change_date}
//               stroke="#EF4444"
//               strokeWidth={2}
//               strokeDasharray="6 6"
//               label={{
//                 value: "Change Point",
//                 position: "insideTopRight",
//                 fill: "#EF4444",
//               }}
//             />

//             <Line
//               type="monotone"
//               dataKey="Price"
//               stroke="#3B82F6"
//               strokeWidth={2}
//               dot={false}
//               activeDot={{ r: 5 }}
//             />
//           </LineChart>
//         </ResponsiveContainer>
//       </div>
//     </div>
//   );
// }



import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  ReferenceLine,
  Legend,
} from "recharts";

export default function PriceChart({
  prices,
  changePoint,
  selectedEvent,
})

 {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg">

      <div className="mb-6">

        <h2 className="text-2xl font-semibold text-white">
          Brent Oil Price History
        </h2>

        <p className="text-slate-400 mt-1">
          Historical Brent crude oil prices with Bayesian change point detection.
        </p>

      </div>

      <ResponsiveContainer
        width="100%"
        height={500}
      >

        <LineChart
          data={prices}
          margin={{
            top: 20,
            right: 30,
            left: 10,
            bottom: 20,
          }}
        >

          <CartesianGrid
            stroke="#334155"
            strokeDasharray="4 4"
          />

          <XAxis
            dataKey="Date"
            stroke="#CBD5E1"
            tick={{ fontSize: 11 }}
            minTickGap={60}
          />

          <YAxis
            stroke="#CBD5E1"
            tick={{ fontSize: 11 }}
          />

          <Tooltip
            contentStyle={{
              backgroundColor: "#1E293B",
              border: "1px solid #475569",
              borderRadius: "10px",
            }}
          />

          <Legend />

          <ReferenceLine
            x={changePoint.change_date}
            stroke="#EF4444"
            strokeWidth={3}
            strokeDasharray="6 6"
            label={{
              value: "Bayesian Change Point",
              fill: "#EF4444",
              fontSize: 12,
            }}
          />

          {selectedEvent && (

            <ReferenceLine
              x={selectedEvent}
              stroke="#10B981"
              strokeWidth={3}
              label={{
                value: "Selected Event",
                fill: "#10B981",
                fontSize: 12,
              }}
            />

          )}

          <Line
            name="Brent Price"
            type="monotone"
            dataKey="Price"
            stroke="#3B82F6"
            strokeWidth={3}
            dot={false}
            activeDot={{
              r: 6,
            }}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
}