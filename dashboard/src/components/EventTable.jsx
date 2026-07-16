export default function EventTable({ events }) {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6">
      <h2 className="text-2xl font-semibold mb-6">
        Historical Events
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="border-b border-slate-700">
            <tr>
              <th className="py-3">Date</th>
              <th className="py-3">Event</th>
              <th className="py-3">Category</th>
            </tr>
          </thead>

          <tbody>
            {events.map((event) => (
              <tr
                key={`${event.Date}-${event.Event}`}
                className="border-b border-slate-800 hover:bg-slate-700"
              >
                <td className="py-3">
                  {event.Date}
                </td>

                <td>{event.Event}</td>

                <td>{event.Category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}