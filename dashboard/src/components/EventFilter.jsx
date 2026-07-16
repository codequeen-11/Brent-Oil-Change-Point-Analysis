export default function EventFilter({
  events,
  selectedEvent,
  setSelectedEvent,
}) {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6">
      <h2 className="text-xl font-semibold mb-4">
        Event Highlight
      </h2>

      <select
        value={selectedEvent}
        onChange={(e) => setSelectedEvent(e.target.value)}
        className="w-full bg-slate-900 border border-slate-600 rounded-lg p-3 text-white"
      >
        <option value="">Select an Event</option>

        {events.map((event) => (
          <option
            key={event.Date}
            value={event.Date}
          >
            {event.Date} — {event.Event}
          </option>
        ))}
      </select>
    </div>
  );
}