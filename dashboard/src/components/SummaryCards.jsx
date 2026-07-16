export default function SummaryCards({ summary, changePoint }) {
  const cards = [
    {
      title: "Average Price",
      value: `$${summary.average_price}`,
      color: "text-green-400",
    },
    {
      title: "Volatility",
      value: summary.volatility,
      color: "text-yellow-400",
    },
    {
      title: "Historical Events",
      value: summary.total_events,
      color: "text-blue-400",
    },
    {
      title: "Change Point",
      value: changePoint.change_date,
      color: "text-red-400",
    },
  ];

  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg hover:shadow-blue-500/20 transition-all duration-300"
        >
          <p className="text-slate-400 text-sm">{card.title}</p>

          <h2 className={`text-3xl font-bold mt-2 ${card.color}`}>
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}