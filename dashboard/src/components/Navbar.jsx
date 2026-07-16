export default function Navbar() {
  return (
    <header className="bg-slate-800 border-b border-slate-700 shadow-lg">
      <div className="max-w-7xl mx-auto px-8 py-5 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-white">
            Brent Oil Analytics
          </h1>

          <p className="text-slate-400 mt-1">
            Bayesian Change Point Analysis Dashboard
          </p>
        </div>

        <div className="text-right">
          <p className="text-slate-400 text-sm">
            Birhan Energies
          </p>

          <p className="text-blue-400 font-semibold">
            Data Analytics Platform
          </p>
        </div>
      </div>
    </header>
  );
}