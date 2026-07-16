
import { useState, useMemo } from "react";

import Navbar from "../components/Navbar";
import SummaryCards from "../components/SummaryCards";
import PriceChart from "../components/PriceChart";
import EventFilter from "../components/EventFilter";
import EventDetails from "../components/EventDetails";
import EventTable from "../components/EventTable";

import useDashboard from "../hooks/useDashboard";

export default function Dashboard() {
  const {
    prices,
    events,
    summary,
    changePoint,
    loading,
  } = useDashboard();

  const [selectedEvent, setSelectedEvent] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const filteredPrices = useMemo(() => {
    return prices.filter((price) => {
      if (startDate && price.Date < startDate) return false;
      if (endDate && price.Date > endDate) return false;
      return true;
    });
  }, [prices, startDate, endDate]);

  const filteredEvents = useMemo(() => {
    return events.filter((event) => {
      if (startDate && event.Date < startDate) return false;
      if (endDate && event.Date > endDate) return false;
      return true;
    });
  }, [events, startDate, endDate]);

  const selectedEventData = filteredEvents.find(
    (event) => event.Date === selectedEvent
  );

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex justify-center items-center text-white text-2xl">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-900">

      <Navbar />

      <main className="max-w-7xl mx-auto px-8 py-8 space-y-8">

        <SummaryCards
          summary={summary}
          changePoint={changePoint}
        />

        <PriceChart
          prices={filteredPrices}
          changePoint={changePoint}
          selectedEvent={selectedEvent}
        />

        <div className="bg-slate-800 rounded-xl border border-slate-700 p-6">

          <h2 className="text-xl font-semibold mb-5">
            Date Range Filter
          </h2>

          <div className="grid md:grid-cols-2 gap-6">

            <div>
              <label className="block mb-2">
                Start Date
              </label>

              <input
                type="date"
                className="w-full bg-slate-900 border border-slate-600 rounded-lg p-3"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
              />
            </div>

            <div>
              <label className="block mb-2">
                End Date
              </label>

              <input
                type="date"
                className="w-full bg-slate-900 border border-slate-600 rounded-lg p-3"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
              />
            </div>

          </div>

        </div>

        <div className="grid lg:grid-cols-2 gap-8">

          <EventFilter
            events={filteredEvents}
            selectedEvent={selectedEvent}
            setSelectedEvent={setSelectedEvent}
          />

          <EventDetails
            event={selectedEventData}
          />

        </div>

        <EventTable
          events={filteredEvents}
        />

      </main>

    </div>
  );
}