export default function EventDetails({
  event,
}) {
  if (!event) {
    return (
      <div className="bg-slate-800 border border-slate-700 rounded-xl p-6">
        <h2 className="text-xl font-semibold mb-3">
          Event Details
        </h2>

        <p className="text-slate-400">
          Select an event to view its details.
        </p>
      </div>
    );
  }

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6">
      <h2 className="text-xl font-semibold">
        {event.Event}
      </h2>

      <p className="text-blue-400 mt-2">
        {event.Date}
      </p>

      <div className="mt-4 space-y-2">
        <p>
          <span className="font-semibold">
            Category:
          </span>{" "}
          {event.Category}
        </p>

        <p>
          <span className="font-semibold">
            Description:
          </span>{" "}
          {event.Description}
        </p>
      </div>
    </div>
  );
}